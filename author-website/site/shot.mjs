import { chromium } from "playwright";

const url = "http://127.0.0.1:8099/";
const browser = await chromium.launch();

// Desktop, full page
const d = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 2 });
await d.goto(url, { waitUntil: "networkidle" });
await d.waitForTimeout(600);
await d.screenshot({ path: "/tmp/home-desktop.png", fullPage: true });

// Mobile, full page
const m = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
await m.goto(url, { waitUntil: "networkidle" });
await m.waitForTimeout(600);
await m.screenshot({ path: "/tmp/home-mobile.png", fullPage: true });

await browser.close();
console.log("done");
