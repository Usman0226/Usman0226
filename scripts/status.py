#!/usr/bin/env python3
"""Check the live sites and redraw assets/status.svg as a Notion-style table.
Run by a GitHub Action every few hours.
Usage: python scripts/status.py [--offline]   (--offline draws the 'not checked yet' state)
"""
import os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse
from typeset import Text

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

W, HEADH, ROWH = 880, 34, 46
T = Text()
ist = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
stamp = "Not checked yet" if offline else "Checked " + ist.strftime("%d %b %Y, %H:%M") + " IST, refreshed every six hours"
COLS = (0, 230, 420, 740)
els = [T.put(h, 400, 13, x, 22, "mut") for h, x in zip(("Name", "Status", "Address", "Response"), COLS)]
els.append(f'<line class="rule" x1="0" x2="{W}" y1="{HEADH}" y2="{HEADH}"/>')
n = len(SITES)
for i, (name, url) in enumerate(SITES):
    y = HEADH + i * ROWH
    a, b = i / n, (i + 1) / n
    kt = f"0;{max(a, 0.001):.3f};{a+0.03:.3f};{b-0.03:.3f};{b:.3f};1"
    els.append(f'<rect class="hov" x="-8" y="{y+3}" width="{W+16}" height="{ROWH-6}" rx="6" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt}" dur="12s" begin="1s" repeatCount="indefinite"/></rect>')
    code, ms = (None, None) if offline else check(url)
    host = urlparse(url).netloc.removeprefix("www.")
    if offline: kind, label = "cn", "Not checked yet"
    elif code is not None and code < 400: kind, label = "cg", "Live"
    else: kind, label = "cr", "Down" if code is None else f"Down, HTTP {code}"
    tw = T.width(label, 400, 13.5) + 18 + (14 if kind == "cg" else 0)
    cy = y + 12
    els.append(f'<rect class="{kind}" x="{COLS[1]}" y="{cy}" width="{tw:.1f}" height="22" rx="4"/>')
    tx = COLS[1] + 9
    if kind == "cg":
        els.append(f'<circle class="up" cx="{tx+3.5}" cy="{cy+11}" r="3.2"/><circle class="ring" cx="{tx+3.5}" cy="{cy+11}" r="3.2">'
                   f'<animate attributeName="r" values="3.2;9;9" keyTimes="0;0.8;1" dur="3.2s" begin="{i*0.5}s" repeatCount="indefinite"/>'
                   f'<animate attributeName="opacity" values="0.55;0;0" keyTimes="0;0.8;1" dur="3.2s" begin="{i*0.5}s" repeatCount="indefinite"/></circle>')
        tx += 14
    els.append(T.put(label, 400, 13.5, tx, cy + 15.5, "ink"))
    els.append(T.put(name, 600, 15, COLS[0], y + 29, "ink"))
    els.append(T.put(host, 400, 14.5, COLS[2], y + 29, "mut"))
    els.append(T.put("-" if ms is None else f"{ms} ms", 400, 14.5, COLS[3], y + 29, "mut"))
    els.append(f'<line class="rule" x1="0" x2="{W}" y1="{y+ROWH}" y2="{y+ROWH}"/>')
H = HEADH + n * ROWH + 30
els.append(T.put(stamp, 400, 12.5, 0, H - 8, "mut"))
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 0 {W+16} {H}" width="{W+16}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Live status of three deployed systems. {stamp}.</title>
<style>
.ink{{fill:#37352f}}.mut{{fill:#787774}}.rule{{stroke:#e9e9e7;stroke-width:1}}.hov{{fill:#f1f1ef}}
.cg{{fill:#dbeddb}}.cr{{fill:#ffe2dd}}.cn{{fill:#e9e9e7}}.up{{fill:#1a9d5a}}.ring{{fill:none;stroke:#1a9d5a;stroke-width:1}}
@media (prefers-color-scheme:dark){{.ink{{fill:#e6e5e3}}.mut{{fill:#9b9a97}}.rule{{stroke:#373737}}.hov{{fill:#262626}}
.cg{{fill:#1f3a2c}}.cr{{fill:#5d2a27}}.cn{{fill:#373737}}.up{{fill:#3fb97a}}.ring{{stroke:#3fb97a}}}}
</style>
{T.defs()}
{chr(10).join(els)}
</svg>
"""
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "status.svg"), "w", encoding="utf-8").write(svg)
print("status.svg written:", stamp)
