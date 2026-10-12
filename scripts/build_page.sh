#!/usr/bin/env bash
# Build an industry page: assemble chrome, then inject the FAQPage schema.
#
#   scripts/build_page.sh <slug> [out.html]
#
# Default output is pages/<slug>.html; an explicit second argument writes
# somewhere else (used to diff a rebuild against the published page).
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "usage: build_page.sh <slug> [out.html]" >&2
  exit 1
fi

slug="$1"
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$repo/sources/$slug.html"
out="${2:-$repo/pages/$slug.html}"

if [ ! -f "$src" ]; then
  echo "error: no source at $src" >&2
  exit 1
fi

python3 "$repo/scripts/assemble_page.py" "$src" "$out"

schema="$(mktemp)"
trap 'rm -f "$schema"' EXIT
python3 "$repo/scripts/build_faq_schema.py" "$out" > "$schema"

OUT="$out" SCHEMA="$schema" python3 - <<'PYEOF'
import os, sys

out = os.environ["OUT"]
with open(os.environ["SCHEMA"], encoding="utf-8", newline="") as fh:
    block = fh.read()
if block.endswith("\n"):
    block = block[:-1]

with open(out, encoding="utf-8", newline="") as fh:
    page = fh.read()

marker = "<!--FAQ_SCHEMA-->"
if marker not in page:
    sys.exit("error: %s has no %s marker" % (out, marker))

page = page.replace(marker, block, 1)
with open(out, "w", encoding="utf-8", newline="") as fh:
    fh.write(page)
PYEOF

echo "injected FAQPage schema into $out"
