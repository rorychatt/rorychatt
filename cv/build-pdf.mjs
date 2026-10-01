// Renders cv/index.html to cv/Mikael-Rinne-CV.pdf with a local Chromium-based browser.
//
//   vp node cv/build-pdf.mjs        (or: node cv/build-pdf.mjs)
//
// Set CHROME_PATH to use a specific browser binary.
import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = pathToFileURL(resolve(here, "index.html")).href;
const out = resolve(here, "Mikael-Rinne-CV.pdf");

const candidates = [
  process.env.CHROME_PATH,
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
  "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
  "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/usr/bin/google-chrome",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser",
].filter(Boolean);

const browser = candidates.find((p) => existsSync(p));
if (!browser) {
  console.error("No Chromium-based browser found. Set CHROME_PATH to a Chrome, Edge or Chromium binary.");
  process.exit(1);
}

const args = ["--headless", "--disable-gpu", "--no-pdf-header-footer", `--print-to-pdf=${out}`, src];
// Hosted CI runners restrict the sandbox's user namespaces; the page is our own static HTML.
if (process.env.CI) args.unshift("--no-sandbox");

execFileSync(browser, args, { stdio: "inherit" });
console.log(`wrote ${out}`);
