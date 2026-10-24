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

<!-- Architecture Blueprint: Notion-style End-to-End Cloud Topology -->
<g class="line">
  <!-- 1. Client Browser / Web Terminal Window -->
  <g transform="translate(456, 18)">
    <rect x="0" y="0" width="70" height="56" rx="4"/>
    <line x1="0" y1="14" x2="70" y2="14"/>
    <circle cx="9" cy="7" r="2" class="up"/>
    <circle cx="16" cy="7" r="2" fill="#e5e7eb" stroke="none"/>
    <circle cx="23" cy="7" r="2" fill="#e5e7eb" stroke="none"/>
    <!-- Code lines inside editor -->
    <line x1="8" y1="24" x2="36" y2="24" stroke-width="1.2"/>
    <line x1="8" y1="32" x2="54" y2="32" stroke-width="1.2"/>
    <line x1="8" y1="40" x2="42" y2="40" stroke-width="1.2"/>
    <line x1="8" y1="48" x2="22" y2="48" stroke-width="1.2" class="up"/>
    <rect x="26" y="44" width="4" height="6" class="up">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Flow 1: Client -> API Gateway -->
  <path class="flow" d="M530 46 H558"/>
  <path d="M552 41 L558 46 L552 51"/>
  <circle class="up" cx="530" cy="46" r="2.5">
    <animate attributeName="cx" values="530;558" dur="1.6s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.6s" repeatCount="indefinite"/>
  </circle>

  <!-- 2. Edge API Gateway / Router -->
  <g transform="translate(564, 26)">
    <polygon points="20,0 40,20 20,40 0,20"/>
    <circle cx="20" cy="20" r="4" class="up"/>
    <circle cx="20" cy="20" r="4" class="ring">
      <animate attributeName="r" values="4;10;10" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Flow 2A: Gateway -> Worker Service -->
  <path class="flow" d="M606 38 H638"/>
  <path d="M632 33 L638 38 L632 43"/>
  <circle class="up" cx="606" cy="38" r="2.5">
    <animate attributeName="cx" values="606;638" dur="1.6s" begin="0.4s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.6s" begin="0.4s" repeatCount="indefinite"/>
  </circle>

  <!-- Flow 2B: Gateway -> Cache Bus -->
  <path class="flow" d="M584 66 V74 H638"/>
  <path d="M632 69 L638 74 L632 79"/>

  <!-- 3. Worker Service Node -->
  <g transform="translate(642, 18)">
    <rect x="0" y="0" width="56" height="34" rx="4"/>
    <line x1="10" y1="10" x2="46" y2="10" stroke-dasharray="2 3"/>
    <line x1="10" y1="17" x2="46" y2="17" stroke-dasharray="2 3"/>
    <line x1="10" y1="24" x2="38" y2="24" stroke-dasharray="2 3"/>
    <circle cx="48" cy="24" r="2" class="up">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="1.4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- 4. Low-Latency Cache (Redis) -->
  <g transform="translate(642, 60)">
    <rect x="0" y="0" width="56" height="26" rx="4"/>
    <path d="M12 13 H24 M12 18 H20" stroke-width="1.2"/>
    <!-- Lightning bolt glyph -->
    <path d="M38 5 L32 14 H37 L34 21 L43 11 H38 L40 5 Z" fill="none" class="up" stroke-width="1.1"/>
  </g>

  <!-- Flow 3: Worker & Cache -> Database -->
  <path class="flow" d="M702 35 H742"/>
  <path d="M736 30 L742 35 L736 40"/>
  <circle class="up" cx="702" cy="35" r="2.5">
    <animate attributeName="cx" values="702;742" dur="1.6s" begin="0.8s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.6s" begin="0.8s" repeatCount="indefinite"/>
  </circle>

  <path class="flow" d="M702 73 H726 V52 H742"/>
  <path d="M736 47 L742 52 L736 57"/>

  <!-- 5. Distributed Database Cluster (Primary + Replica) -->
  <g transform="translate(748, 18)">
    <!-- Primary Cylinder -->
    <path d="M0 12 V48 M52 12 V48 M0 12 A26 7 0 0 1 52 12 A26 7 0 0 1 0 12 M0 28 A26 7 0 0 0 52 28 M0 48 A26 7 0 0 0 52 48"/>
    <!-- Replica Cylinder behind -->
    <path d="M52 24 V58 M74 24 V58 M52 24 A18 5 0 0 1 74 24 M52 40 A18 5 0 0 0 74 40 M52 58 A18 5 0 0 0 74 58" stroke-dasharray="3 3"/>
    <ellipse cx="26" cy="12" rx="13" ry="3.5" class="ring">
      <animate attributeName="rx" values="13;22;22" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
      <animate attributeName="ry" values="3.5;6;6" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
    </ellipse>
  </g>

  <!-- 6. Real-time Telemetry Broadcast Beacon -->
  <g transform="translate(840, 36)">
    <circle cx="0" cy="0" r="3" class="up"/>
    <path d="M-6 -8 A10 10 0 0 0 -6 8 M6 -8 A10 10 0 0 1 6 8" stroke-width="1.2">
      <animate attributeName="opacity" values="0.2;1;0.2" dur="1.8s" repeatCount="indefinite"/>
    </path>
    <path d="M-11 -13 A17 17 0 0 0 -11 13 M11 -13 A17 17 0 0 1 11 13" stroke-width="1.2">
      <animate attributeName="opacity" values="0.1;0.7;0.1" dur="1.8s" begin="0.4s" repeatCount="indefinite"/>
    </path>
  </g>
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
