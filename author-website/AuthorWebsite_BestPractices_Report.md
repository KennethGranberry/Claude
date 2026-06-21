# Author & Publisher Website Best Practices — Research Report

*Prepared for Kenneth Granberry. A survey of current (2026) best practices for author and
publishing-house websites, gathered to ground the design of `KennethGranberry.com`. Nothing
here is built or authorized; the design that follows it (`AuthorWebsite_Design_Spec.md`) is a
proposal for your markup.*

---

## 0. Method and source-class — read this first (the honesty boundary)

What this report is, exactly, so you can weigh it correctly:

- **Source-class: popular / practitioner consensus.** The material was gathered through web
  *search* across ~16 targeted queries. The sources are marketing studios, publishing-service
  blogs, author-platform educators (Jane Friedman, Reedsy, BookBub, IngramSpark, Kindlepreneur,
  Author Media), and web-design firms. This is the trade's working consensus — *not*
  peer-reviewed research, and not law. Where a number appears (conversion rates, page-speed
  thresholds), treat it as a cited industry claim, not a verified fact, unless it traces to a
  standards body (WCAG, Google Core Web Vitals — those two are primary and marked **[STD]**).
- **A real limit, stated plainly.** I could **not open** the individual showcased author sites.
  `WebFetch` returns HTTP 403 for every URL in this environment, so I could not study any one
  site's execution directly — only what the search summaries say about them. So where this
  report names an exemplar (e.g., James Kirchick's site), that is *reported*, not *inspected by
  me*. If you want a specific site studied in depth, the honest path is for you to open it and
  paste what you see, or to lift the fetch block.
- **What is therefore reliable here:** the *convergent* practices — the ones every independent
  source repeats. Those are the backbone below. The single-source claims are marked **[single]**.

Full source list at the end (§22).

---

## 1. Strategic foundations — what an author site is *for*

The convergent finding across every source: an author website does three jobs at once, and a
good one does all three without making the visitor choose.

1. **Sell the work** — make the books visible and the path to buying them frictionless.
2. **Establish the person** — who is behind the work and why they are worth trusting (for
   nonfiction, this is *authority*; for fiction, *voice*).
3. **Capture the relationship** — convert a one-time visitor into an owned contact (email),
   because the email list is the only audience a writer truly owns.

The site you control is the **hub**; retailers and social platforms are **spokes** you rent.
The strategic point of the hub is to convert rented attention into owned attention.

---

## 2. Site architecture — the essential pages

Convergent core (every source lists these five):

- **Home** — the storefront window; orient and direct, do not autobiograph.
- **Books** — all titles, how they relate, where to buy.
- **About** — bio + photo + the credibility/voice case.
- **Newsletter / Sign-up** — list capture (often a section on every page rather than only a
  standalone page).
- **Contact** — a form, not a raw email address (spam protection).

Strongly recommended additions:

- **Individual book pages** (one per title) — see §5.
- **Press / Media kit** — see §9.
- **Essays / Writing / Blog** — see §10 (high-value for a nonfiction author who writes essays).
- **Events / Speaking** — if you speak or launch publicly.

Rule repeated everywhere: **4–5 items in the main navigation, no more.** Too many choices
suppress action.

---

## 3. The homepage and hero (above the fold)

- The **hero** is the full-width first screen, visible without scrolling. It must carry: a
  **headline** (≤10 words, a value/identity statement — not "Welcome"), brief supporting text,
  one strong **visual**, and **one** primary call-to-action. Multiple competing CTAs reduce
  click-through.
- **Show, don't autobiograph.** The most-cited homepage mistake: filling it with "Dear Reader"
  welcome letters and the author's life story. The visitor wants to know what's here for them.
- **Book covers are the color.** For a literary site, let generous white space dominate and let
  the covers supply visual energy. Covers should be large and clickable.
- **One clear next step.** Either "start the flagship book" or "join the list" — pick the single
  action you most want and make it unmistakable.
- **No autoplay audio/video** — a near-universal "instant exit" trigger. **[convergent]**
- Performance target: the hero should render in **under ~3 seconds**; first impression is lost
  past that. **[single, but consistent with Core Web Vitals §15]**

---

## 4. The About / bio page (highest-leverage page for nonfiction)

- **Lead with the ideas, then the credentials.** For serious nonfiction, the strong pattern is
  to open with the *core question or philosophy* the work pursues, then establish authority.
  The bio's job is to answer "why should I trust this person on this subject?"
- **Authority through specifics, not adjectives.** Verifiable, third-party credentials and
  concrete particulars outweigh self-described superlatives. Show the practitioner, not the
  theorist.
- **Be selective.** Choose the few credibility points that matter most; leave the exhaustive CV
  elsewhere.
- **Keep multiple bio lengths on hand:** a one-liner (15–30 words), a short version (50–200
  words), and a long-form narrative for the page itself.
- **Third person** is the industry convention for the formal bio (it reads as authority and
  travels into book jackets and guest posts unchanged).
- **A high-quality headshot** that matches the book branding — formal gravitas suits a serious
  nonfiction author (the reported Kirchick example opens this way).
- **Close with calls to action**: discover the books, read the essays, join the list, contact.
- **E-E-A-T [STD-adjacent]:** Google rewards experience/expertise/authority/trust signals; a
  real, specific author bio measurably helps ranking and is the foundation of author schema
  (§16).

---

## 5. The Books page and individual book pages

**Books index page:**

- Every title with its **cover, one-line hook, and a clear path** to learn more / buy.
- Make **relationships between titles legible** — series order, which book starts where,
  standalones vs. collections. (Directly relevant to your trilogy + standalones + 5-volume set.)

**Individual book page (the proven layout, convergent across landing-page sources):**

1. **Hero**: cover + title + a one-sentence hook.
2. **The promise / problem**: a few bullets on what the book does for the reader (or, for
   literary work, what it confronts).
3. **Social proof**: blurbs, endorsements, review pulls, "as seen in."
4. **A look inside**: an excerpt or free first chapter — "if the first chapter is good, it does
   the selling." This doubles as a reader magnet (§7).
5. **Purchase options**: a **primary featured buy button**, with secondary retailers listed
   below to avoid decision fatigue. Button copy should be specific ("Get the book,"
   "Pre-order") not "Click here."
6. **Email capture** repeated near the bottom.

- **CTA placement**: a buy/CTA near the top *and* again at the bottom.
- **Multiple retailers, but curated**: Amazon first (where most buyers go), plus a manageable
  few (Bookshop.org, B&N, Apple Books). Too many links cause decision fatigue.
- Reported conversion benchmarks **[single, treat as motivational not promised]**: good book
  landing pages convert ~15–25% to *a buy or an email*; distraction-free sales pages, ~3–5% to
  purchase.

---

## 6. Series, backlist, and collection presentation (publishing-house practices)

Because your work is structured as a trilogy, a five-volume collection, and standalones, the
publisher-side practices apply:

- **Reading-order clarity**: explicitly show sequence and entry points. Don't make the reader
  reconstruct how the books relate.
- **Imprint/series as a branding device**: publishers use series labels and *systematic color
  palettes* to differentiate groups of titles and orient readers. A consistent visual treatment
  per series (the trilogy as one visual family; the Blueprint volumes as another) helps a
  multi-book catalog feel ordered rather than crowded.
- **Search / filter** for larger catalogs (by title, theme) — matters once the catalog grows.
- **Restrained, systematic design** so a growing list still reads as one coherent body of work.

---

## 7. Email list, reader magnet, and newsletter (the spine)

Treated by every source as the single most important conversion asset.

- **The list is the only audience you own** — not subject to a platform's algorithm or
  policy. Build it deliberately.
- **Sign-up visible on every page**, above the fold and again at the bottom.
- **Promise specific value, not "join my mailing list."** Offer a **reader/lead magnet**: for
  nonfiction, a checklist, framework, sample chapter, or a standalone essay; the magnet must be
  *immediately usable* and solve a concrete need. ("How to ___" beats "tips.")
- **Ask for little** — name + email is standard; more fields suppress sign-ups.
- **Welcome sequence (3–5 automated emails):** (1) deliver the magnet; (2) introduce
  yourself/your voice; (3–5) point gently toward the books; then fold into the regular
  newsletter.
- **Platform** (practitioner consensus): ConvertKit/Kit, MailerLite, Substack, or beehiiv for
  newsletters; the choice is yours and is a §design decision.

---

## 8. Selling: direct vs. retailer links

- **Retailer links** are the low-friction default — readers trust and default to Amazon; you
  add a curated few others.
- **Direct sales** (selling from your own store) keep ~100% minus payment fees vs. retailers'
  ~30% cut, **give you the buyer's email and data**, and let you control pricing/bundles/promos.
  Cost: you run the store (Shopify, WooCommerce, Lemon Squeezy/Laterpress for digital).
- **Consensus verdict: both, not either/or.** Offer direct purchase to buyers who are
  platform-agnostic; use retailers to reach new readers. Direct sales reportedly don't
  cannibalize retailer sales and often lift them. **[single]**
- **Recommendation for launch:** start with curated retailer links (simple, fast, credible);
  add direct sales later if/when you want the data and margin. Don't let a store delay the site.

---

## 9. Press / media kit page

For a nonfiction author seeking reviews, interviews, and speaking, a press page is high-value.
Include:

- **Contact** for media (and a business mailing address).
- **Bio** (the short and long versions) + **downloadable hi-res and lo-res headshots** (JPG).
- **Book info**: title, subtitle, pub date, cover copy, ISBN, **downloadable cover images**.
- **Suggested interview questions (7–10) with sample answers** — lowers the friction for a host
  to book you.
- **Endorsements / blurbs** and **past coverage** (links to prior interviews/articles as
  samples).
- **Social links.**

---

## 10. Essays / writing / blog

Particularly relevant to you, since you write essays:

- A regularly updated **essays/writing section** feeds SEO, demonstrates the thinking behind the
  books, and gives the newsletter something to point at.
- Keep web copy **skimmable** — short paragraphs, clear subheads. (This is web-reading advice,
  not a constraint on the prose itself; the long-form essays can live as their own reading
  pages.)
- Each essay is a potential **reader-magnet on-ramp** and a shareable spoke that drives back to
  the hub.

---

## 11. Contact

- A **form** (name, email, subject, message) rather than a raw mailbox, to limit spam.
- Distinguish **reader** contact from **media/business** contact if volume warrants.
- Keep it genuinely simple — over-built contact pages suppress messages.

---

## 12. Design and typography — the literary / serious register

This is where your work's character should drive the choices, and the sources happen to point
the same way:

- **Serif typography signals "serious writer."** Reported web-friendly literary serifs: Freight
  Text, Crimson (Text/Pro), **Lora**, **Spectral**, **Source Serif**, **Merriweather**.
- **Two fonts maximum** — one for headings, one for body. (A serif/serif or serif-body +
  restrained-sans-heading pairing both work.)
- **Restraint and white space.** "Crisp typography and restrained elegance"; "let the covers
  provide the color." Minimalism dominates the 2026 examples.
- **Gravitas over flash** — formal headshot, strong About, logical hierarchy from book →
  thought leadership. This matches a witness/serious-nonfiction posture.

---

## 13. Navigation and UX

- **4–5 main nav items.** A clear, shallow hierarchy.
- **One primary action per page.** Decide what each page is *for* and make that action obvious.
- **Consistent header/footer** with the persistent newsletter CTA and social links.
- **Search** once the catalog justifies it.

---

## 14. Mobile and responsive

- **Mobile-first is non-negotiable** — sources report 60%+ of author-site traffic is mobile.
- **Tap-friendly targets, legible type, strong contrast**, no horizontal scroll, fast on
  cellular.
- Verify structured data and content parity on the mobile template, not just desktop.

---

## 15. Performance — Core Web Vitals **[STD: Google]**

Google's thresholds (primary source-class):

- **LCP (Largest Contentful Paint) ≤ 2.5 s** — loading.
- **INP (Interaction to Next Paint) ≤ 200 ms** — responsiveness.
- **CLS (Cumulative Layout Shift) ≤ 0.1** — visual stability.

Practices: optimize/compress images, use modern formats (**WebP/AVIF**), minify CSS/JS,
leverage caching, lazy-load below-the-fold media. A static site (see design spec) hits these
targets almost by default.

---

## 16. SEO and structured data

- **E-E-A-T**: a real, specific author bio and expert content measurably help rankings; this is
  the SEO payoff of doing §4 well.
- **Structured data / schema** must **match visible content** — `Person`/`Author`, `Book`,
  `Article` schema; never mark up hidden content, fake FAQs, or fake ratings.
- **Own your name**: `FirstNameLastName.com` is the standard — the one thing readers know is
  your name (§18).
- Standard hygiene: descriptive titles/meta, clean URLs, sitemap, alt text (also accessibility),
  internal links among books/essays.

---

## 17. Accessibility — WCAG **[STD: W3C]**

- **Contrast (WCAG 2.2 AA):** ≥ **4.5:1** normal text, **3:1** large text. AAA: 7:1 / 4.5:1.
- **Resizable text** to 200% without breaking layout.
- **Line spacing** ≥ 1.5× font size; paragraph spacing ≥ 2× (AAA guidance) — also simply good
  for literary reading.
- **Accessible typefaces**: adequate x-height, distinguishable letterforms, sufficient weight
  range; hierarchy not conveyed by color alone.
- Alt text on images, semantic headings, keyboard navigability, visible focus states.
- *(Horizon: WCAG 3.0 is still a working draft in 2026; APCA contrast — perceptual, size/weight
  weighted — is coming but not yet required. Build to 2.2 AA now.)*

---

## 18. Domain and branding

- **`KennethGranberry.com`** — `FirstLast.com` is the industry standard and the credibility
  default. Secure it (and reasonable variants) regardless of platform.
- Consistent name, headshot, and color/type system across the site, book jackets, and social —
  one recognizable identity.

---

## 19. Maintenance, analytics, trust

- **Keep it current** — the most-cited slow-rot mistake is launching and abandoning; an
  out-of-date site (missing the newest book) reads as neglect.
- **Proofread ruthlessly** — for a writer, a typo on the site undercuts the product itself.
- **Analytics** (privacy-respecting, e.g., Plausible/Fathom, or GA4) to see what converts.
- **No free-tier sites with injected ads** — they read as amateur.

---

## 20. Common mistakes to avoid (consolidated)

1. Homepage that talks only about the author ("Dear Reader" welcome letters).
2. No clear call-to-action / too many competing CTAs.
3. Too many navigation items (keep to 4–5).
4. Not mobile-friendly.
5. Autoplay audio/video.
6. Out-of-date site (missing current books/news).
7. Typos and sloppy copy.
8. Burying or omitting the email sign-up.
9. Too many retailer links → decision fatigue.
10. Free/ad-laden hosting that looks unprofessional.

---

## 21. Publishing-house practices worth borrowing

Even as a single author with multiple series, the house-side patterns help a multi-book catalog:

- **Systematic color/typography per series** to differentiate groups of titles.
- **Clear catalog structure** with reading order and entry points.
- **Search/filter and clickable theme tags** as the catalog grows.
- **A CMS/workflow** that lets you add a new title or essay without a redesign — argues for a
  content structure planned now, before there are eleven+ titles.

---

## 22. Sources

Author-website fundamentals & examples:
- [Sitebuilder Report — Author Websites (2026)](https://www.sitebuilderreport.com/inspiration/author-websites)
- [Jane Friedman — How to Build an Author Website](https://janefriedman.com/author-websites/)
- [Jane Friedman — Set Up the Perfect Online Press Kit](https://janefriedman.com/set-up-the-perfect-online-press-kit/)
- [BookBub — Author Websites Missing Crucial Elements](https://insights.bookbub.com/author-websites-missing-crucial-elements/)
- [IngramSpark — What Should I Put on My Author Website](https://www.ingramspark.com/blog/what-should-i-put-on-my-author-website)
- [IngramSpark — 6 Mistakes Authors Make with Their Websites](https://www.ingramspark.com/blog/6-mistakes-authors-make-with-their-websites)
- [314designs — Essential Pages Every Author Website Needs](https://314designs.net/author-website-pages)
- [Jin & Co. — Essential Pages & Features](https://jinand.co/articles/essential-pages-features-author-website-should-have)
- [Jin & Co. — Nonfiction Author Website Best Practices](https://jinand.co/articles/nonfiction-author-website/)
- [Charlotte Duckworth Studio — About & Contact Pages](https://www.charlotteduckworthstudio.com/blog/author-website-about-page)
- [Charlotte Duckworth Studio — Top 5 Mistakes](https://www.charlotteduckworthstudio.com/blog/top-5-mistakes-author-websites-make)
- [Brilliant Author — Hidden Pages](https://brilliantauthor.com/articles/author-website-hidden-pages)
- [Foglio — Professional Author Website Guide](https://www.foglioprint.com/blog/professional-author-website-guide)
- [Author Media — 10 Common Homepage Mistakes](https://www.authormedia.com/103/)
- [Anne R. Allen — 10 Website Mistakes New Authors Make](https://annerallen.com/2023/01/10-website-mistakes-new-authors-make/)
- [Rocket Expansion — 39 Nonfiction Author Websites](https://rocketexpansion.com/nonfiction-author-websites/)
- [Dorik — Author Website Examples](https://dorik.com/blog/author-website-examples)

Hero / homepage / landing pages:
- [Prismic — Hero Section Best Practices](https://prismic.io/blog/website-hero-section)
- [DreamHost — Homepage Hero Design](https://www.dreamhost.com/blog/homepage-hero-design/)
- [LogRocket — Hero Section Examples](https://blog.logrocket.com/ux-design/hero-section-examples-best-practices/)
- [Sumy Designs — Book Landing Page](https://www.sumydesigns.com/create-a-book-landing-page-authors/)
- [Kit — Book Landing Page Examples](https://kit.com/resources/blog/book-landing-page)
- [Thrive Themes — Book Landing Pages & Funnels](https://thrivethemes.com/book-landing-pages/)

Bio / About / E-E-A-T:
- [Kindlepreneur — Write an Author Bio](https://kindlepreneur.com/write-author-bio/)
- [Reedsy — Killer Author Bio](https://reedsy.com/studio/resources/author-bio)
- [Search Engine Journal — Author Bios, E-A-T & SEO](https://www.searchenginejournal.com/how-to-write-author-bios/417619/)
- [Selfpublishing.com — About the Author](https://selfpublishing.com/about-the-author/)

Email / reader magnets:
- [Kit — Lead Magnets for Authors](https://kit.com/resources/blog/lead-magnets-for-authors)
- [Author Media — Delicious Reader Magnets](https://www.authormedia.com/delicious-reader-magnets/)
- [Brilliant Author — 33 Reader Magnet Ideas](https://brilliantauthor.com/articles/reader-magnet-ideas)
- [Sudowrite — Email Marketing for Authors](https://sudowrite.com/blog/email-marketing-for-authors-the-ultimate-guide-to-building-a-newsletter/)

Direct vs. retailer sales:
- [Written Word Media — Direct Sales Bookstore](https://www.writtenwordmedia.com/adding-direct-sales-to-your-author-website/)
- [BookBaby — Amazon vs Direct-to-Reader](https://blog.bookbaby.com/how-to-self-publish/book-distribution/amazon-vs-direct-to-reader-book-sales)
- [Kindlepreneur — Selling Books Direct (500+ authors)](https://kindlepreneur.com/the-truth-on-selling-books-direct-insights-from-authors/)
- [Self-Publishing Advice — Selling Books on Your Website](https://selfpublishingadvice.org/selling-books-on-your-author-website/)

Press / media kit:
- [Reedsy — Author Media Kit Template](https://reedsy.com/blog/author-media-kit-template/)
- [Author Media — Online Author Press Kit](https://www.authormedia.com/how-to-create-an-online-author-press-kit/)
- [Greenleaf — What to Include in Your Press Kit](https://greenleafbookgroup.com/learning-center/book-marketing/what-to-include-in-your-author-press-kit-and-why-you-should-have-one)

Design / typography:
- [Chapter — Author Website Design Guide 2026](https://blog.chapter.pub/author-website-design/)
- [Lynn's Author Studio — Typography Trends 2026](https://www.lynnsauthorstudio.com/blog/author-typography-trends-2026)
- [LetterSiro — Fonts for Serious Nonfiction](https://lettersiro.com/best-publication-font-to-use-for-serious-nonfiction/)

Publishing-house sites:
- [Fireart — Best Publishing Website Examples](https://fireart.studio/blog/13-great-publishing-website-examples/)
- [Founderjar — Best Publisher Websites](https://www.founderjar.com/inspiration/publisher-websites-examples/)
- [Colorlib — Publishers Websites](https://colorlib.com/wp/publishers-websites/)
- [Spines — What Is an Imprint](https://spines.com/what-is-an-imprint-in-publishing/)

Performance / SEO / accessibility (standards-class marked in text):
- [Google Core Web Vitals via Gracker — Optimization Guide](https://gracker.ai/seo-101/core-web-vitals-optimization-technical-seo-guide)
- [DebugBear — Page Speed and SEO](https://www.debugbear.com/docs/page-speed-seo)
- [Editorialge — Mobile SEO Best Practices 2026](https://editorialge.com/mobile-seo-best-practices/)
- [W3C — WCAG 2.1](https://www.w3.org/TR/WCAG21/)
- [Section508.gov — Fonts & Typography](https://www.section508.gov/develop/fonts-typography/)
- [WebAIM — Typefaces and Fonts](https://webaim.org/techniques/fonts/)
- [Web Accessibility Checker — WCAG 3.0 Guide 2026](https://web-accessibility-checker.com/en/blog/wcag-3-0-guide-2026-changes-prepare)
