#!/usr/bin/env python3
"""Redraw assets/activity.svg: a headline contribution count plus a minimal gradient
sparkline of weekly public activity over the last 12 months. No token, no third-party
service: reads the public calendar GitHub shows on the profile page.
Usage: python scripts/activity.py [username]
"""
import os, re, sys, urllib.request, json
from collections import OrderedDict
from datetime import date
from typeset import Text

config_path = os.path.join(os.path.dirname(__file__), "profile_config.json")
config = {}
if os.path.exists(config_path):
    try:
        config = json.load(open(config_path, encoding="utf-8"))
    except Exception:
        pass

spark_light = config.get("activity", {}).get("color", {}).get("light", "#2383e2")
spark_dark = config.get("activity", {}).get("color", {}).get("dark", "#529cca")
fill_op = config.get("activity", {}).get("fill_opacity", "0.14")
cfg_user = config.get("activity", {}).get("username", "Usman0226")

CSS = f"""<style>
.ink{{fill:#161616}}.mut{{fill:#6e6e6e}}.faint{{fill:#b6b6b6}}.rule{{stroke:#e2e2e2;stroke-width:1}}
.spark{{fill:none;stroke:{spark_light};stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}.area{{fill:{spark_light}}}.now{{fill:{spark_light}}}.ring2{{fill:none;stroke:{spark_light};stroke-width:1.4}}
@media (prefers-color-scheme:dark){{
.ink{{fill:#f0f0f0}}.mut{{fill:#9a9a9a}}.faint{{fill:#4d4d4d}}.rule{{stroke:#2b2b2b}}
.spark{{stroke:{spark_dark}}}.area{{fill:{spark_dark}}}.now{{fill:{spark_dark}}}.ring2{{stroke:{spark_dark}}}}}
</style>"""

user = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_REPOSITORY_OWNER", cfg_user)
req = urllib.request.Request(f"https://github.com/users/{user}/contributions", headers={"User-Agent": "profile-activity-script"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

days, counts = {}, {}
for m in re.finditer(r'data-date="([\d-]+)"\s+id="(contribution-day-component-\d+-\d+)"', html):
    days[m.group(2)] = m.group(1)
for m in re.finditer(r'for="(contribution-day-component-\d+-\d+)"[^>]*>\s*(No|\d+) contributions?', html):
    counts[m.group(1)] = 0 if m.group(2) == "No" else int(m.group(2))
if not days:
    sys.exit("Could not read the contribution calendar; leaving the existing SVG untouched.")

weeks = OrderedDict()
for cid, iso in days.items():
    w = weeks.setdefault(int(cid.rsplit("-", 1)[1]), [0, iso])
    w[0] += counts.get(cid, 0); w[1] = min(w[1], iso)
weeks = [weeks[k] for k in sorted(weeks)]
total, peak, n = sum(w[0] for w in weeks), max(w[0] for w in weeks) or 1, len(weeks)
best_run = cur_run = run = 0
for w, _ in weeks:
    run = run + 1 if w else 0
    best_run = max(best_run, run)

W, H = 880, 170
T = Text()
GX, GY, GW, GH = 300, 36, 580, 88

pts = []
for i, (tot, _) in enumerate(weeks):
    x = GX + i * (GW / (n - 1))
    y = GY + GH - (GH * tot / peak if tot else 0)
    pts.append((x, y))
path_d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
area_d = path_d + f" L{pts[-1][0]:.1f} {GY+GH:.1f} L{pts[0][0]:.1f} {GY+GH:.1f} Z"
length = sum(((pts[i+1][0]-pts[i][0])**2 + (pts[i+1][1]-pts[i][1])**2) ** 0.5 for i in range(len(pts)-1))

els = [
    T.put(f"{total:,}", "sans600", 56, 0, 86, "ink", ls=-1),
    T.put("public contributions, last 12 months", "sans400", 14.5, 0, 112, "mut"),
    T.put(f"{best_run} wk", "sans600", 20, 0, 150, "ink"),
    T.put("longest active streak", "sans400", 12.5, 0, 168, "faint"),
    T.put(f"{peak}", "sans600", 20, 150, 150, "ink"),
    T.put("busiest week", "sans400", 12.5, 150, 168, "faint"),
    f'<line class="rule" x1="0" x2="{W}" y1="{GY+GH+28}" y2="{GY+GH+28}"/>',
    f'<clipPath id="reveal"><path d="{area_d}"/></clipPath>',
    f'<rect class="area" x="{GX}" y="{GY}" width="{GW}" height="{GH}" opacity="0" clip-path="url(#reveal)">'
    f'<animate attributeName="opacity" values="0;0;{fill_op}" keyTimes="0;0.05;0.3" dur="3s" begin="0.4s" fill="freeze"/></rect>',
    f'<path class="spark" pathLength="{length:.1f}" stroke-dasharray="{length:.1f}" d="{path_d}">'
    f'<animate attributeName="stroke-dashoffset" values="{length:.1f};{length:.1f};0" keyTimes="0;0.05;0.85" dur="3s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;0.25 0.1 0.25 1"/></path>',
    f'<circle class="now" cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="3.2">'
    f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;0.84;0.86" dur="3s" begin="0.2s" fill="freeze"/></circle>',
    f'<circle class="ring2" cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="3.2">'
    f'<animate attributeName="r" values="3.2;10;10" keyTimes="0;0.8;1" dur="3.2s" begin="3.4s" repeatCount="indefinite"/>'
    f'<animate attributeName="opacity" values="0.45;0;0" keyTimes="0;0.8;1" dur="3.2s" begin="3.4s" repeatCount="indefinite"/></circle>',
]
last_month = None
for i, (tot, iso) in enumerate(weeks):
    dt = date.fromisoformat(iso)
    if dt.month != last_month and dt.day <= 14 and i < n - 2:
        els.append(T.put(dt.strftime("%b"), "sans400", 12, GX + i * (GW / (n - 1)), GY + GH + 20, "faint"))
    if dt.day <= 14: last_month = dt.month

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">{total} public contributions in the last 12 months. Longest active streak {best_run} weeks. Busiest week {peak} contributions.</title>
{CSS}
{T.defs()}
{chr(10).join(els)}
</svg>
"""
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "activity.svg")
open(out, "w", encoding="utf-8").write(svg)
print(f"{user}: {total} contributions, peak {peak}, streak {best_run} -> assets/activity.svg")
