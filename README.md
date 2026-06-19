# KennethGranberry.com

The literary author hub for Kenneth Granberry — formation, the examined life,
and the defense of what makes us human. Built with [Eleventy](https://www.11ty.dev/)
as a static site: one shared layout, navigation defined once, and the design
tokens in a single stylesheet.

## Develop

```bash
npm install      # once
npm run serve    # local dev server with live reload
npm run build    # output static site to ./_site
```

## Structure

```
src/
  _data/site.js              site-wide data (title, motto, canonical nav)
  _includes/
    base.njk                 the one HTML shell every page extends
    partials/masthead.njk    canonical masthead (nav defined once)
    partials/footer.njk      canonical footer (motto + nav)
  assets/
    css/site.css             design tokens, base type, masthead, footer,
                             reveal animation, shared interior-page styles
    js/site.js               masthead-on-scroll, reveal-on-scroll, form stub
  index.njk                  Home (night → dawn hub)
  lighthouse.njk             The Lighthouse (newsletter front door)
  writing.njk                Writing index
  books.njk                  Books
  prompts/index.njk          Prompts index (the seven Socratic sequences)
  prompts/the-contradiction.njk   the level-two prompt (template for the rest)
  about.njk                  About  (see TODO)
  credo.njk                  The Credo (the vow in four motions)
```

Design language and copy are taken verbatim from the approved reference pages —
construction only, no redesign or rewrite. Tokens: Cormorant Garamond / EB
Garamond; night-to-dawn palette with the gold star motif. No localStorage or
sessionStorage anywhere (in-memory JS only).

## Open TODOs

- **Email forms are stubbed.** Every capture (home, Lighthouse, the Contradiction)
  shows a thank-you and captures nothing. Wire to the chosen provider
  (Kit / Beehiiv / Substack). See the `data-capture` stub in `src/assets/js/site.js`
  and the comment on the Contradiction form.
- **About is a stopgap.** `src/about.njk` is assembled from the home teaser and
  the approved house bio — no new prose invented. Replace with the final
  `kenneth-granberry-about.html` when available.
- **Books buy-links are placeholders** ("Buy links to come"); the books are
  forthcoming.
- **The AI Entrepreneur's Blueprint** has a marked placeholder in `src/books.njk`
  to slot in later as an additional title.

## Deploy

The build is host-agnostic static output in `_site/`. For Netlify: build
command `npm run build`, publish directory `_site`. For GitHub Pages: build in
CI and publish `_site`.
