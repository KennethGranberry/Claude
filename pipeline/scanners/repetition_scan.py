#!/usr/bin/env python3
"""Repetition / frequency scanner — build-order item #1 of the pipeline.

Replaces the chat-model counting in TMM Writing System v1.7 §V.2 (verbatim
repetition) and §III.2 (governing-term frequency/spacing/density). Deterministic:
it counts; it does not judge. Every flag is a candidate for the author to rule on.

Reads .md / .txt directly and .docx via the standard library only (zipfile +
xml.etree) — no third-party package, no network, nothing leaves the machine.

Usage:
    python3 repetition_scan.py PATH [--min-n 4] [--max-n 12] [--term WORD ...]
                                    [--top 40] [--json OUT.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from xml.etree import ElementTree as ET

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# Function words excluded from single-word frequency ranking (they say nothing
# about a manuscript's governing vocabulary). N-gram repetition keeps them —
# a repeated phrase is a repeated phrase regardless of what it is made of.
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on", "at",
    "by", "for", "with", "as", "is", "are", "was", "were", "be", "been", "being",
    "it", "its", "this", "that", "these", "those", "he", "she", "they", "them",
    "his", "her", "their", "we", "us", "our", "you", "your", "i", "me", "my",
    "not", "no", "do", "does", "did", "has", "have", "had", "from", "so", "than",
    "then", "there", "here", "what", "which", "who", "whom", "whose", "when",
    "where", "why", "how", "all", "any", "both", "each", "more", "most", "other",
    "some", "such", "only", "own", "same", "too", "very", "can", "will", "just",
    "would", "should", "could", "into", "about", "over", "out", "up", "down",
    "again", "also", "one", "two", "first", "now", "never", "ever", "yet",
}


def paragraphs_from_docx(path: str) -> list[str]:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    out = []
    for p in root.iter(f"{W_NS}p"):
        text = "".join(t.text or "" for t in p.iter(f"{W_NS}t"))
        if text.strip():
            out.append(text.strip())
    return out


def paragraphs_from_text(path: str) -> list[str]:
    """Markdown/plain text → body paragraphs. Headings, horizontal rules, and
    code fences are dropped; blank lines delimit blocks. Apparatus notes (a
    block that is wholly italicized *...*) are kept but marked, since the author
    may want them excluded from prose counts."""
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    blocks = re.split(r"\n\s*\n", raw)
    out = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        # drop pure structural lines
        lines = [ln for ln in b.splitlines() if ln.strip()]
        if all(ln.lstrip().startswith("#") for ln in lines):
            continue
        if all(set(ln.strip()) <= {"-", "*", "_"} and len(ln.strip()) >= 3 for ln in lines):
            continue
        out.append(b)
    return out


def load_paragraphs(path: str) -> list[str]:
    if path.lower().endswith(".docx"):
        return paragraphs_from_docx(path)
    return paragraphs_from_text(path)


WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")


def tokenize(text: str) -> list[str]:
    return [w.lower() for w in WORD_RE.findall(text)]


def build_token_stream(paras: list[str]):
    """Flat token list with a parallel list mapping each token to its paragraph
    index, so a repeated phrase can be reported with the paragraphs it spans."""
    tokens, owners = [], []
    for i, p in enumerate(paras):
        for w in tokenize(p):
            tokens.append(w)
            owners.append(i)
    return tokens, owners


def repeated_phrases(tokens, owners, min_n, max_n):
    """All token n-grams (min_n..max_n) occurring >1 time, reduced to maximal
    phrases: a shorter phrase is suppressed when a longer repeated phrase with
    the same count contains it (so we report 'the light has never been overcome',
    not its six overlapping fragments)."""
    per_n = {}
    for n in range(min_n, max_n + 1):
        counts = defaultdict(list)
        for i in range(len(tokens) - n + 1):
            counts[tuple(tokens[i:i + n])].append(i)
        per_n[n] = {ph: pos for ph, pos in counts.items() if len(pos) > 1}

    subsumed = set()
    for n in range(max_n, min_n, -1):
        for ph in per_n[n]:
            cnt = len(per_n[n][ph])
            for sub in (ph[:-1], ph[1:]):
                if per_n.get(n - 1, {}).get(sub) and len(per_n[n - 1][sub]) == cnt:
                    subsumed.add((n - 1, sub))

    results = []
    for n in range(max_n, min_n - 1, -1):
        for ph, pos in per_n[n].items():
            if (n, ph) in subsumed:
                continue
            para_ids = sorted({owners[i] for i in pos})
            results.append({
                "phrase": " ".join(ph),
                "length": n,
                "count": len(pos),
                "paragraphs": para_ids,
            })
    results.sort(key=lambda r: (-r["count"], -r["length"], r["phrase"]))
    return results


def term_tracking(paras, terms):
    """Per-term: total count, paragraphs of occurrence, and minimum spacing
    (smallest gap in paragraphs between two occurrences) — the §III.2 inputs."""
    report = {}
    for term in terms:
        t = term.lower()
        hits = [i for i, p in enumerate(paras) if t in tokenize(p)]
        gaps = [b - a for a, b in zip(hits, hits[1:])]
        report[term] = {
            "count": len(hits),
            "paragraphs": hits,
            "min_paragraph_gap": min(gaps) if gaps else None,
            "density_paras_per_hit": round(len(paras) / len(hits), 1) if hits else None,
        }
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path")
    ap.add_argument("--min-n", type=int, default=4)
    ap.add_argument("--max-n", type=int, default=12)
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--term", action="append", default=[])
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    paras = load_paragraphs(args.path)
    tokens, owners = build_token_stream(paras)

    reps = repeated_phrases(tokens, owners, args.min_n, args.max_n)

    word_counts = Counter(w for w in tokens if w not in STOPWORDS and len(w) > 2)

    terms = term_tracking(paras, args.term) if args.term else {}

    print(f"FILE: {args.path}")
    print(f"Body paragraphs: {len(paras)}   Words: {len(tokens)}   "
          f"Unique words: {len(set(tokens))}")
    print()

    print(f"REPEATED PHRASES ({args.min_n}+ words, appearing >1) — "
          f"{len(reps)} maximal phrases")
    print("-" * 64)
    for r in reps[:args.top]:
        locs = ", ".join(f"¶{p}" for p in r["paragraphs"][:8])
        more = "" if len(r["paragraphs"]) <= 8 else f" +{len(r['paragraphs'])-8}"
        print(f"  {r['count']}×  [{r['length']}w]  \"{r['phrase']}\"")
        print(f"        {locs}{more}")
    if len(reps) > args.top:
        print(f"  ... {len(reps) - args.top} more (see --json for the full list)")
    print()

    print(f"TOP CONTENT WORDS (stopwords removed) — first {min(args.top, 25)}")
    print("-" * 64)
    for w, c in word_counts.most_common(min(args.top, 25)):
        print(f"  {c:5d}  {w}")
    print()

    if terms:
        print("TRACKED TERMS (§III.2 frequency / spacing / density)")
        print("-" * 64)
        for term, d in terms.items():
            print(f"  \"{term}\": {d['count']}× | "
                  f"min gap {d['min_paragraph_gap']} ¶ | "
                  f"~1 per {d['density_paras_per_hit']} ¶")
        print()

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({
                "file": args.path,
                "paragraphs": len(paras),
                "words": len(tokens),
                "repeated_phrases": reps,
                "top_words": word_counts.most_common(args.top),
                "tracked_terms": terms,
            }, fh, indent=2)
        print(f"Full machine-readable report → {args.json}")


if __name__ == "__main__":
    main()
