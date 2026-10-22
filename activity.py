#!/usr/bin/env python3
"""Redraw assets/activity.svg: one fine line per week of public contributions, last 12 months.
No token or third-party service: reads the public calendar GitHub shows on your profile.
Usage: python scripts/activity.py [username]
"""
import os, re, sys, urllib.request
from collections import OrderedDict
from datetime import date
from typeset import Text

user = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_REPOSITORY_OWNER", "Usman0226")
req = urllib.request.Request(f"https://github.com/users/{user}/contributions", headers={"User-Agent": "profile-activity-script"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
days, counts = {}, {}
for m in re.finditer(r'data-date="([\d-]+)"\s+id="(contribution-day-component-\d+-\d+)"', html): days[m.group(2)] = m.group(1)
for m in re.finditer(r'for="(contribution-day-component-\d+-\d+)"[^>]*>\s*(No|\d+) contributions?', html):
    counts[m.group(1)] = 0 if m.group(2) == "No" else int(m.group(2))
if not days: sys.exit("Could not read the contribution calendar; leaving the existing SVG untouched.")
weeks = OrderedDict()
for cid, iso in days.items():
    w = weeks.setdefault(int(cid.rsplit("-", 1)[1]), [0, iso]); w[0] += counts.get(cid, 0); w[1] = min(w[1], iso)
weeks = [weeks[k] for k in sorted(weeks)]
total, peak, n = sum(w[0] for w in weeks), max(w[0] for w in weeks) or 1, len(weeks)

W, H, BASE, MAXH = 880, 86, 56, 46
T = Text(); step, bw = W / n, 2.4
bars, labels, last = [], [], None
for i, (tot, iso) in enumerate(weeks):
    x = i * step + step / 2 - bw / 2
    h = max(3.0, MAXH * tot / peak) if tot else 3.0
    cls = "zero" if not tot else ("now" if i == n - 1 else "bar")
    d = (i / n) * 0.62
    pulse = '<animate attributeName="opacity" values="1;0.35;1" dur="3.2s" begin="2.6s" repeatCount="indefinite"/>' if cls == "now" else ""
    bars.append(f'<rect class="{cls}" x="{x:.1f}" y="{BASE-h:.1f}" width="{bw}" height="{h:.1f}" rx="1.2"><animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{d:.3f};{d+0.04:.3f};1" dur="2.8s" begin="0s" fill="freeze"/>{pulse}</rect>')
    dt = date.fromisoformat(iso)
    if dt.month != last and dt.day <= 14 and i < n - 2: labels.append(T.put(dt.strftime("%b"), 400, 12, i * step, 79, "lbl"))
    if dt.day <= 14: last = dt.month
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">{total} public contributions in the last year, one line per week</title>
<style>
.bar{{fill:#667085}}.zero{{fill:#e4e7ec}}.now{{fill:#1a9d5a}}.lbl{{fill:#667085}}.rule{{stroke:#e4e7ec;stroke-width:1}}
@media (prefers-color-scheme:dark){{.bar{{fill:#98a2b3}}.zero{{fill:#2b3038}}.now{{fill:#3fb97a}}.lbl{{fill:#98a2b3}}.rule{{stroke:#2b3038}}}}
</style>
{T.defs()}
<line class="rule" x1="0" x2="{W}" y1="62" y2="62"/>
{chr(10).join(bars)}
{chr(10).join(labels)}
</svg>
"""
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "activity.svg"), "w", encoding="utf-8").write(svg)
print(f"{user}: {total} contributions, peak week {peak}, {n} weeks -> assets/activity.svg")
