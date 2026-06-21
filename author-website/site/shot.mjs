import { chromium } from "playwright";

const base = "http://127.0.0.1:8099";
const shots = [
  { url: "/", out: "/tmp/home-desktop.png", w: 1280 },
  { url: "/books/", out: "/tmp/books-index.png", w: 1280 },
  { url: "/books/the-mirrored-mind/", out: "/tmp/book-flagship.png", w: 1280 },
];

const browser = await chromium.launch();
for (const s of shots) {
  const p = await browser.newPage({ viewport: { width: s.w, height: 900 }, deviceScaleFactor: 2 });
  await p.goto(base + s.url, { waitUntil: "networkidle" });
  await p.waitForTimeout(500);
  await p.screenshot({ path: s.out, fullPage: true });
  await p.close();
}
await browser.close();
console.log("done");
