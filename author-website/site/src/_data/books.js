// The catalogue, as data. Adding a title later is an entry in `titles` — no redesign.
// status: "available" | "preorder" | "forthcoming"
// Covers/buy links/excerpts are placeholders until assets exist (spec §9.11).

const trilogy = {
  title: "Formation in the Age of AI",
  note: "A trilogy. Working series title.",
  readingOrder: [
    "the-center-that-cannot-be-empty",
    "what-the-mirror-cannot-see",
    "the-mirrored-mind",
  ],
  publicationOrder: [
    "the-mirrored-mind",
    "what-the-mirror-cannot-see",
    "the-center-that-cannot-be-empty",
  ],
};

const titles = {
  // ── The Trilogy ──────────────────────────────────────────────────────────
  "the-mirrored-mind": {
    title: "The Mirrored Mind",
    subtitle: "A Modern Prophecy, and the Road to Redemption",
    group: "trilogy",
    flagship: true,
    status: "forthcoming",
    hook: "The flagship of the trilogy: a civilizational road to redemption, and an individual one.",
  },
  "what-the-mirror-cannot-see": {
    title: "What the Mirror Cannot See",
    group: "trilogy",
    status: "forthcoming",
    hook: "Book two of the trilogy.",
  },
  "the-center-that-cannot-be-empty": {
    title: "The Center That Cannot Be Empty",
    group: "trilogy",
    status: "forthcoming",
    hook: "Book one of the trilogy: the binding center, and what is lost when it empties.",
  },

  // ── The Entrepreneur's Blueprint ───────────────────────────────────────────
  "the-entrepreneurs-blueprint": {
    title: "The Entrepreneur's Blueprint",
    group: "blueprint",
    status: "forthcoming",
    hook: "A five-volume collection.",
    isCollection: true,
    volumeCount: 5,
  },

  // ── Standalones ───────────────────────────────────────────────────────────
  "the-wise-life": {
    title: "The Wise Life",
    subtitle: "How to Envision, Live, and Die Wisely",
    group: "standalone",
    status: "forthcoming",
    hook: "A witness to the literature on what wisdom is and how to live and die well.",
  },
  "the-jinn-has-left-the-bottle": {
    title: "The Jinn Has Left the Bottle",
    group: "standalone",
    status: "forthcoming",
    hook: "",
  },
  "the-law-written-twice": {
    title: "The Law Written Twice",
    group: "standalone",
    status: "forthcoming",
    hook: "",
  },
  "the-morning-star": {
    title: "The Morning Star",
    group: "standalone",
    status: "forthcoming",
    hook: "",
  },
  "the-performance-gap": {
    title: "The Performance Gap",
    group: "standalone",
    status: "forthcoming",
    hook: "",
  },

  // ── The Novel ─────────────────────────────────────────────────────────────
  "eli": {
    title: "ELI",
    group: "novel",
    status: "forthcoming",
    hook: "A novel.",
  },
};

export default {
  trilogy,
  titles,
  // Iterable form for pagination / grouping (insertion order preserved).
  all: Object.entries(titles).map(([slug, data]) => ({ slug, ...data })),
};
