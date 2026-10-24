#!/usr/bin/env python3
"""Check the live sites and redraw assets/status.svg as a monochrome index table.
Run by a GitHub Action every few hours.
Usage: python scripts/status.py [--offline]   (--offline draws the 'not checked yet' state)
"""
import os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse
from typeset import Text

CSS = """<style>
.ink{fill:#161616}.mut{fill:#6e6e6e}.faint{fill:#b6b6b6}.rule{stroke:#e2e2e2;stroke-width:1}.hov{fill:#f4f4f4}
.outline{fill:none;stroke:#c7c7c7;stroke-width:1}.up{fill:#1a9d5a}.ring{fill:none;stroke:#1a9d5a;stroke-width:1}.down{fill:#c0392b}
@media (prefers-color-scheme:dark){
.ink{fill:#f0f0f0}.mut{fill:#9a9a9a}.faint{fill:#4d4d4d}.rule{stroke:#2b2b2b}.hov{fill:#1e1e1e}
.outline{stroke:#3a3a3a}.up{fill:#3fb97a}.ring{stroke:#3fb97a}.down{fill:#e0574a}}
</style>"""

SITES = [("NoDues", "https://www.nodues-arcclub.tech/"),
         ("D\u2019FESTA 2K26", "https://dfesta.in"),
         ("NCC Exam Portal", "https://ncc-exam-portal.vercel.app/")]
offline = "--offline" in sys.argv

def check(url):
    t = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "profile-status-check"})
        with urllib.request.urlopen(req, timeout=20) as r: code = r.status
    except urllib.error.HTTPError as e: code = e.code
    except Exception: return None, None
    return code, int((time.time() - t) * 1000)

W, HEADH, ROWH = 880, 30, 42
T = Text()
ist = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
stamp = "Not checked yet" if offline else "Checked " + ist.strftime("%d %b, %H:%M") + " IST, every six hours"
COLS = (0, 430, 700)
els = [T.put(h, "sans400", 12.5, x, 18, "faint") for h, x in zip(("Name", "Status", "Response"), COLS)]
els.append(f'<line class="rule" x1="0" x2="{W}" y1="{HEADH}" y2="{HEADH}"/>')
n = len(SITES)
for i, (name, url) in enumerate(SITES):
    y = HEADH + i * ROWH
    a, b = i / n, (i + 1) / n
    kt = f"0;{max(a,0.001):.3f};{a+0.03:.3f};{b-0.03:.3f};{b:.3f};1"
    els.append(f'<rect class="hov" x="-10" y="{y+2}" width="900" height="{ROWH-4}" rx="4" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt}" dur="10s" begin="1s" repeatCount="indefinite"/></rect>')
    code, ms = (None, None) if offline else check(url)
    cy = y + ROWH / 2
    if offline: dot, label, lcls = "outline", "Not checked yet", "mut"
    elif code is not None and code < 400: dot, label, lcls = "up", "Live", "ink"
    else: dot, label, lcls = "down", ("Down" if code is None else f"HTTP {code}"), "ink"
    els.append(T.put(name, "sans600", 16, COLS[0], cy + 5, "ink"))
    if dot == "up":
        els.append(f'<circle class="up" cx="{COLS[1]+3.5}" cy="{cy}" r="3.2"/><circle class="ring" cx="{COLS[1]+3.5}" cy="{cy}" r="3.2">'
                   f'<animate attributeName="r" values="3.2;9;9" keyTimes="0;0.8;1" dur="3.2s" begin="{i*0.5}s" repeatCount="indefinite"/>'
                   f'<animate attributeName="opacity" values="0.5;0;0" keyTimes="0;0.8;1" dur="3.2s" begin="{i*0.5}s" repeatCount="indefinite"/></circle>')
    else:
        els.append(f'<circle class="{dot}" cx="{COLS[1]+3.5}" cy="{cy}" r="3.2"/>')
    els.append(T.put(label, "sans400", 14, COLS[1] + 16, cy + 5, lcls))
    els.append(T.put("-" if ms is None else f"{ms} ms", "sans400", 14, COLS[2], cy + 5, "mut"))
    if i < n - 1: els.append(f'<line class="rule" x1="0" x2="{W}" y1="{y+ROWH}" y2="{y+ROWH}"/>')
H = HEADH + n * ROWH + 26
els.append(T.put(stamp, "sans400", 12, 0, H - 6, "faint"))
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Live status of three deployed systems. {stamp}.</title>
{CSS}{T.defs()}
{chr(10).join(els)}
</svg>
"""
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "status.svg"), "w", encoding="utf-8").write(svg)
print("status.svg written:", stamp)
