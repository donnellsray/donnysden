// usage: node snap.mjs <name> <url> <width> [--full]  (visitor view)
import { createRequire } from "node:module";
const require = createRequire("/opt/node22/lib/node_modules/"); const { chromium } = require("playwright");
const S = ".";
const [name, url, w] = process.argv.slice(2); const full = process.argv.includes("--full");
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium", proxy: { server: process.env.HTTPS_PROXY } });
const p = await (await b.newContext({ viewport: { width: +w, height: +w <= 430 ? 844 : 900 } })).newPage();
const errs = []; p.on("pageerror", e => errs.push(e.message)); p.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
await p.goto(url, { waitUntil: "networkidle" }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1200);
const info = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, h: document.documentElement.scrollHeight, fonts: [...new Set([...document.fonts].filter(f => f.status === "loaded").map(f => f.family))].join(",") }));
console.log(name, w, JSON.stringify(info), errs);
await p.screenshot({ path: `${S}/shots/${name}-${w}.png`, fullPage: full }); await b.close();
