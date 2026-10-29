#!/usr/bin/env python3
"""Easiest way to run RetentionGuard locally.

No dependencies, no install, no server required by default:
it just opens index.html in your default browser.

Usage:
    python3 run.py            # open index.html in your browser
    python3 run.py --serve    # also serve it at http://localhost:8000
"""
import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX = HERE / "index.html"


def main() -> int:
    if not INDEX.exists():
        print(f"index.html not found in {HERE}")
        return 1
    if "--serve" in sys.argv:
        port = 8000
        print(f"Serving RetentionGuard at http://localhost:{port} (Ctrl+C to stop)")
        webbrowser.open(f"http://localhost:{port}/index.html")
        with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
            httpd.serve_forever()
        return 0
    print("Opening RetentionGuard in your browser (no install needed).")
    webbrowser.open(INDEX.as_uri())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
