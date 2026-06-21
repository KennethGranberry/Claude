# TMM Writing System v1.7 — Mechanical / Hybrid / Judgment Classification

*Optimization analysis. A proposal for markup — nothing here is authorized or built. Source:
`TMM_Writing_System_v1_7.docx`, read in full. Section references are to that document.*

## Headline finding

The system's **judgment architecture is sound and should not change.** §I.1 (Authorization) is
exactly right: detection/analysis/classification/drafting/presentation to the AI; judgment and
authorization to the author. The problem is not the division of labor in principle. It is that
the system then asks the **chat model to perform the mechanical substrate** — counting,
exhaustive search, spacing, density, adjacency, version-tracking — that feeds those judgments,
and the model cannot do it reliably.

The document proves this against itself. **§XI.8 (the Examination Procedure) was added in v1.5**
(version history, v1.5 note) precisely because, on the Chapter Six pass, *"successive full-text
reads surfaced instances not caught in earlier inventory work"* — i.e., the model missed
instances. The elaborate four-step human procedure (complete inventory → work the list →
post-implementation re-scan → closure) is a **workaround for a tool-shaped problem.** A tool
does exhaustive search correctly in one pass; the procedure that exists to compensate for the
model's unreliability largely dissolves once the counting is mechanized.

So the optimization is not a redesign of the system's intent. It is: **move the mechanical
substrate to deterministic tools; leave every act of judgment and authorization with the
author.**

## MECHANICAL — move to tools (the model should not do these)

- **Governing-term frequency (§III.2):** per-chapter count (max 2), minimum spacing (no two
  within 5 paragraphs), full-manuscript density (≤1 per 15 paragraphs), consecutive-paragraph
  adjacency, defining-passage exemption. → a term-frequency/spacing/density scanner.
- **Verbatim repetition (§V.2):** every phrase of 4+ words appearing more than once; the
  "not primarily" pattern (cap 4). → an n-gram repetition scanner.
- **The Examination Procedure (§XI.8):** exhaustive inventory + post-change verification scan.
  → one search/verify tool pass; the four-step procedure collapses to its result.
- **Version control (§I.2, §X):** new version per change, never skipped/shared/retroactive; the
  version log. → versioning (git already does this reliably).
- **Protected strings (§I.4, §VII.4):** "The light has never been overcome," the Motto, the
  Three Threshold Passages — verify exact text, position, and that they are unchanged. →
  protected-string checker.
- **Formatting commitments (§IV.3):** detect any table, bullet, numbered list, callout box, or
  in-body bold. → format linter.
- **Paragraph-length distribution (§XIII.4):** flag if more than half the paragraphs fall
  within 100 words of one another. → length-distribution tool.
- **Severity assignment (§XI.3):** once counts exist, count → CRITICAL/FLAG/WATCH/CLEAR is a
  deterministic rule. → rules engine over the scanners' output.
- **Voice/technique deployment caps (§XII, §XIII.4):** once voices are tagged, the per-chapter
  and per-essay caps (Voice 2 ≤3–4 sentences; Voice 4 ≤2–3/chapter, ≤2/essay never within 2
  paragraphs; Voice 9 ≤1/chapter) and the adjacency-collision checks are pure counting.
  (Tagging the voices is judgment; counting against the caps is not.)

## HYBRID — tool detects and assembles; author (or model judgment) decides

- **Prohibited expressions (§IV.4):** tool finds every "genuinely / honestly / straightforward"
  exhaustively → author judges filler vs. load-bearing. The system already specifies exactly
  this split. The cleanest hybrid in the document.
- **Repetition classification (§V.2–V.3):** tool surfaces candidates → A/B/C and
  invocation/amplification/restatement are judgment calls.
- **The five monitoring documents (§VI):** tool generates the count-based scaffolding
  (vocabulary counts and density, the phrase register, all locations) → author/model supplies
  the semantic classifications. These become **generated registers, not hand-maintained ones** —
  exactly the "cross-cutting registers, generated not hand-maintained" the pipeline calls for.
- **Tells of Mechanical Composition (§XIII.2–3):** tool flags candidate imposed-rhythm and
  self-narrating patterns → judgment of *earned vs. signature.*
- **The flag packet (§I.1):** tool assembles location + full paragraph + count + threshold +
  proposed resolution → author authorizes. Assembly is mechanical; the authorization is not.

## JUDGMENT — stays with the author; never mechanized

- **Authorization itself (§I.1)** — the spine. Correct as written.
- **The Voice Palette (§XII)** — voice identity, calibration ("too hot/too cold"), deployment
  choices, blending. The artistry is judgment; only the caps are counted.
- **Voice characteristics (§IV.2), architectural decisions (§VII), Notes-vs-text (§VIII),
  Part Two guidance (§IX)** — authorial.
- **The final call on every flagged item** — whether a frequency is load-bearing, whether a
  repetition is Category A and right, whether a "tell" is earned.

## One discipline the system is missing

There is **no citation-verification discipline** anywhere in v1.7 — yet the corpus's most
exposed flank (established separately) is unverified claims: named studies, dates, figures,
quotations. This is a hybrid the system should add: a tool/process that checks every named
source, statistic, and quote against a primary source, returning *claim · source-class ·
primary citation or flag.* It belongs alongside the five monitoring documents as a sixth
register.

## Recommended build order (highest leverage first)

1. **The frequency/repetition/spacing/density scanner.** It replaces §III.2 and §V.2, supplies
   most of §XI.4, and dissolves §XI.8 — the procedure that exists only because the model cannot
   count. This single tool fixes the exact failure the document was patched to work around.
2. **Generate the five monitoring documents (§VI) as registers** from that scanner's output, so
   they stop being hand-maintained and become reliable.
3. **Add the citation-verification register** (the missing discipline).
4. **Protected-string + formatting + paragraph-length checkers** — small, cheap, high-trust.
5. **Voice-cap counting** — only after a voice-tagging convention exists (tagging stays judgment).

## What does not get touched

The authorization spine, the Voice Palette's artistry, the architectural decisions, and every
qualitative judgment. The optimization removes the model from the counting, not the author from
the book.
