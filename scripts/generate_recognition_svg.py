#!/usr/bin/env python3
"""Generate assets/recognition.svg with outlined glyphs and clean 3-row layout.
Rows:
1. LifeLink Hackathon (Winner)
2. Onco-IQ Internship (NIT Pondicherry)
3. IIC Innovation Coordinator & ARC Club Student Coordinator (MITS Madanapalle)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from typeset import Text

T = Text()

CSS = """<style>
.ink{fill:#161616}.mut{fill:#6e6e6e}.faint{fill:#b6b6b6}.rule{stroke:#e2e2e2;stroke-width:1}
.line{fill:none;stroke:#161616;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}
.hov{fill:#f4f4f4}.outline{fill:none;stroke:#c7c7c7;stroke-width:1}
.up{fill:#1a9d5a}.ring{fill:none;stroke:#1a9d5a;stroke-width:1}.down{fill:#c0392b}
@media (prefers-color-scheme:dark){
.ink{fill:#f0f0f0}.mut{fill:#9a9a9a}.faint{fill:#4d4d4d}.rule{stroke:#2b2b2b}
.line{stroke:#f0f0f0}.hov{fill:#1e1e1e}.outline{stroke:#3a3a3a}
.up{fill:#3fb97a}.ring{stroke:#3fb97a}.down{fill:#e0574a}
}
</style>"""

r1_t = T.put("LifeLink Hackathon", "sans600", 16, 40, 26, "ink")
r1_pill = T.put("Winner", "sans400", 12.5, 49, 46, "mut")

r2_t = T.put("Onco-IQ Internship", "sans600", 16, 40, 82, "ink")
r2_sub = T.put("NIT Pondicherry", "sans400", 14.5, 40, 101, "mut")

r3_t = T.put("IIC Innovation Coordinator & ARC Club Student Coordinator", "sans600", 16, 40, 138, "ink")
r3_sub = T.put("MITS Madanapalle", "sans400", 14.5, 40, 157, "mut")

defs_content = T.defs()

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 0 900 170" width="900" height="170" role="img" aria-labelledby="t">
<title id="t">Recognition: LifeLink hackathon winner. Onco-IQ internship at NIT Pondicherry. IIC Innovation Coordinator and ARC Club Student Coordinator at MITS Madanapalle.</title>
{CSS}
{defs_content}
<!-- Row 1: LifeLink Hackathon -->
<rect class="hov" x="-10" y="3" width="1000" height="50" rx="4" opacity="0">
  <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.001;0.033;0.300;0.333;1" dur="7.5s" begin="1.0s" repeatCount="indefinite"/>
</rect>
<g transform="translate(2 16) scale(1.05)">
  <path class="line" d="M6 3h8v5a4 4 0 0 1-8 0z M6 5H3v1a3 3 0 0 0 3 3 M14 5h3v1a3 3 0 0 1-3 3 M10 12v3 M7 17h6"/>
</g>
{r1_t}
<rect class="outline" x="40" y="32" width="61.3" height="20" rx="10"/>
{r1_pill}
<line class="rule" x1="0" x2="880" y1="56" y2="56"/>

<!-- Row 2: Onco-IQ Internship -->
<rect class="hov" x="-10" y="59" width="1000" height="50" rx="4" opacity="0">
  <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.333;0.366;0.633;0.666;1" dur="7.5s" begin="1.0s" repeatCount="indefinite"/>
</rect>
<g transform="translate(2 72) scale(1.05)">
  <path class="line" d="M3 7h14v9H3z M7 7V5.2c0-.7.5-1.2 1.2-1.2h3.6c.7 0 1.2.5 1.2 1.2V7 M3 11.5h14"/>
</g>
{r2_t}
{r2_sub}
<line class="rule" x1="0" x2="880" y1="112" y2="112"/>

<!-- Row 3: Leadership -->
<rect class="hov" x="-10" y="115" width="1000" height="50" rx="4" opacity="0">
  <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.666;0.700;0.966;1.000;1" dur="7.5s" begin="1.0s" repeatCount="indefinite"/>
</rect>
<g transform="translate(2 128) scale(1.05)">
  <path class="line" d="M7 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M2 17c0-3 2.2-5 5-5s5 2 5 5 M14 8.3a2.4 2.4 0 1 0 0-4.8 M14.6 12.3c2.1.3 3.4 2 3.4 4.7"/>
</g>
{r3_t}
{r3_sub}
</svg>
"""

out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "recognition.svg")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg_content.strip() + "\n")

print(f"Generated assets/recognition.svg ({len(svg_content)} bytes)")
