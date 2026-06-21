# KennethGranberry.com — Author Website Design Spec (Proposal v0.1)

*A design for your markup. Nothing here is built or authorized. It applies the best-practices
report (`AuthorWebsite_BestPractices_Report.md`) to your actual corpus. Approve, amend, or
strike — then, once approved, I build it. Open decisions are collected at the end (§9); I've
proposed a default for each so the design is concrete, not a questionnaire.*

---

## 1. Positioning — what this site says in one breath

You are not a single-book author; you are a writer with a **body of work converging on one
subject**: *Cultural Disintegration and Formation in the Age of AI* (working descriptor). The
site should read as **a serious author's hub with the order of a small imprint** — a trilogy, a
five-volume work, standalones, and a novel — unified by one voice and one concern.

**The posture is the witness**, taken straight from your own apparatus: declared, not neutral;
grave, literary, precise. The site's design *is* an argument that this is a serious mind worth
reading. Restraint is the strategy. (Report §1, §4, §12.)

**Primary visitor goals, in order:** (1) join the list; (2) start the flagship book
(*The Mirrored Mind*); (3) read an essay and stay.

---

## 2. Information architecture

Five-item main navigation (Report §2, §13):

```
Home  ·  Books  ·  Essays  ·  About  ·  Contact
        └ (Newsletter is a persistent CTA in header/footer, not a nav item)
        └ (Press lives as /press, linked from footer + About)
```

Page/route map:

```
/                     Home
/books                Catalogue (series + standalones + collection + novel)
/books/the-mirrored-mind
/books/what-the-mirror-cannot-see
/books/the-center-that-cannot-be-empty
/books/the-entrepreneurs-blueprint        (collection hub → 5 volumes)
/books/eli                                 (the novel)
/books/<standalones>                       (Wise Life, Jinn, Law Written Twice, Morning Star, Performance Gap)
/essays                Essays index
/essays/<slug>         Individual essay (long-form reading page)
/about                 Bio + the witness stance + headshot
/press                 Media kit (bios, headshots, covers, Q&A, coverage)
/contact               Form (reader + media)
/subscribe             Newsletter landing (+ reader-magnet delivery)
```

**Catalogue organization** (Report §6, §21) — three visual families, one house style:

- **The Trilogy — *Formation in the Age of AI*** — shown with reading order *and* publication
  order made explicit, because they differ:
  - *Reading order:* The Center That Cannot Be Empty → What the Mirror Cannot See →
    The Mirrored Mind: A Modern Prophecy, and the Road to Redemption.
  - *Publication order (reverse):* The Mirrored Mind (flagship) first, then What the Mirror
    Cannot See, then The Center That Cannot Be Empty — ~1 month apart.
  - One color/type treatment binds the three.
- **The Entrepreneur's Blueprint** — a five-volume collection with its own visual family and a
  collection hub page that lists the volumes + the combined edition.
- **Standalones** — The Wise Life · The Jinn Has Left the Bottle · The Law Written Twice · The
  Morning Star · The Performance Gap.
- **ELI** — the novel, given its own page; the fiction is presented distinctly from the
  nonfiction so the two registers don't blur.

---

## 3. Page-by-page design

### Home (Report §3)
- **Hero:** full-width, deep quiet background, generous white space. One grave line — a distilled
  statement of the work's concern (drawn from your own words; candidate source: the Motto or a
  line from the trilogy's thesis). ≤ ~12 words. Beneath it, one sentence of orientation and
  **one** primary CTA: *"Begin with The Mirrored Mind"* or *"Join the readers"* (pick one — §9).
- **Below the fold:** the flagship book (cover + hook + buy/learn), then a compact "The Work"
  band showing the three families, then a single essay teaser, then the newsletter band.
- No autoplay, no carousel auto-rotation, covers supply the only strong color.

### Books index (Report §5, §6)
- Three labelled sections (Trilogy / Blueprint / Standalones) + the novel.
- Each title: cover, one-line hook, link to its page. Reading-order rail for the trilogy.

### Individual book page (Report §5)
Proven layout: hero (cover + hook) → what it confronts (a few lines, not bullets, to suit the
register) → endorsements/blurbs (when you have them) → **look inside** (excerpt / first
section) → purchase (one featured retailer button + a curated few below) → newsletter capture.
Pre-launch titles show a **"Notify me / Pre-order"** capture instead of buy buttons — turning
the launch runway into list growth.

### Essays (Report §10)
- Index of essays (date, title, one-line standfirst). Individual essay = a clean long-form
  reading page: serif body, ample line-height, no sidebar clutter. Each essay ends with a
  newsletter CTA and links to the related book.

### About (Report §4)
- Opens with **the questions the work pursues / the witness stance**, *then* the credentials —
  ideas before résumé. Formal headshot. Short + long bio. Closes with CTAs (books, essays,
  subscribe, contact).

### Press / Media kit (Report §9)
- Short & long bios, downloadable hi/lo-res headshots, cover images, book metadata, 7–10
  interview questions with sample answers, blurbs, past coverage, media contact.

### Contact (Report §11)
- Simple form (name, email, subject, message); optional toggle for "Reader" vs "Media/Business."

### Subscribe (Report §7)
- One promise, one form (name + email). **Reader magnet** (your §9 decision): a strong candidate
  is a standalone essay or a sampler from *The Wise Life* / the trilogy. Welcome sequence (3–5
  emails) drafted later.

---

## 4. Visual system (Report §12, §17)

- **Type:** two faces maximum. Proposed: **Spectral** or **Lora** for body (web-built literary
  serifs), paired with either the same family for headings or a restrained high-contrast serif
  (e.g., **Source Serif** / a display serif) for titles. Final pairing in §9.
- **Color:** near-monochrome, paper-and-ink — warm off-white ground, near-black text, one quiet
  accent (deep oxblood, ink-blue, or bronze) used sparingly for links/CTAs. Covers carry the
  color. Per-series accent tints differentiate the three families without noise.
- **Space:** large margins, long measure capped at ~65–75 characters for readability.
- **Contrast:** WCAG 2.2 AA minimum (4.5:1 body) — comfortably met by near-black on off-white.
- **Reading comfort:** line-height ≥ 1.5; paragraph spacing generous (also AAA typography
  guidance) — fits long-form prose.
- **Motion:** minimal; no autoplay; gentle fades at most.

---

## 5. Technical build (Report §14–§16)

**Recommendation: a static site.** It is the right tool for your situation, and here is why:

- **Fast by default** — meets Core Web Vitals (LCP/INP/CLS) almost automatically; nothing to
  optimize away.
- **You own it outright** — plain files, no platform lock-in, no ad-injecting free tier, host
  anywhere (Netlify, Cloudflare Pages, GitHub Pages) cheaply or free.
- **Confidentiality-safe** — it can be built and previewed entirely in this repo; *no manuscript
  content goes to any external service* during the build. You publish only what you choose.
- **Maintainable** — content (books, essays) as structured Markdown/data files, so adding the
  next title or essay is one file, not a redesign (Report §21).

Proposed stack: **Eleventy (11ty)** or **Astro** as the generator (clean, content-first, no
heavy framework), hand-written CSS (no bloat), `Person`/`Book`/`Article` schema, WebP/AVIF
images, sitemap, semantic HTML, keyboard-navigable, alt text throughout. If you'd rather avoid
a generator entirely, plain hand-built HTML/CSS also works for a site this size.

**Newsletter** integrates via the chosen provider's embed (Kit/MailerLite/Substack/beehiiv —
§9). **Buy links** are simple curated retailer links at launch; **direct sales** can be added
later (Report §8) without rebuilding.

---

## 6. What the design deliberately does *not* do

- No "Dear Reader" homepage letter; no homepage autobiography (Report §20).
- No more than 5 nav items; one primary CTA per page.
- No autoplay media; no decision-fatigue wall of retailer buttons.
- No blurring of the novel with the nonfiction.
- No external transmission of manuscript text in the build.

---

## 7. Build phasing (once approved)

1. **Skeleton + visual system** — layout, type, color, nav, footer, newsletter band; one
   complete page (Home) as the reference.
2. **Books** — index + the flagship book page as the template; then the rest.
3. **About + Contact + Subscribe.**
4. **Essays** — index + reading-page template; migrate selected essays.
5. **Press.**
6. **Technical pass** — schema, performance, accessibility audit, sitemap.
7. **Content load + proofing**, then handoff/publish to the host you choose.

Each phase is one authorized step; I confirm after each (the authorization spine).

---

## 8. How this maps to the best-practices report

Every design choice above traces to a section of the report: positioning/witness (§1, §4, §12);
five-page architecture + 4–5 nav (§2, §13); hero/one-CTA (§3); About-leads-with-ideas (§4);
book-page layout + curated retailers (§5, §8); series/reading-order/imprint treatment (§6, §21);
newsletter spine + reader magnet (§7); press kit (§9); essays (§10); literary serif system
(§12); mobile/performance/SEO/accessibility (§14–§17); domain (§18); maintainability (§19, §21);
mistakes designed around (§20).

---

## 9. Open decisions for you (each with my proposed default)

1. **Domain** — confirm `KennethGranberry.com` as the canonical address. *(Default: yes.)*
2. **Primary homepage CTA** — newsletter sign-up **or** "Begin with The Mirrored Mind"? *(Default:
   newsletter, since the list is the owned asset and the books are pre-launch.)*
3. **Hero line** — which words carry the hero? The Motto, a trilogy thesis line, or something
   written fresh for the site. *(Default: I draft 3 candidates from your texts for you to choose.)*
4. **Reader magnet** — what do new subscribers receive? *(Default: a standalone essay or a Wise
   Life sampler.)*
5. **Newsletter platform** — Kit / MailerLite / Substack / beehiiv. *(Default: Kit (ConvertKit),
   strong for author welcome-sequences; reversible.)*
6. **Direct sales now or later** — retailer links only at launch, or stand up a store too?
   *(Default: retailer links now; direct sales later.)*
7. **Type pairing** — Spectral vs. Lora body; heading face. *(Default: Spectral body + Source
   Serif headings; I'll mock both.)*
8. **Accent color** — oxblood / ink-blue / bronze. *(Default: oxblood, for gravitas.)*
9. **Generator** — 11ty, Astro, or hand-built HTML/CSS. *(Default: 11ty.)*
10. **ELI placement** — feature the novel alongside the nonfiction now, or hold it until the
    nonfiction launches? *(Default: include, on its own page, clearly separated.)*
11. **Headshot & cover assets** — do these exist yet, or are they to come? (Affects what I can
    populate vs. placeholder.)
12. **Launch-state honesty** — show pre-launch titles as "Pre-order/Notify me," or list only what
    is purchasable today? *(Default: show the runway with capture forms — it grows the list.)*

---

*End of proposal v0.1. Mark it up. On your approval — item by item — I build it here, starting
with the skeleton and the Home reference page, manuscript content never leaving the repo.*
