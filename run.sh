#!/bin/sh
# RetentionGuard: double-click / run this, no install needed.
# Opens index.html in your default browser.
cd "$(dirname "$0")" || exit 1
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open index.html
elif command -v open >/dev/null 2>&1; then
  open index.html
elif command -v python3 >/dev/null 2>&1; then
  python3 run.py
else
  echo "Open index.html in your browser."
fi
