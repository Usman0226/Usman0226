#!/usr/bin/env python3
"""Generate the clean, human, motion-rich assets/hero.svg.
Replaces AI-sounding phrasing with authentic, relevant engineering language.
Replaces theoretical research item with real-world Hackathon recognition (LifeLink 1st place).
Includes perpetual micro-interactions on the 3 metrics and architecture pipeline.
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))
from typeset import Text

T = Text()
W, H = 880, 458

config_path = os.path.join(os.path.dirname(__file__), "profile_config.json")
config = {}
if os.path.exists(config_path):
    try:
        config = json.load(open(config_path, encoding="utf-8"))
    except Exception:
        pass

p_light = config.get("colors", {}).get("primary", {}).get("light", "#2383e2")
p_dark = config.get("colors", {}).get("primary", {}).get("dark", "#529cca")
p_bg_light = config.get("colors", {}).get("primary_bg", {}).get("light", "#e7f3f8")
p_bg_dark = config.get("colors", {}).get("primary_bg", {}).get("dark", "#182833")
p_txt_light = config.get("colors", {}).get("primary_txt", {}).get("light", "#1967b2")
p_txt_dark = config.get("colors", {}).get("primary_txt", {}).get("dark", "#6cb3e8")

CSS = f"""<style>
.cov{{fill:#f4f4f2}}.ghost{{fill:#e7e7e4}}
.ink{{fill:#161616}}.mut{{fill:#6e6e6e}}.faint{{fill:#b6b6b6}}.rule{{stroke:#e2e2e2;stroke-width:1}}
.line{{fill:none;stroke:#161616;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}}
.hov{{fill:#f4f4f4}}.outline{{fill:none;stroke:#c7c7c7;stroke-width:1}}
.up{{fill:#1a9d5a}}.ring{{fill:none;stroke:#1a9d5a;stroke-width:1.2}}.down{{fill:#c0392b}}
.blue{{fill:{p_light}}}.blue-ln{{fill:none;stroke:{p_light};stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}}
.gold{{fill:#d97706}}.gold-ln{{fill:none;stroke:#d97706;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}}
.tag-bg{{fill:#eef6ef}}.tag-txt{{fill:#1a9d5a;font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;font-size:9.5px;font-weight:700}}
.blue-bg{{fill:{p_bg_light}}}.blue-txt{{fill:{p_txt_light};font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;font-size:9.5px;font-weight:700}}
.gold-bg{{fill:#fef3c7}}.gold-txt{{fill:#b45309;font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;font-size:9.5px;font-weight:700}}
@media (prefers-color-scheme:dark){{
.cov{{fill:#1b1b1b}}.ghost{{fill:#222}}
.ink{{fill:#f0f0f0}}.mut{{fill:#9a9a9a}}.faint{{fill:#4d4d4d}}.rule{{stroke:#2b2b2b}}
.line{{stroke:#f0f0f0}}.hov{{fill:#1e1e1e}}.outline{{stroke:#3a3a3a}}
.up{{fill:#3fb97a}}.ring{{stroke:#3fb97a}}.down{{fill:#e0574a}}
.blue{{fill:{p_dark}}}.blue-ln{{stroke:{p_dark}}}
.blue-bg{{fill:{p_bg_dark}}}.blue-txt{{fill:{p_txt_dark}}}
.gold{{fill:#f59e0b}}.gold-ln{{stroke:#f59e0b}}
.tag-bg{{fill:#1a2e22}}.tag-txt{{fill:#3fb97a}}
.gold-bg{{fill:#362615}}.gold-txt{{fill:#fbbf24}}
}}
</style>"""

hero_cfg = config.get("hero", {})
name_text = hero_cfg.get("name", "Usman")
status_text = hero_cfg.get("status", "Available for freelance & contracts")
bio1_text = hero_cfg.get("bio1", "Full-stack and AI engineer building real-time web applications and backend systems.")
bio2_text = hero_cfg.get("bio2", "Focused on reliable architecture, clean interfaces, and shipping for clients and teams.")

m1 = hero_cfg.get("metric1", {"val": "2,100+", "l1": "students cleared dues", "l2": "through NoDues at MITS"})
m2 = hero_cfg.get("metric2", {"val": "4", "l1": "production platforms live", "l2": "NoDues \u00b7 D\u2019FESTA \u00b7 NCC \u00b7 BizEasy"})
m3 = hero_cfg.get("metric3", {"val": "10+", "l1": "tools, APIs & motion libraries", "l2": "React motion, OCR benchmarks & agents"})

# Pre-render text lines using typeset
name_el = T.put(name_text, "sans600", 68, -2, 206, "ink")
intern_el = T.put(status_text, "sans400", 16.5, 520, 186, "mut")

bio1_el = T.put(bio1_text, "sans400", 19.5, 0, 254, "ink")
bio2_el = T.put(bio2_text, "sans400", 19.5, 0, 284, "ink")

stat1_num = T.put(m1["val"], "sans600", 34, -1, 394, "ink")
stat1_l1 = T.put(m1["l1"], "sans400", 14.5, 0, 419, "mut")
stat1_l2 = T.put(m1["l2"], "sans400", 14.5, 0, 440, "mut")

stat2_num = T.put(m2["val"], "sans600", 34, 299, 394, "ink")
stat2_l1 = T.put(m2["l1"], "sans400", 14.5, 300, 419, "mut")
stat2_l2 = T.put(m2["l2"], "sans400", 14.5, 300, 440, "mut")

stat3_num = T.put(m3["val"], "sans600", 34, 599, 394, "ink")
stat3_l1 = T.put(m3["l1"], "sans400", 14.5, 600, 419, "mut")
stat3_l2 = T.put(m3["l2"], "sans400", 14.5, 600, 440, "mut")

# Ghost number "01" at top
ghost_01 = f"""<g class="ghost">
  <use href="#gserI400_30" transform="translate(730.00 150.00) scale(0.15000)"/>
  <use href="#gserI400_31" transform="translate(802.00 150.00) scale(0.15000)"/>
</g>"""

# Defs of glyphs
defs_content = T.defs()

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Usman</title>
<desc id="d">Full-stack and AI engineer building real-time web applications and backend systems. Available for freelance &amp; contracts. 2,100+ students cleared dues through NoDues at MITS. 4 production platforms live. 10+ shipped tools, APIs, and libraries.</desc>
{CSS}
{defs_content}
<!-- Top canvas header banner -->
<rect class="cov" x="0" y="0" width="{W}" height="104"/>
{ghost_01}

<!-- Architecture Diagram (Chat -> Worker Queue -> Database) with animated data packets -->
<g class="line">
  <!-- Incoming Event / Chat Bubble -->
  <path d="M500 20 H560 Q568 20 568 28 V50 Q568 58 560 58 H524 L512 70 L513 58 H510 Q502 58 502 50 V28 Q502 20 510 20 Z"/>
  <path d="M512 33 H554 M512 44 H536"/>

  <!-- Path 1: Client -> Worker Queue -->
  <path class="flow" d="M578 40 H624"/>
  <path d="M616 34 L624 40 L616 46"/>

  <!-- Flowing packet 1 (Client to Queue) -->
  <circle class="up" cx="578" cy="40" r="2.8">
    <animate attributeName="cx" values="578;622" dur="1.8s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.8s" repeatCount="indefinite"/>
  </circle>

  <!-- Worker Queue Nodes -->
  <rect x="632" y="18" width="58" height="16" rx="4">
    <animate attributeName="stroke" values="#161616;#1a9d5a;#161616" dur="3s" repeatCount="indefinite"/>
  </rect>
  <rect x="632" y="38" width="58" height="16" rx="4">
    <animate attributeName="stroke" values="#161616;#1a9d5a;#161616" dur="3s" begin="1s" repeatCount="indefinite"/>
  </rect>
  <rect x="632" y="58" width="58" height="16" rx="4">
    <animate attributeName="stroke" values="#161616;#1a9d5a;#161616" dur="3s" begin="2s" repeatCount="indefinite"/>
  </rect>
  <line x1="640" y1="26" x2="682" y2="26" stroke-dasharray="2 3"/>
  <line x1="640" y1="46" x2="682" y2="46" stroke-dasharray="2 3"/>
  <line x1="640" y1="66" x2="682" y2="66" stroke-dasharray="2 3"/>

  <!-- Path 2: Queue -> Database -->
  <path class="flow" d="M698 46 H742"/>
  <path d="M734 40 L742 46 L734 52"/>

  <!-- Flowing packet 2 (Queue to DB) -->
  <circle class="up" cx="698" cy="46" r="2.8">
    <animate attributeName="cx" values="698;740" dur="1.8s" begin="0.9s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.8s" begin="0.9s" repeatCount="indefinite"/>
  </circle>

  <!-- Database Cylinder -->
  <path d="M750 30 V62 M806 30 V62 M750 30 A28 8 0 0 1 806 30 A28 8 0 0 1 750 30 M750 62 A28 8 0 0 0 806 62 M750 46 A28 8 0 0 0 806 46"/>
  <ellipse cx="778" cy="30" rx="14" ry="4" class="ring">
    <animate attributeName="rx" values="14;24;24" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
    <animate attributeName="ry" values="4;7;7" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;0;0" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
  </ellipse>
</g>

<!-- Divider Rule at y=104 -->
<line class="rule" x1="0" y1="104" x2="{W}" y2="104" stroke-dasharray="{W}">
  <animate attributeName="stroke-dashoffset" values="{W};{W};0;0" keyTimes="0;0.04;0.22;1" dur="6.0s" begin="0s" fill="freeze"/>
</line>

<!-- Name "Usman" -->
<g>
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.0250;0.1750;1" dur="6.0s" begin="0s" fill="freeze"/>
  {name_el}
</g>

<!-- Open to Internships status badge -->
<g>
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.0917;0.2417;1" dur="6.0s" begin="0s" fill="freeze"/>
  <circle class="up" cx="505" cy="179" r="4"/>
  <circle class="ring" cx="505" cy="179" r="4">
    <animate attributeName="r" values="4;12;12" keyTimes="0;0.8;1" dur="3.2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0" keyTimes="0;0.8;1" dur="3.2s" repeatCount="indefinite"/>
  </circle>
  {intern_el}
</g>

<!-- Bio Paragraph (Clean, relevant, human engineering statement) -->
<g>
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.1500;0.3000;1" dur="6.0s" begin="0s" fill="freeze"/>
  {bio1_el}
  {bio2_el}
</g>

<!-- Divider Rule at y=340 -->
<line class="rule" x1="0" x2="{W}" y1="340" y2="340"/>

<!-- ============================================================== -->
<!-- METRIC 1: 2,100+ Clearances with Live SSE Motion -->
<!-- ============================================================== -->
<g>
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.2167;0.3667;1" dur="6.0s" begin="0s" fill="freeze"/>
  {stat1_num}

  <!-- Live SSE Streaming Badge beside 2,100+ -->
  <g transform="translate(112, 368)">
    <rect class="tag-bg" x="0" y="0" width="86" height="18" rx="4"/>
    <circle class="up" cx="10" cy="9" r="3.2"/>
    <circle class="ring" cx="10" cy="9" r="3.2">
      <animate attributeName="r" values="3.2;9;9" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text class="tag-txt" x="20" y="12.5">SSE LIVE</text>
  </g>

  {stat1_l1}
  {stat1_l2}

  <!-- Animated Real-time Approval Flow Bar -->
  <g transform="translate(0, 452)">
    <line class="rule" x1="0" y1="0" x2="220" y2="0"/>
    <rect class="up" x="0" y="-1.5" width="45" height="3" rx="1.5">
      <animate attributeName="x" values="0;175;0" dur="3.6s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1"/>
    </rect>
  </g>
</g>

<!-- ============================================================== -->
<!-- METRIC 2: 4 Production Platforms with Live System Heartbeats -->
<!-- ============================================================== -->
<g>
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.2533;0.4033;1" dur="6.0s" begin="0s" fill="freeze"/>
  {stat2_num}

  <!-- Multi-platform status badge beside 4 -->
  <g transform="translate(330, 368)">
    <rect class="tag-bg" x="0" y="0" width="168" height="18" rx="4"/>
    <circle class="up" cx="12" cy="9" r="2.8">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.1s" repeatCount="indefinite"/>
    </circle>
    <text class="tag-txt" x="18" y="12.5">NoDues</text>

    <circle class="up" cx="66" cy="9" r="2.8">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.1s" begin="0.7s" repeatCount="indefinite"/>
    </circle>
    <text class="tag-txt" x="72" y="12.5">D&apos;FESTA</text>

    <circle class="up" cx="124" cy="9" r="2.8">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.1s" begin="1.4s" repeatCount="indefinite"/>
    </circle>
    <text class="tag-txt" x="130" y="12.5">NCC</text>
  </g>

  {stat2_l1}
  {stat2_l2}

  <!-- Animated Uptime Heartbeat Line -->
  <g transform="translate(300, 452)">
    <line class="rule" x1="0" y1="0" x2="230" y2="0"/>
    <rect class="up" x="0" y="-1.5" width="45" height="3" rx="1.5">
      <animate attributeName="x" values="0;185;0" dur="4.2s" begin="0.6s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1"/>
    </rect>
  </g>
</g>

<!-- ============================================================== -->
<!-- METRIC 3: 10+ Shipped Tools, APIs & Libraries -->
<!-- ============================================================== -->
<g>
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.2900;0.4400;1" dur="6.0s" begin="0s" fill="freeze"/>
  {stat3_num}

  <!-- Shipped Tag beside 10+ (Blue) -->
  <g transform="translate(670, 368)">
    <rect class="blue-bg" x="0" y="0" width="78" height="18" rx="4"/>
    <circle class="blue" cx="10" cy="9" r="3.2"/>
    <circle class="blue-ln" cx="10" cy="9" r="3.2">
      <animate attributeName="r" values="3.2;9;9" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text class="blue-txt" x="20" y="12.5">SHIPPED</text>
  </g>

  {stat3_l1}
  {stat3_l2}

  <!-- Animated Output Progress Bar (Blue) -->
  <g transform="translate(600, 452)">
    <line class="rule" x1="0" y1="0" x2="230" y2="0"/>
    <rect class="blue" x="0" y="-1.5" width="45" height="3" rx="1.5">
      <animate attributeName="x" values="0;185;0" dur="3.8s" begin="1.2s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1"/>
    </rect>
  </g>
</g>
</svg>
"""

out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hero.svg")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg_content.strip() + "\n")

print(f"Generated hero.svg ({len(svg_content)} bytes)")
