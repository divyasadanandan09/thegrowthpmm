#!/usr/bin/env node
/**
 * Keeps the Growth Audit email copy identical to the page copy.
 *
 * The page imports src/content/audit-copy.json directly. Apps Script cannot
 * import anything, so this injects the same JSON into GOOGLE_APPS_SCRIPT.gs
 * between two markers.
 *
 *   npm run sync:audit-copy    rewrite the .gs block from the JSON
 *   npm run check:audit-copy   fail if the .gs block is out of date
 *
 * Emitting via JSON.stringify also means copy can contain apostrophes safely.
 * A hand-written apostrophe inside a single-quoted string is what made an
 * earlier version of the .gs fail to parse at all.
 */
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const JSON_PATH = join(root, "src/content/audit-copy.json");
const GS_PATH = join(root, "GOOGLE_APPS_SCRIPT.gs");

const START = "// <<< GENERATED FROM src/content/audit-copy.json — do not edit by hand";
const END = "// >>> END GENERATED";

const copy = JSON.parse(readFileSync(JSON_PATH, "utf8"));

const block = [
  START,
  `var VERDICTS = ${JSON.stringify(copy.verdicts, null, 2)};`,
  "",
  `var DIAGNOSIS = ${JSON.stringify(copy.stages, null, 2)};`,
  "",
  `var FREE_MAIL = ${JSON.stringify(copy.freeMailDomains)};`,
  END,
].join("\n");

const gs = readFileSync(GS_PATH, "utf8");
const startAt = gs.indexOf(START);
const endAt = gs.indexOf(END);

if (startAt === -1 || endAt === -1) {
  console.error(`Markers missing in ${GS_PATH}. Expected:\n  ${START}\n  ${END}`);
  process.exit(1);
}

const next = gs.slice(0, startAt) + block + gs.slice(endAt + END.length);
const checkOnly = process.argv.includes("--check");

if (next === gs) {
  console.log("audit copy: page and email are in sync");
  process.exit(0);
}

if (checkOnly) {
  console.error(
    "audit copy: GOOGLE_APPS_SCRIPT.gs is out of date with src/content/audit-copy.json.\n" +
      "The page and the emailed audit would disagree. Run: npm run sync:audit-copy"
  );
  process.exit(1);
}

writeFileSync(GS_PATH, next);
console.log("audit copy: GOOGLE_APPS_SCRIPT.gs updated. Re-paste it into Apps Script and deploy a new version.");
