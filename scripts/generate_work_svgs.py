#!/usr/bin/env python3
"""Generate the 6 Notion-style animated SVGs for the Work showcase.
Each SVG uses Notion's signature wobbly-doodle filter, pastel palette,
and perpetual micro-interactions.
"""
import os

COMMON_STYLES = """<style>
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
.txt-sm{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:10px;font-weight:600;fill:#787774}
.txt-red{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:10px;font-weight:800;letter-spacing:0.5px;fill:#e03e3e}
.txt-stamp{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:11px;font-weight:800;letter-spacing:1px;fill:#1a9d5a}
.txt-mono{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;font-size:10.5px;font-weight:600;fill:#37352f}
.txt-stat{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:24px;font-weight:800;fill:#37352f}
@media (prefers-color-scheme:dark){
.ink{fill:#e6e5e3}.mut{fill:#9b9a97}.rule{stroke:#373737}
.ln{stroke:#e6e5e3}.thin{stroke:#9b9a97}
.bgY{fill:#342f21}.bgB{fill:#1d2a32}.bgP{fill:#30262b}.bgG{fill:#202b24}.bgO{fill:#33271f}.bgN{fill:#262626}.bgR{fill:#342323}
.fY{fill:#4d4228}.fB{fill:#29414f}.fP{fill:#4a3641}.fG{fill:#2c4638}.fO{fill:#553d29}.fR{fill:#4e2929}.paper{fill:#1f1f1f}.solid{fill:#e6e5e3}
.cb{fill:#203c4c}.cg{fill:#1f3a2c}.co{fill:#4a3321}.cp{fill:#43303b}.cy{fill:#463c24}.hov{fill:#262626}
.scan{stroke:#529cca}.blue{fill:#529cca}.blue-ln{stroke:#529cca}
.green{fill:#3fb97a}.green-ln{stroke:#3fb97a}
.red{fill:#eb5757}.red-ln{stroke:#eb5757}
.txt-sm{fill:#9b9a97}.txt-red{fill:#eb5757}.txt-stamp{fill:#3fb97a}.txt-mono{fill:#e6e5e3}.txt-stat{fill:#e6e5e3}
}
</style>"""

WOB_FILTER = """<defs>
<filter id="wob" x="-5%" y="-8%" width="110%" height="116%">
  <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="5" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/>
</filter>
</defs>"""

# 1. NoDues SVG
nodues_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 180" width="400" height="180" role="img" aria-labelledby="t">
<title id="t">NoDues clearance: animated checklist whose student approvals tick sequentially</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgG" width="400" height="180" rx="6"/>
<g filter="url(#wob)">
  <!-- Clipboard Backing -->
  <rect class="solid" x="96" y="24" width="208" height="138" rx="10" opacity="0.12"/>
  <rect class="ln paper" x="92" y="20" width="216" height="142" rx="8"/>
  <!-- Clip at top -->
  <rect class="solid" x="166" y="12" width="68" height="18" rx="4" opacity="0.85"/>
  <rect class="ln paper" x="178" y="16" width="44" height="10" rx="3"/>

  <!-- Row 1: Dept Library -->
  <rect class="ln" x="114" y="46" width="14" height="14" rx="3"/>
  <path class="green-ln" d="M117 53 L121 57 L127 49" stroke-dasharray="16" stroke-dashoffset="16">
    <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.12;0.22;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
  </path>
  <path class="ln" d="M138 53 H215"/>
  <path class="ln thin" d="M225 53 H250"/>

  <!-- Row 2: Lab Equipment -->
  <rect class="ln" x="114" y="70" width="14" height="14" rx="3"/>
  <path class="green-ln" d="M117 77 L121 81 L127 73" stroke-dasharray="16" stroke-dashoffset="16">
    <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.32;0.42;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
  </path>
  <path class="ln" d="M138 77 H235"/>
  <path class="ln thin" d="M245 77 H270"/>

  <!-- Row 3: Faculty Adviser -->
  <rect class="ln" x="114" y="94" width="14" height="14" rx="3"/>
  <path class="green-ln" d="M117 101 L121 105 L127 97" stroke-dasharray="16" stroke-dashoffset="16">
    <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.52;0.62;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
  </path>
  <path class="ln" d="M138 101 H205"/>
  <path class="ln thin" d="M215 101 H260"/>

  <!-- Clearance Progress bar -->
  <rect class="ln paper" x="114" y="126" width="172" height="14" rx="7"/>
  <rect class="fG" x="116" y="128" width="20" height="10" rx="5">
    <animate attributeName="width" values="20;60;115;168;168;20" keyTimes="0;0.25;0.45;0.65;0.88;0.98" dur="5.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1"/>
  </rect>

  <!-- Approved Stamp Banner popping in -->
  <g transform="translate(200, 78) rotate(-10)">
    <g>
      <rect class="paper" x="-5" y="-14" width="94" height="26" rx="4" stroke="#1a9d5a" stroke-width="2"/>
      <text class="txt-stamp" x="6" y="3">CLEARED ✓</text>
      <animateTransform attributeName="transform" type="scale" values="0;0;1.15;1.0;1.0;0" keyTimes="0;0.63;0.70;0.74;0.88;0.95" dur="5.5s" repeatCount="indefinite"/>
    </g>
  </g>

  <!-- Decorative stars -->
  <path class="ln thin" d="M54 42 V54 M48 48 H60"/>
  <path class="ln thin" d="M346 128 V138 M341 133 H351"/>
</g>
</svg>
"""

# 1B. NoDues Wide Bento SVG (Hero Card)
nodues_wide_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="880" height="200" role="img" aria-labelledby="t">
<title id="t">NoDues clearance: animated checklist and real-time SSE metrics dashboard</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgG" width="880" height="200" rx="8"/>
<g filter="url(#wob)">
  <!-- Left Half: Animated Checklist Clipboard -->
  <g transform="translate(45, 12)">
    <rect class="solid" x="54" y="16" width="220" height="152" rx="10" opacity="0.12"/>
    <rect class="ln paper" x="50" y="12" width="224" height="156" rx="8"/>
    <!-- Clip at top -->
    <rect class="solid" x="128" y="4" width="68" height="18" rx="4" opacity="0.85"/>
    <rect class="ln paper" x="140" y="8" width="44" height="10" rx="3"/>

    <!-- Row 1: Dept Library -->
    <rect class="ln" x="72" y="38" width="14" height="14" rx="3"/>
    <path class="green-ln" d="M75 45 L79 49 L85 41" stroke-dasharray="16" stroke-dashoffset="16">
      <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.12;0.22;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
    </path>
    <path class="ln" d="M96 45 H173"/>
    <path class="ln thin" d="M183 45 H208"/>

    <!-- Row 2: Lab Equipment -->
    <rect class="ln" x="72" y="62" width="14" height="14" rx="3"/>
    <path class="green-ln" d="M75 69 L79 73 L85 65" stroke-dasharray="16" stroke-dashoffset="16">
      <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.32;0.42;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
    </path>
    <path class="ln" d="M96 69 H193"/>
    <path class="ln thin" d="M203 69 H228"/>

    <!-- Row 3: Faculty Adviser -->
    <rect class="ln" x="72" y="86" width="14" height="14" rx="3"/>
    <path class="green-ln" d="M75 93 L79 97 L85 89" stroke-dasharray="16" stroke-dashoffset="16">
      <animate attributeName="stroke-dashoffset" values="16;16;0;0;16" keyTimes="0;0.52;0.62;0.88;0.96" dur="5.5s" repeatCount="indefinite"/>
    </path>
    <path class="ln" d="M96 93 H163"/>
    <path class="ln thin" d="M173 93 H218"/>

    <!-- Progress bar -->
    <rect class="ln paper" x="72" y="118" width="180" height="14" rx="7"/>
    <rect class="fG" x="74" y="120" width="20" height="10" rx="5">
      <animate attributeName="width" values="20;70;125;176;176;20" keyTimes="0;0.25;0.45;0.65;0.88;0.98" dur="5.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1"/>
    </rect>

    <!-- Cleared Stamp -->
    <g transform="translate(155, 70) rotate(-10)">
      <g>
        <rect class="paper" x="-5" y="-14" width="94" height="26" rx="4" stroke="#1a9d5a" stroke-width="2"/>
        <text class="txt-stamp" x="6" y="3">CLEARED ✓</text>
        <animateTransform attributeName="transform" type="scale" values="0;0;1.15;1.0;1.0;0" keyTimes="0;0.63;0.70;0.74;0.88;0.95" dur="5.5s" repeatCount="indefinite"/>
      </g>
    </g>
  </g>

  <!-- Divider line -->
  <path class="ln thin" d="M365 20 V180" stroke-dasharray="3 6"/>

  <!-- Right Half: Real-time Telemetry & Architecture Bento Boxes -->
  <g transform="translate(395, 16)">
    <!-- Box 1: Scale metric -->
    <g>
      <rect class="paper ln" x="0" y="0" width="210" height="70" rx="8"/>
      <rect class="fG" x="12" y="10" width="86" height="15" rx="3.5"/>
      <text class="txt-mono" x="18" y="21" style="font-size:8.5px;fill:#1a9d5a;font-weight:700;">● MITS LIVE</text>
      <text class="txt-stat" x="12" y="55">2,100+</text>
      <text class="txt-sm" x="108" y="44" style="font-size:10px;">Students<br/>Cleared Dues</text>
    </g>

    <!-- Box 2: Faculty Sign-offs -->
    <g transform="translate(225, 0)">
      <rect class="paper ln" x="0" y="0" width="210" height="70" rx="8"/>
      <rect class="fB" x="12" y="10" width="96" height="15" rx="3.5"/>
      <text class="txt-mono" x="18" y="21" style="font-size:8.5px;fill:#2383e2;font-weight:700;">SSE BROADCAST</text>
      <text class="txt-stat" x="12" y="55">30+</text>
      <text class="txt-sm" x="72" y="44" style="font-size:10px;">Faculty<br/>Live Approvals</text>
    </g>

    <!-- Box 3: Data Ingestion & Sync Pipeline (Wide bottom panel) -->
    <g transform="translate(0, 82)">
      <rect class="paper ln" x="0" y="0" width="435" height="86" rx="8"/>
      <!-- Animated pulse light -->
      <circle class="green" cx="20" cy="22" r="3.5">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle class="green-ln" cx="20" cy="22" r="8" opacity="0.6">
        <animate attributeName="r" values="3.5;12;12" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.8;0;0" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text class="txt-mono" x="36" y="25" style="font-size:10.5px;font-weight:700;">ZERO-POLLING SSE PIPELINE &amp; EXCEL FUZZY INGESTION</text>
      <path class="ln thin" d="M14 38 H421"/>
      <text class="txt-sm" x="14" y="54" style="font-size:9.5px;">• Multi-role authorization state transitions pushed over Server-Sent Events with zero lag</text>
      <text class="txt-sm" x="14" y="70" style="font-size:9.5px;">• Fuzzy string matching normalizes heterogeneous department faculty rosters &amp; schedules</text>
    </g>
  </g>
</g>
</svg>
"""

# 2. D'FESTA 2K26 SVG (Refined Notion ticket with scanning QR laser)
dfesta_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 180" width="400" height="180" role="img" aria-labelledby="t">
<title id="t">D'FESTA 2K26 ticketing: event pass with animated laser sweeping the QR code</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgP" width="400" height="180" rx="6"/>
<g filter="url(#wob)">
  <!-- Ticket Body with Perforations -->
  <path class="solid" d="M102 42 H302 a14 14 0 0 1 14 14 V74 a14 14 0 0 0 0 28 V128 a14 14 0 0 1 -14 14 H102 a14 14 0 0 1 -14 -14 V102 a14 14 0 0 0 0 -28 V56 a14 14 0 0 1 14 -14 Z" opacity="0.12"/>
  <path class="ln paper" d="M98 38 H298 a14 14 0 0 1 14 14 V70 a14 14 0 0 0 0 28 V124 a14 14 0 0 1 -14 14 H98 a14 14 0 0 1 -14 -14 V98 a14 14 0 0 0 0 -28 V52 a14 14 0 0 1 14 -14 Z"/>
  <path class="ln thin" d="M234 46 V128" stroke-dasharray="3 6"/>

  <!-- Left details -->
  <path class="ln" d="M112 66 H195"/>
  <path class="ln thin" d="M112 86 H175 M112 102 H155"/>
  <rect class="fP" x="112" y="116" width="70" height="14" rx="4"/>
  <text class="txt-sm" x="120" y="127">ENTRY PASS</text>

  <!-- Right: QR Matrix -->
  <rect class="solid" x="246" y="62" width="11" height="11" rx="2.5"/>
  <rect class="ln" x="246" y="78" width="11" height="11" rx="2.5"/>
  <rect class="solid" x="246" y="94" width="11" height="11" rx="2.5"/>
  <rect class="ln" x="262" y="62" width="11" height="11" rx="2.5"/>
  <rect class="solid" x="262" y="78" width="11" height="11" rx="2.5"/>
  <rect class="ln" x="262" y="94" width="11" height="11" rx="2.5"/>
  <rect class="solid" x="278" y="62" width="11" height="11" rx="2.5"/>
  <rect class="ln" x="278" y="78" width="11" height="11" rx="2.5"/>
  <rect class="solid" x="278" y="94" width="11" height="11" rx="2.5"/>

  <!-- Laser scanning beam -->
  <g>
    <path class="scan" d="M240 62 H294">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 46;0 0" keyTimes="0;0.5;1" dur="2.8s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
    </path>
    <!-- Laser glow dot -->
    <circle class="blue" cx="294" cy="62" r="3">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 46;0 0" keyTimes="0;0.5;1" dur="2.8s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
      <animate attributeName="opacity" values="0.8;1;0.8" dur="1.4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Decorative hand-drawn crosses -->
  <path class="ln thin" d="M64 36 V46 M59 41 H69"/>
  <path class="ln thin" d="M336 142 V154 M330 148 H342"/>
</g>
</svg>
"""

# 3. BizEasy SVG (WhatsApp commerce state machine)
bizeasy_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 180" width="400" height="180" role="img" aria-labelledby="t">
<title id="t">BizEasy: WhatsApp-first commerce platform with real-time order state machine</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgB" width="400" height="180" rx="6"/>
<g filter="url(#wob)">
  <!-- Mobile/Chat Shell -->
  <rect class="solid" x="90" y="20" width="224" height="142" rx="12" opacity="0.12"/>
  <rect class="ln paper" x="86" y="16" width="228" height="144" rx="10"/>

  <!-- WhatsApp Header Bar -->
  <path class="ln thin" d="M86 42 H314"/>
  <circle class="green" cx="106" cy="29" r="6"/>
  <circle class="paper" cx="106" cy="29" r="2.5"/>
  <path class="ln" d="M120 29 H190"/>
  <!-- Status dot -->
  <circle class="green" cx="292" cy="29" r="3.5">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
  </circle>

  <!-- Incoming Customer Message Bubble -->
  <g>
    <rect class="ln fB" x="100" y="52" width="138" height="28" rx="8"/>
    <path class="ln" d="M112 63 H195"/>
    <path class="ln thin" d="M112 71 H165"/>
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.05;0.12;0.88;0.95;1" dur="6s" repeatCount="indefinite"/>
  </g>

  <!-- Bot State Machine Reply Bubble -->
  <g>
    <rect class="ln paper" x="162" y="86" width="140" height="34" rx="8"/>
    <path class="ln" d="M174 97 H275"/>
    <!-- Razorpay Pay Link Pill -->
    <rect class="fG" x="174" y="103" width="76" height="12" rx="3"/>
    <text class="txt-sm" x="180" y="112" fill="#1a9d5a">PAY ₹650 ↗</text>
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.34;0.88;0.95;1" dur="6s" repeatCount="indefinite"/>
  </g>

  <!-- Live Payment Reconciled Event -->
  <g>
    <rect class="solid" x="110" y="128" width="180" height="22" rx="5" fill="#1a9d5a" opacity="0.95"/>
    <text class="txt-stamp" x="122" y="143" fill="#ffffff" font-size="10px">WEBHOOK: PAID ✓  [ID #842]</text>
    <animateTransform attributeName="transform" type="translate" values="0 10;0 0;0 0;0 10" keyTimes="0;0.52;0.88;0.96" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.48;0.56;0.88;0.96;1" dur="6s" repeatCount="indefinite"/>
  </g>

  <!-- Decorative stars -->
  <path class="ln thin" d="M52 38 V48 M47 43 H57"/>
  <path class="ln thin" d="M344 126 V136 M339 131 H349"/>
</g>
</svg>
"""

# 4. NCC Exam Portal SVG (Server-enforced timer & exam sheet)
ncc_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 180" width="400" height="180" role="img" aria-labelledby="t">
<title id="t">NCC Exam Portal: timed examination sheet with server-synchronized clock and RBAC isolation</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgY" width="400" height="180" rx="6"/>
<g filter="url(#wob)">
  <!-- Exam Paper Base -->
  <rect class="solid" x="84" y="22" width="234" height="142" rx="8" opacity="0.12"/>
  <rect class="ln paper" x="80" y="18" width="238" height="144" rx="8"/>

  <!-- Exam Header -->
  <rect class="fY" x="96" y="30" width="86" height="16" rx="4"/>
  <text class="txt-sm" x="103" y="42">NCC TIRUPATI</text>

  <!-- Animated Countdown Clock at top right -->
  <g transform="translate(270, 38)">
    <circle class="ln paper" cx="0" cy="0" r="14"/>
    <circle class="solid" cx="0" cy="0" r="2"/>
    <!-- Hour Hand -->
    <line class="ln" x1="0" y1="0" x2="0" y2="-6"/>
    <!-- Minute Hand Rotating -->
    <line class="ln thin" x1="0" y1="0" x2="0" y2="-10">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
    </line>
    <!-- Server-locked tag -->
    <circle class="green" cx="18" cy="-6" r="3">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="1.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <path class="ln thin" d="M96 56 H298"/>

  <!-- Question 04 block -->
  <rect class="ln" x="96" y="66" width="206" height="66" rx="6"/>
  <path class="ln" d="M108 78 H260"/>
  <path class="ln thin" d="M108 88 H210"/>

  <!-- Option A -->
  <circle class="ln" cx="116" cy="104" r="5"/>
  <path class="ln thin" d="M128 104 H195"/>

  <!-- Option B: Selects dynamically -->
  <circle class="ln" cx="116" cy="120" r="5"/>
  <circle class="green" cx="116" cy="120" r="0">
    <animate attributeName="r" values="0;0;3.2;3.2;0" keyTimes="0;0.3;0.38;0.88;0.96" dur="5s" repeatCount="indefinite"/>
  </circle>
  <path class="ln thin" d="M128 120 H225"/>

  <!-- Server Lock indicator at bottom -->
  <g transform="translate(96, 144)">
    <!-- Small Padlock -->
    <rect class="solid" x="0" y="4" width="10" height="8" rx="1.5"/>
    <path class="ln thin" d="M2 4 V1.5 a3 3 0 0 1 6 0 V4"/>
    <text class="txt-sm" x="14" y="11" font-size="9px">SERVER TIMING · CLOCK SECURED</text>
  </g>

  <!-- Decorative hand-drawn pluses -->
  <path class="ln thin" d="M48 40 V50 M43 45 H53"/>
  <path class="ln thin" d="M350 134 V144 M345 139 H355"/>
</g>
</svg>
"""

# 4B. NCC Exam Portal Wide Bento SVG (Anchor Card)
ncc_wide_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="880" height="200" role="img" aria-labelledby="t">
<title id="t">NCC Exam Portal: timed examination sheet with server-synchronized clock and RBAC isolation</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgY" width="880" height="200" rx="8"/>
<g filter="url(#wob)">
  <!-- Left Half: Exam Paper with Ticking Clock & Dynamic Answer Selection -->
  <g transform="translate(45, 12)">
    <rect class="solid" x="54" y="16" width="260" height="152" rx="8" opacity="0.12"/>
    <rect class="ln paper" x="50" y="12" width="264" height="156" rx="8"/>

    <!-- Exam Header -->
    <rect class="fY" x="66" y="24" width="94" height="16" rx="4"/>
    <text class="txt-sm" x="72" y="36">NCC TIRUPATI</text>

    <!-- Animated Countdown Clock at top right -->
    <g transform="translate(280, 32)">
      <circle class="ln paper" cx="0" cy="0" r="14"/>
      <circle class="solid" cx="0" cy="0" r="2"/>
      <line class="ln" x1="0" y1="0" x2="0" y2="-6"/>
      <line class="ln thin" x1="0" y1="0" x2="0" y2="-10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
      </line>
      <circle class="green" cx="18" cy="-6" r="3">
        <animate attributeName="opacity" values="0.3;1;0.3" dur="1.5s" repeatCount="indefinite"/>
      </circle>
    </g>

    <path class="ln thin" d="M66 50 H298"/>

    <!-- Question block -->
    <rect class="ln" x="66" y="60" width="232" height="74" rx="6"/>
    <path class="ln" d="M78 72 H260"/>
    <path class="ln thin" d="M78 82 H210"/>

    <!-- Option A -->
    <circle class="ln" cx="86" cy="98" r="5"/>
    <path class="ln thin" d="M98 98 H185"/>

    <!-- Option B: Selects dynamically -->
    <circle class="ln" cx="86" cy="116" r="5"/>
    <circle class="green" cx="86" cy="116" r="0">
      <animate attributeName="r" values="0;0;3.2;3.2;0" keyTimes="0;0.3;0.38;0.88;0.96" dur="5s" repeatCount="indefinite"/>
    </circle>
    <path class="ln thin" d="M98 116 H245"/>

    <!-- Server Locked Badge -->
    <g transform="translate(66, 144)">
      <rect class="fG" x="0" y="0" width="154" height="16" rx="4"/>
      <text class="txt-stamp" x="12" y="11.5" style="font-size:9.5px;">✓ SUBMISSION LOCKED</text>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.48;0.56;0.88;0.96;1" dur="5s" repeatCount="indefinite"/>
    </g>
  </g>

  <!-- Divider line -->
  <path class="ln thin" d="M365 20 V180" stroke-dasharray="3 6"/>

  <!-- Right Half: Security & Multi-Role Architecture Telemetry -->
  <g transform="translate(395, 16)">
    <!-- Box 1: RBAC Middleware -->
    <g>
      <rect class="paper ln" x="0" y="0" width="210" height="70" rx="8"/>
      <rect class="fY" x="12" y="10" width="108" height="15" rx="3.5"/>
      <text class="txt-mono" x="18" y="21" style="font-size:8.5px;fill:#b45309;font-weight:700;">TENANT ISOLATION</text>
      <text class="txt-stat" x="12" y="55">3 Roles</text>
      <text class="txt-sm" x="100" y="44" style="font-size:10px;">Admin • Officer<br/>Cadet RBAC</text>
    </g>

    <!-- Box 2: Clock Tamper Protection -->
    <g transform="translate(225, 0)">
      <rect class="paper ln" x="0" y="0" width="210" height="70" rx="8"/>
      <rect class="fG" x="12" y="10" width="112" height="15" rx="3.5"/>
      <text class="txt-mono" x="18" y="21" style="font-size:8.5px;fill:#1a9d5a;font-weight:700;">AUTHORITATIVE</text>
      <text class="txt-stat" x="12" y="55">0 Offset</text>
      <text class="txt-sm" x="104" y="44" style="font-size:10px;">Server-Enforced<br/>Deadline Sync</text>
    </g>

    <!-- Box 3: Defense Security Engine Panel -->
    <g transform="translate(0, 82)">
      <rect class="paper ln" x="0" y="0" width="435" height="86" rx="8"/>
      <circle class="green" cx="20" cy="22" r="3.5">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text class="txt-mono" x="36" y="25" style="font-size:10.5px;font-weight:700;">PRISMA MIDDLEWARE MULTI-TENANCY &amp; CRYPTOGRAPHIC AUDITING</text>
      <path class="ln thin" d="M14 38 H421"/>
      <text class="txt-sm" x="14" y="54" style="font-size:9.5px;">• Queries automatically scoped to active unit battalion ID at the ORM layer</text>
      <text class="txt-sm" x="14" y="70" style="font-size:9.5px;">• Client timestamp manipulation impossible: server calculates and enforces expiration</text>
    </g>
  </g>
</g>
</svg>
"""

# 5. HireMinds AI SVG (Autonomous interviewer with critic layer)
hireminds_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 180" width="400" height="180" role="img" aria-labelledby="t">
<title id="t">HireMinds AI: autonomous technical interviewer with agent loop, candidate assessment and filling score bar</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgO" width="400" height="180" rx="6"/>
<g filter="url(#wob)">
  <!-- Interviewer Bubble with Question Mark -->
  <g>
    <path class="solid" d="M96 32 H198 a12 12 0 0 1 12 12 V60 a12 12 0 0 1 -12 12 H114 L98 86 V72 H96 a12 12 0 0 1 -12 -12 V44 a12 12 0 0 1 12 -12 Z" opacity="0.12"/>
    <path class="ln fO" d="M92 28 H194 a12 12 0 0 1 12 12 V56 a12 12 0 0 1 -12 12 H110 L94 82 V68 H92 a12 12 0 0 1 -12 -12 V40 a12 12 0 0 1 12 -12 Z"/>
    <!-- Icon/Avatar question mark -->
    <text class="txt-stamp" x="104" y="52" fill="#37352f" font-size="16px">AI?</text>
    <path class="ln thin" d="M140 48 H190 M140 58 H175"/>
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.04;0.09;0.90;0.96;1" dur="7s" repeatCount="indefinite"/>
  </g>

  <!-- Candidate Answer Audio/Text Card -->
  <g>
    <rect class="solid" x="194" y="86" width="134" height="42" rx="12" opacity="0.12"/>
    <rect class="ln fB" x="190" y="82" width="134" height="42" rx="12"/>
    <path class="ln thin" d="M204 97 H302 M204 110 H268"/>
    <!-- Voice wave ripples -->
    <path class="ln" d="M280 110 V102 M286 114 V98 M292 110 V102 M298 108 V104" stroke="#2383e2"/>
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.26;0.32;0.90;0.96;1" dur="7s" repeatCount="indefinite"/>
  </g>

  <!-- Critic Evaluation Engine Score Bar -->
  <g>
    <rect class="ln paper" x="92" y="142" width="216" height="16" rx="8"/>
    <rect class="fG" x="94" y="144" width="20" height="12" rx="6">
      <animate attributeName="width" values="20;50;130;190;190;20" keyTimes="0;0.32;0.50;0.72;0.90;0.98" dur="7s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1"/>
    </rect>
    <text class="txt-sm" x="314" y="154">94% SCORE</text>
  </g>

  <!-- Decorative hand-drawn pluses -->
  <path class="ln thin" d="M344 36 V48 M338 42 H350"/>
  <path class="ln thin" d="M60 120 V130 M55 125 H65"/>
</g>
</svg>
"""

# 6. LifeLink SVG (Emergency medical dispatch platform with live GPS tracking)
lifelink_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 180" width="400" height="180" role="img" aria-labelledby="t">
<title id="t">LifeLink: emergency medical dispatch platform with live GPS ambulance routing and hospital status</title>
{COMMON_STYLES}
{WOB_FILTER}
<rect class="bgR" width="400" height="180" rx="6"/>
<g filter="url(#wob)">
  <!-- Dispatch Card Sheet -->
  <rect class="solid" x="74" y="20" width="254" height="142" rx="8" opacity="0.12"/>
  <rect class="ln paper" x="70" y="16" width="258" height="144" rx="8"/>

  <!-- Top Dispatch Status Bar -->
  <rect class="fR" x="84" y="28" width="94" height="18" rx="4"/>
  <circle class="red" cx="95" cy="37" r="3.2">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.4s" repeatCount="indefinite"/>
  </circle>
  <text class="txt-red" x="105" y="41">SOS DISPATCH</text>

  <rect class="fY" x="184" y="28" width="130" height="18" rx="4"/>
  <text class="txt-sm" x="194" y="41" fill="#b45309">★ 1ST PLACE WINNER</text>

  <!-- Route Map Grid Lines -->
  <path class="ln thin" d="M84 72 H314 M84 102 H314 M84 132 H314" stroke-dasharray="2 4" opacity="0.5"/>
  <path class="ln thin" d="M130 54 V136 M190 54 V136 M250 54 V136 M300 54 V136" stroke-dasharray="2 4" opacity="0.5"/>

  <!-- Dispatch Route Path from Patient (x=105, y=118) to Hospital (x=285, y=85) -->
  <path class="blue-ln" d="M105 118 L160 118 L190 85 L285 85" stroke-dasharray="6 4" opacity="0.6"/>

  <!-- Animated Active Ambulance Route Progression -->
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

  <!-- Animated Moving Ambulance Vehicle -->
  <g>
    <animateMotion path="M105 118 L160 118 L190 85 L285 85" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1" keyTimes="0;0.55;0.85;1">
      <mpath/>
    </animateMotion>
    <!-- Ambulance Icon -->
    <rect class="ln paper" x="-10" y="-12" width="20" height="12" rx="3"/>
    <rect class="red" x="-2" y="-10" width="4" height="8"/>
    <rect class="red" x="-4" y="-8" width="8" height="4"/>
    <circle class="solid" cx="-5" cy="0" r="2"/>
    <circle class="solid" cx="5" cy="0" r="2"/>
  </g>

  <!-- Hospital Station Node with Medical Cross -->
  <g transform="translate(285, 85)">
    <rect class="ln paper" x="-13" y="-13" width="26" height="26" rx="5"/>
    <!-- Medical Cross -->
    <rect class="red" x="-2" y="-8" width="4" height="16" rx="1"/>
    <rect class="red" x="-8" y="-2" width="16" height="4" rx="1"/>
    <!-- Radar ping around hospital -->
    <circle class="blue-ln" cx="0" cy="0" r="14">
      <animate attributeName="r" values="14;22;22" dur="2.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0" dur="2.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Real-time Status Footer -->
  <g transform="translate(84, 142)">
    <rect class="fG" x="0" y="0" width="230" height="16" rx="4"/>
    <circle class="green" cx="10" cy="8" r="3"/>
    <text class="txt-mono" x="20" y="11.5">AMBULANCE EN ROUTE · ETA 3 MIN</text>
  </g>

  <!-- Decorative hand-drawn pluses -->
  <path class="ln thin" d="M42 36 V46 M37 41 H47"/>
  <path class="ln thin" d="M356 124 V134 M351 129 H361"/>
</g>
</svg>
"""

# Write all 6 SVGs to assets/
assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
files = {
    "work-nodues.svg": nodues_svg,
    "work-nodues-wide.svg": nodues_wide_svg,
    "work-dfesta.svg": dfesta_svg,
    "work-bizeasy.svg": bizeasy_svg,
    "work-ncc.svg": ncc_svg,
    "work-ncc-wide.svg": ncc_wide_svg,
    "work-hireminds.svg": hireminds_svg,
    "work-lifelink.svg": lifelink_svg,
}

for filename, content in files.items():
    filepath = os.path.join(assets_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated {filename} ({len(content)} bytes)")

print("All Notion-style animated SVGs successfully generated!")
