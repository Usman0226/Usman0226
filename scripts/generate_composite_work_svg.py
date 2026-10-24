#!/usr/bin/env python3
"""Generate assets/work.svg as a unified Notion animated showcase.
Renders a 2-column by 3-row grid (880x640) of Notion cards with
hand-drawn wobbly filters, pastel backings, and animated micro-interactions.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from typeset import Text

T = Text()
W, H = 880, 620

CSS = """<style>
.ink{fill:#37352f}.mut{fill:#787774}.rule{stroke:#e9e9e7;stroke-width:1}
.ln{fill:none;stroke:#37352f;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.thin{stroke-width:1.5;stroke:#787774}
.bgY{fill:#fbf3db}.bgB{fill:#e7f3f8}.bgP{fill:#f9eef3}.bgG{fill:#edf3ec}.bgO{fill:#fbebe3}.bgN{fill:#f1f1ef}.bgR{fill:#fbebe9}
.fY{fill:#fdecc8}.fB{fill:#d3e5ef}.fP{fill:#f5e0e9}.fG{fill:#dbeddb}.fO{fill:#fadec9}.fR{fill:#fadbd8}.paper{fill:#ffffff}.solid{fill:#37352f;stroke:none}
.cb{fill:#d3e5ef}.cg{fill:#dbeddb}.co{fill:#fadec9}.cp{fill:#f5e0e9}.cy{fill:#fdecc8}.hov{fill:#f1f1ef}
.scan{fill:none;stroke:#2383e2;stroke-width:2.5;stroke-linecap:round}.blue{fill:#2383e2}
.blue-ln{fill:none;stroke:#2383e2;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.green{fill:#1a9d5a}.green-ln{fill:none;stroke:#1a9d5a;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.red{fill:#e03e3e}.red-ln{fill:none;stroke:#e03e3e;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.gold-bg{fill:#fef3c7}.gold-txt{fill:#b45309;font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;font-size:9.5px;font-weight:700}
.txt-sm{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:10px;font-weight:600;fill:#787774}
.txt-red{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:10px;font-weight:800;letter-spacing:0.5px;fill:#e03e3e}
.txt-stamp{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:11px;font-weight:800;letter-spacing:1px;fill:#1a9d5a}
.txt-mono{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;font-size:10px;font-weight:600;fill:#37352f}
.card-bg{fill:#ffffff;stroke:#e2e2e2;stroke-width:1}
@media (prefers-color-scheme:dark){
.ink{fill:#e6e5e3}.mut{fill:#9b9a97}.rule{stroke:#373737}
.ln{stroke:#e6e5e3}.thin{stroke:#9b9a97}
.bgY{fill:#342f21}.bgB{fill:#1d2a32}.bgP{fill:#30262b}.bgG{fill:#202b24}.bgO{fill:#33271f}.bgN{fill:#262626}.bgR{fill:#342323}
.fY{fill:#4d4228}.fB{fill:#29414f}.fP{fill:#4a3641}.fG{fill:#2c4638}.fO{fill:#553d29}.fR{fill:#4e2929}.paper{fill:#1f1f1f}.solid{fill:#e6e5e3}
.cb{fill:#203c4c}.cg{fill:#1f3a2c}.co{fill:#4a3321}.cp{fill:#43303b}.cy{fill:#463c24}.hov{fill:#262626}
.scan{stroke:#529cca}.blue{fill:#529cca}.blue-ln{stroke:#529cca}
.green{fill:#3fb97a}.green-ln{stroke:#3fb97a}
.red{fill:#eb5757}.red-ln{stroke:#eb5757}
.gold-bg{fill:#362615}.gold-txt{fill:#fbbf24}
.txt-sm{fill:#9b9a97}.txt-red{fill:#eb5757}.txt-stamp{fill:#3fb97a}.txt-mono{fill:#e6e5e3}
.card-bg{fill:#191919;stroke:#2b2b2b}
}
</style>"""

WOB_FILTER = """<defs>
<filter id="wob" x="-5%" y="-8%" width="110%" height="116%">
  <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="5" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/>
</filter>
</defs>"""

# Card 1: NoDues
nodues_group = f"""<g transform="translate(0, 0)">
  <!-- Card Shell -->
  <rect class="card-bg" x="0" y="0" width="425" height="190" rx="8"/>
  <g transform="translate(12, 12) scale(0.65)">
    <!-- Clipboard Backing -->
    <rect class="solid" x="96" y="24" width="208" height="138" rx="10" opacity="0.12"/>
    <rect class="ln paper" x="92" y="20" width="216" height="142" rx="8"/>
    <rect class="solid" x="166" y="12" width="68" height="18" rx="4" opacity="0.85"/>
    <rect class="ln paper" x="178" y="16" width="44" height="10" rx="3"/>
    <rect class="ln" x="114" y="46" width="14" height="14" rx="3"/>
    <path class="green-ln" d="M117 53 L121 57 L127 49" stroke-dasharray="16" stroke-dashoffset="16">
      <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.12;0.22;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
    </path>
    <path class="ln" d="M138 53 H215"/>
    <rect class="ln" x="114" y="70" width="14" height="14" rx="3"/>
    <path class="green-ln" d="M117 77 L121 81 L127 73" stroke-dasharray="16" stroke-dashoffset="16">
      <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.32;0.42;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
    </path>
    <path class="ln" d="M138 77 H235"/>
    <rect class="ln" x="114" y="94" width="14" height="14" rx="3"/>
    <path class="green-ln" d="M117 101 L121 105 L127 97" stroke-dasharray="16" stroke-dashoffset="16">
      <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.52;0.62;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
    </path>
    <path class="ln" d="M138 101 H205"/>
    <rect class="ln paper" x="114" y="126" width="172" height="14" rx="7"/>
    <rect class="fG" x="116" y="128" width="20" height="10" rx="5">
      <animate attributeName="width" values="20;60;115;168;168;20" keyTimes="0;0.25;0.45;0.65;0.88;0.98" dur="5.5s" repeatCount="indefinite"/>
    </rect>
    <g transform="translate(200, 78) rotate(-10)">
      <g>
        <rect class="paper" x="-5" y="-14" width="94" height="26" rx="4" stroke="#1a9d5a" stroke-width="2"/>
        <text class="txt-stamp" x="6" y="3">CLEARED ✓</text>
        <animateTransform attributeName="transform" type="scale" values="0;0;1.15;1.0;1.0;0" keyTimes="0;0.63;0.70;0.74;0.88;0.95" dur="5.5s" repeatCount="indefinite"/>
      </g>
    </g>
  </g>
  <!-- Card Text details -->
  {T.put("01  NoDues", "sans600", 17, 230, 36, "ink")}
  <circle class="up" cx="395" cy="30" r="3"/>
  <circle class="ring" cx="395" cy="30" r="3"><animate attributeName="r" values="3;8;8" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0;0" dur="2.4s" repeatCount="indefinite"/></circle>
  {T.put("Semester clearance for 2,100 students & 30+ faculty at MITS.", "sans400", 12.5, 230, 62, "mut")}
  {T.put("Live approvals streaming over SSE.", "sans400", 12.5, 230, 80, "mut")}
  {T.put("React \u00b7 Express \u00b7 MongoDB", "sans400", 11.5, 230, 114, "faint")}
  {T.put("Live at nodues-arcclub.tech \u2197", "sans600", 11.5, 230, 142, "ink")}
</g>"""

# Card 2: D'FESTA 2K26
dfesta_group = f"""<g transform="translate(455, 0)">
  <rect class="card-bg" x="0" y="0" width="425" height="190" rx="8"/>
  <g transform="translate(12, 12) scale(0.65)">
    <path class="ln paper" d="M98 38 H298 a14 14 0 0 1 14 14 V70 a14 14 0 0 0 0 28 V124 a14 14 0 0 1 -14 14 H98 a14 14 0 0 1 -14 -14 V98 a14 14 0 0 0 0 -28 V52 a14 14 0 0 1 14 -14 Z"/>
    <path class="ln thin" d="M234 46 V128" stroke-dasharray="3 6"/>
    <path class="ln" d="M112 66 H195"/>
    <path class="ln thin" d="M112 86 H175 M112 102 H155"/>
    <rect class="fP" x="112" y="116" width="70" height="14" rx="4"/>
    <text class="txt-sm" x="120" y="127">ENTRY PASS</text>
    <rect class="solid" x="246" y="62" width="11" height="11" rx="2.5"/>
    <rect class="ln" x="246" y="78" width="11" height="11" rx="2.5"/>
    <rect class="solid" x="246" y="94" width="11" height="11" rx="2.5"/>
    <rect class="ln" x="262" y="62" width="11" height="11" rx="2.5"/>
    <rect class="solid" x="262" y="78" width="11" height="11" rx="2.5"/>
    <rect class="ln" x="262" y="94" width="11" height="11" rx="2.5"/>
    <rect class="solid" x="278" y="62" width="11" height="11" rx="2.5"/>
    <rect class="ln" x="278" y="78" width="11" height="11" rx="2.5"/>
    <rect class="solid" x="278" y="94" width="11" height="11" rx="2.5"/>
    <g>
      <path class="scan" d="M240 62 H294">
        <animateTransform attributeName="transform" type="translate" values="0 0;0 46;0 0" keyTimes="0;0.5;1" dur="2.8s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
      </path>
    </g>
  </g>
  {T.put("02  D\u2019FESTA 2K26", "sans600", 17, 230, 36, "ink")}
  <circle class="up" cx="400" cy="30" r="3"/>
  <circle class="ring" cx="400" cy="30" r="3"><animate attributeName="r" values="3;8;8" dur="2.4s" begin="0.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0;0" dur="2.4s" begin="0.4s" repeatCount="indefinite"/></circle>
  {T.put("Ticketing, payments & judging for symposium.", "sans400", 12.5, 230, 62, "mut")}
  {T.put("AES-signed QR tickets & 3-node SMTP failover.", "sans400", 12.5, 230, 80, "mut")}
  {T.put("Next.js 16 \u00b7 TypeScript \u00b7 MongoDB", "sans400", 11.5, 230, 114, "faint")}
  {T.put("Live at dfesta.in \u2197", "sans600", 11.5, 230, 142, "ink")}
</g>"""

# Card 3: BizEasy
bizeasy_group = f"""<g transform="translate(0, 210)">
  <rect class="card-bg" x="0" y="0" width="425" height="190" rx="8"/>
  <g transform="translate(12, 12) scale(0.65)">
    <rect class="ln paper" x="86" y="16" width="228" height="144" rx="10"/>
    <path class="ln thin" d="M86 42 H314"/>
    <circle class="green" cx="106" cy="29" r="6"/>
    <path class="ln" d="M120 29 H190"/>
    <g>
      <rect class="ln fB" x="100" y="52" width="138" height="28" rx="8"/>
      <path class="ln" d="M112 63 H195"/>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.05;0.12;0.88;0.95;1" dur="6s" repeatCount="indefinite"/>
    </g>
    <g>
      <rect class="ln paper" x="162" y="86" width="140" height="34" rx="8"/>
      <path class="ln" d="M174 97 H275"/>
      <rect class="fG" x="174" y="103" width="76" height="12" rx="3"/>
      <text class="txt-sm" x="180" y="112" fill="#1a9d5a">PAY ₹650 ↗</text>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.34;0.88;0.95;1" dur="6s" repeatCount="indefinite"/>
    </g>
    <g>
      <rect class="solid" x="110" y="128" width="180" height="22" rx="5" fill="#1a9d5a" opacity="0.95"/>
      <text class="txt-stamp" x="122" y="143" fill="#ffffff" font-size="10px">WEBHOOK: PAID ✓</text>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.48;0.56;0.88;0.96;1" dur="6s" repeatCount="indefinite"/>
    </g>
  </g>
  {T.put("03  BizEasy", "sans600", 17, 230, 36, "ink")}
  <circle class="outline" cx="395" cy="30" r="3"/>
  {T.put("Multi-tenant WhatsApp commerce platform.", "sans400", 12.5, 230, 62, "mut")}
  {T.put("Per-seller bot state machine with Razorpay links.", "sans400", 12.5, 230, 80, "mut")}
  {T.put("Node.js \u00b7 Meta Cloud API \u00b7 Razorpay", "sans400", 11.5, 230, 114, "faint")}
  {T.put("In active development", "sans600", 11.5, 230, 142, "mut")}
</g>"""

# Card 4: NCC Exam Portal
ncc_group = f"""<g transform="translate(455, 210)">
  <rect class="card-bg" x="0" y="0" width="425" height="190" rx="8"/>
  <g transform="translate(12, 12) scale(0.65)">
    <rect class="ln paper" x="80" y="18" width="238" height="144" rx="8"/>
    <rect class="fY" x="96" y="30" width="86" height="16" rx="4"/>
    <text class="txt-sm" x="103" y="42">NCC TIRUPATI</text>
    <g transform="translate(270, 38)">
      <circle class="ln paper" cx="0" cy="0" r="14"/>
      <circle class="solid" cx="0" cy="0" r="2"/>
      <line class="ln" x1="0" y1="0" x2="0" y2="-6"/>
      <line class="ln thin" x1="0" y1="0" x2="0" y2="-10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
      </line>
    </g>
    <path class="ln thin" d="M96 56 H298"/>
    <rect class="ln" x="96" y="66" width="206" height="66" rx="6"/>
    <path class="ln" d="M108 78 H260"/>
    <circle class="ln" cx="116" cy="104" r="5"/>
    <path class="ln thin" d="M128 104 H195"/>
    <circle class="ln" cx="116" cy="120" r="5"/>
    <circle class="green" cx="116" cy="120" r="0">
      <animate attributeName="r" values="0;0;3.2;3.2;0" keyTimes="0;0.3;0.38;0.88;0.96" dur="5s" repeatCount="indefinite"/>
    </circle>
    <path class="ln thin" d="M128 120 H225"/>
  </g>
  {T.put("04  NCC Exam Portal", "sans600", 17, 230, 36, "ink")}
  <circle class="up" cx="400" cy="30" r="3"/>
  <circle class="ring" cx="400" cy="30" r="3"><animate attributeName="r" values="3;8;8" dur="2.4s" begin="0.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0;0" dur="2.4s" begin="0.8s" repeatCount="indefinite"/></circle>
  {T.put("Timed examinations for NCC Tirupati Unit.", "sans400", 12.5, 230, 62, "mut")}
  {T.put("Tenant isolation & server-enforced exam timer.", "sans400", 12.5, 230, 80, "mut")}
  {T.put("React \u00b7 Express \u00b7 PostgreSQL \u00b7 Prisma", "sans400", 11.5, 230, 114, "faint")}
  {T.put("Live at ncc-exam-portal \u2197", "sans600", 11.5, 230, 142, "ink")}
</g>"""

# Card 5: HireMinds AI
hireminds_group = f"""<g transform="translate(0, 420)">
  <rect class="card-bg" x="0" y="0" width="425" height="190" rx="8"/>
  <g transform="translate(12, 12) scale(0.65)">
    <g>
      <path class="ln fO" d="M92 28 H194 a12 12 0 0 1 12 12 V56 a12 12 0 0 1 -12 12 H110 L94 82 V68 H92 a12 12 0 0 1 -12 -12 V40 a12 12 0 0 1 12 -12 Z"/>
      <text class="txt-stamp" x="104" y="52" fill="#37352f" font-size="16px">AI?</text>
      <path class="ln thin" d="M140 48 H190 M140 58 H175"/>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.04;0.09;0.90;0.96;1" dur="7s" repeatCount="indefinite"/>
    </g>
    <g>
      <rect class="ln fB" x="190" y="82" width="134" height="42" rx="12"/>
      <path class="ln thin" d="M204 97 H302 M204 110 H268"/>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.26;0.32;0.90;0.96;1" dur="7s" repeatCount="indefinite"/>
    </g>
    <rect class="ln paper" x="92" y="142" width="216" height="16" rx="8"/>
    <rect class="fG" x="94" y="144" width="20" height="12" rx="6">
      <animate attributeName="width" values="20;50;130;190;190;20" keyTimes="0;0.32;0.50;0.72;0.90;0.98" dur="7s" repeatCount="indefinite"/>
    </rect>
  </g>
  {T.put("05  HireMinds AI", "sans600", 17, 230, 36, "ink")}
  <circle class="outline" cx="395" cy="30" r="3"/>
  {T.put("Autonomous technical interviewer with critic layer.", "sans400", 12.5, 230, 62, "mut")}
  {T.put("Agent loop & multi-layer candidate evaluation.", "sans400", 12.5, 230, 80, "mut")}
  {T.put("FastAPI \u00b7 React \u00b7 Groq", "sans400", 11.5, 230, 114, "faint")}
  {T.put("Source on GitHub \u2197", "sans600", 11.5, 230, 142, "ink")}
</g>"""

# Card 6: LifeLink
lifelink_group = f"""<g transform="translate(455, 420)">
  <rect class="card-bg" x="0" y="0" width="425" height="190" rx="8"/>
  <g transform="translate(12, 12) scale(0.65)">
    <rect class="ln paper" x="70" y="16" width="258" height="144" rx="8"/>
    <!-- Top Dispatch Status Bar -->
    <rect class="fR" x="84" y="28" width="94" height="18" rx="4"/>
    <circle class="red" cx="95" cy="37" r="3.2">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.4s" repeatCount="indefinite"/>
    </circle>
    <text class="txt-red" x="105" y="41">SOS DISPATCH</text>

    <!-- Route Grid -->
    <path class="ln thin" d="M84 72 H314 M84 102 H314 M84 132 H314" stroke-dasharray="2 4" opacity="0.5"/>
    <path class="ln thin" d="M130 54 V136 M190 54 V136 M250 54 V136 M300 54 V136" stroke-dasharray="2 4" opacity="0.5"/>

    <!-- Route Paths -->
    <path class="blue-ln" d="M105 118 L160 118 L190 85 L285 85" stroke-dasharray="6 4" opacity="0.6"/>
    <path class="red-ln" d="M105 118 L160 118 L190 85 L285 85" stroke-dasharray="210" stroke-dashoffset="210">
      <animate attributeName="stroke-dashoffset" values="210;0;0;210" keyTimes="0;0.55;0.85;1" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1"/>
    </path>

    <!-- Patient SOS Beacon Node -->
    <g transform="translate(105, 118)">
      <circle class="red" cx="0" cy="0" r="4.5"/>
      <circle class="red-ln" cx="0" cy="0" r="4.5">
        <animate attributeName="r" values="4.5;13;13" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.8;0;0" dur="2s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Moving Ambulance -->
    <g>
      <animateMotion path="M105 118 L160 118 L190 85 L285 85" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1" keyTimes="0;0.55;0.85;1">
        <mpath/>
      </animateMotion>
      <rect class="ln paper" x="-10" y="-12" width="20" height="12" rx="3"/>
      <rect class="red" x="-2" y="-10" width="4" height="8"/>
      <rect class="red" x="-4" y="-8" width="8" height="4"/>
      <circle class="solid" cx="-5" cy="0" r="2"/>
      <circle class="solid" cx="5" cy="0" r="2"/>
    </g>

    <!-- Hospital Station Node -->
    <g transform="translate(285, 85)">
      <rect class="ln paper" x="-13" y="-13" width="26" height="26" rx="5"/>
      <rect class="red" x="-2" y="-8" width="4" height="16" rx="1"/>
      <rect class="red" x="-8" y="-2" width="16" height="4" rx="1"/>
      <circle class="blue-ln" cx="0" cy="0" r="14">
        <animate attributeName="r" values="14;22;22" dur="2.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.7;0;0" dur="2.5s" repeatCount="indefinite"/>
      </circle>
    </g>
  </g>
  {T.put("06  LifeLink", "sans600", 17, 230, 36, "ink")}
  <rect class="gold-bg" x="350" y="21" width="60" height="17" rx="3"/>
  <text class="gold-txt" x="358" y="32.5">WINNER</text>
  {T.put("Emergency dispatch & geolocation platform.", "sans400", 12.5, 230, 62, "mut")}
  {T.put("Real-time ambulance routing & hospital status.", "sans400", 12.5, 230, 80, "mut")}
  {T.put("React \u00b7 Node.js \u00b7 Socket.io \u00b7 Leaflet", "sans400", 11.5, 230, 114, "faint")}
  {T.put("Source on GitHub \u2197", "sans600", 11.5, 230, 142, "ink")}
</g>"""

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Selected work by Usman: NoDues, D'FESTA 2K26, BizEasy, NCC Exam Portal, HireMinds AI, LifeLink.</title>
{CSS}
{WOB_FILTER}
{T.defs()}
<g filter="url(#wob)">
  {nodues_group}
  {dfesta_group}
  {bizeasy_group}
  {ncc_group}
  {hireminds_group}
  {lifelink_group}
</g>
</svg>
"""

out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "work.svg")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg_content.strip() + "\n")

print(f"Generated composite work.svg ({len(svg_content)} bytes)")
