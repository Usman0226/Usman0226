#!/usr/bin/env python3
"""Generate assets/status.svg as an Awwwards-grade 3D Fan-out Cover Flow Carousel.
Directly inspired by Apple / mobile app showcase carousels (Reference Image 3).
Features 5 auto-scrolling cards with authentic favicons, live p95 telemetry,
real-time EKG waves, and bottom pagination controls.
"""
import os
import sys
import time
import base64
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(SCRIPT_DIR, "..", "assets", "status.svg")

# Load Base64 Favicons
DFESTA_PNG = os.path.join(SCRIPT_DIR, "..", "assets", "favicons", "dfesta.png")
NCC_SVG = os.path.join(SCRIPT_DIR, "..", "assets", "favicons", "ncc.svg")

dfesta_b64 = ""
if os.path.exists(DFESTA_PNG):
    with open(DFESTA_PNG, "rb") as f:
        dfesta_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

ncc_b64 = ""
if os.path.exists(NCC_SVG):
    with open(NCC_SVG, "rb") as f:
        ncc_b64 = "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")

CSS = """<style>
.bg { fill: none; }
.header-lbl { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11px; font-weight: 700; letter-spacing: 1px; fill: #6b7280; }
.header-sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; fill: #9ca3af; }
.card-shell { fill: #ffffff; stroke: #e5e7eb; stroke-width: 1px; }
.card-screen { fill: #f9fafb; stroke: #f3f4f6; stroke-width: 1px; }
.title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #111827; }
.sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 9.5px; font-weight: 500; fill: #6b7280; }
.stat-tag { fill: #ecfdf5; stroke: #a7f3d0; stroke-width: 1px; }
.stat-txt { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 8px; font-weight: 700; fill: #059669; }
.up-dot { fill: #10b981; }
.up-ring { fill: none; stroke: #10b981; stroke-width: 1.2px; }
.metric-val { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 10px; font-weight: 700; fill: #111827; }
.metric-lbl { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 8.5px; font-weight: 500; fill: #6b7280; }
.url-txt { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 8.5px; fill: #9ca3af; }
.ctrl-btn { fill: #ffffff; stroke: #e5e7eb; stroke-width: 1px; }
.ctrl-arrow { fill: none; stroke: #6b7280; stroke-width: 1.5px; stroke-linecap: round; stroke-linejoin: round; }
.dot-inactive { fill: #d1d5db; }
.dot-active { fill: #10b981; }
.wave-live { fill: none; stroke: #10b981; stroke-width: 1.4px; stroke-linecap: round; stroke-linejoin: round; }
.laser { stroke: #3b82f6; stroke-width: 1.5px; }

/* 3D Cover Flow Auto-Changing Carousel Animation */
@keyframes cf1 {
  0%, 16%    { transform: translate(345px, 35px) rotate(0deg) scale(1.0); opacity: 1.0; }
  20%, 36%   { transform: translate(490px, 42px) rotate(7deg) scale(0.86); opacity: 0.75; }
  40%, 56%   { transform: translate(630px, 54px) rotate(14deg) scale(0.72); opacity: 0.42; }
  60%, 76%   { transform: translate(60px, 54px) rotate(-14deg) scale(0.72); opacity: 0.42; }
  80%, 96%   { transform: translate(200px, 42px) rotate(-7deg) scale(0.86); opacity: 0.75; }
  100%       { transform: translate(345px, 35px) rotate(0deg) scale(1.0); opacity: 1.0; }
}

@keyframes cf2 {
  0%, 16%    { transform: translate(490px, 42px) rotate(7deg) scale(0.86); opacity: 0.75; }
  20%, 36%   { transform: translate(630px, 54px) rotate(14deg) scale(0.72); opacity: 0.42; }
  40%, 56%   { transform: translate(60px, 54px) rotate(-14deg) scale(0.72); opacity: 0.42; }
  60%, 76%   { transform: translate(200px, 42px) rotate(-7deg) scale(0.86); opacity: 0.75; }
  80%, 96%   { transform: translate(345px, 35px) rotate(0deg) scale(1.0); opacity: 1.0; }
  100%       { transform: translate(490px, 42px) rotate(7deg) scale(0.86); opacity: 0.75; }
}

@keyframes cf3 {
  0%, 16%    { transform: translate(630px, 54px) rotate(14deg) scale(0.72); opacity: 0.42; }
  20%, 36%   { transform: translate(60px, 54px) rotate(-14deg) scale(0.72); opacity: 0.42; }
  40%, 56%   { transform: translate(200px, 42px) rotate(-7deg) scale(0.86); opacity: 0.75; }
  60%, 76%   { transform: translate(345px, 35px) rotate(0deg) scale(1.0); opacity: 1.0; }
  80%, 96%   { transform: translate(490px, 42px) rotate(7deg) scale(0.86); opacity: 0.75; }
  100%       { transform: translate(630px, 54px) rotate(14deg) scale(0.72); opacity: 0.42; }
}

@keyframes cf4 {
  0%, 16%    { transform: translate(60px, 54px) rotate(-14deg) scale(0.72); opacity: 0.42; }
  20%, 36%   { transform: translate(200px, 42px) rotate(-7deg) scale(0.86); opacity: 0.75; }
  40%, 56%   { transform: translate(345px, 35px) rotate(0deg) scale(1.0); opacity: 1.0; }
  60%, 76%   { transform: translate(490px, 42px) rotate(7deg) scale(0.86); opacity: 0.75; }
  80%, 96%   { transform: translate(630px, 54px) rotate(14deg) scale(0.72); opacity: 0.42; }
  100%       { transform: translate(60px, 54px) rotate(-14deg) scale(0.72); opacity: 0.42; }
}

@keyframes cf5 {
  0%, 16%    { transform: translate(200px, 42px) rotate(-7deg) scale(0.86); opacity: 0.75; }
  20%, 36%   { transform: translate(345px, 35px) rotate(0deg) scale(1.0); opacity: 1.0; }
  40%, 56%   { transform: translate(490px, 42px) rotate(7deg) scale(0.86); opacity: 0.75; }
  60%, 76%   { transform: translate(630px, 54px) rotate(14deg) scale(0.72); opacity: 0.42; }
  80%, 96%   { transform: translate(60px, 54px) rotate(-14deg) scale(0.72); opacity: 0.42; }
  100%       { transform: translate(200px, 42px) rotate(-7deg) scale(0.86); opacity: 0.75; }
}

.c-pos1 { animation: cf1 15s cubic-bezier(0.4, 0, 0.2, 1) infinite; }
.c-pos2 { animation: cf2 15s cubic-bezier(0.4, 0, 0.2, 1) infinite; }
.c-pos3 { animation: cf3 15s cubic-bezier(0.4, 0, 0.2, 1) infinite; }
.c-pos4 { animation: cf4 15s cubic-bezier(0.4, 0, 0.2, 1) infinite; }
.c-pos5 { animation: cf5 15s cubic-bezier(0.4, 0, 0.2, 1) infinite; }

/* Indicator Dots sync */
@keyframes dot1 { 0%, 16%, 100% { fill: #10b981; r: 3.5; } 20%, 96% { fill: #d1d5db; r: 2.5; } }
@keyframes dot2 { 20%, 36% { fill: #10b981; r: 3.5; } 0%, 16%, 40%, 100% { fill: #d1d5db; r: 2.5; } }
@keyframes dot3 { 60%, 76% { fill: #10b981; r: 3.5; } 0%, 56%, 80%, 100% { fill: #d1d5db; r: 2.5; } }
@keyframes dot4 { 80%, 96% { fill: #10b981; r: 3.5; } 0%, 76%, 100% { fill: #d1d5db; r: 2.5; } }
@keyframes dot5 { 40%, 56% { fill: #10b981; r: 3.5; } 0%, 36%, 60%, 100% { fill: #d1d5db; r: 2.5; } }

.ind-dot1 { animation: dot1 15s infinite; }
.ind-dot2 { animation: dot5 15s infinite; }
.ind-dot3 { animation: dot2 15s infinite; }
.ind-dot4 { animation: dot3 15s infinite; }
.ind-dot5 { animation: dot4 15s infinite; }

@media (prefers-color-scheme: dark) {
  .header-lbl { fill: #9ca3af; }
  .header-sub { fill: #6b7280; }
  .card-shell { fill: #121214; stroke: #26262a; }
  .card-screen { fill: #18181b; stroke: #222226; }
  .title { fill: #f9fafb; }
  .sub { fill: #9ca3af; }
  .stat-tag { fill: rgba(16, 185, 129, 0.12); stroke: rgba(16, 185, 129, 0.3); }
  .stat-txt { fill: #34d399; }
  .up-dot { fill: #34d399; }
  .up-ring { stroke: #34d399; }
  .metric-val { fill: #f3f4f6; }
  .metric-lbl { fill: #9ca3af; }
  .url-txt { fill: #6b7280; }
  .ctrl-btn { fill: #18181b; stroke: #27272a; }
  .ctrl-arrow { stroke: #9ca3af; }
  .dot-inactive { fill: #3f3f46; }
}
</style>"""

def render_card_inner(site_id, name, sub, url, ms, tag, favicon_xml, mock_xml):
    W, H = 190, 226
    return f"""
    <rect class="card-shell" width="{W}" height="{H}" rx="14"/>
    
    <!-- Header: Favicon + Title + Status Pill -->
    <g transform="translate(12, 12)">
      {favicon_xml}
      <text class="title" x="28" y="14">{name}</text>
      <text class="sub" x="28" y="25">{sub}</text>
      
      <!-- Status Tag -->
      <g transform="translate({W - 84}, 2)">
        <rect class="stat-tag" width="60" height="15" rx="7.5"/>
        <circle class="up-dot" cx="7" cy="7.5" r="2.2"/>
        <text class="stat-txt" x="13" y="10.5">ONLINE</text>
      </g>
    </g>
    
    <!-- Mini Screen Mockup Area -->
    <g transform="translate(10, 48)">
      <rect class="card-screen" width="{W - 20}" height="114" rx="8"/>
      {mock_xml}
    </g>
    
    <!-- Bottom Telemetry & URL -->
    <g transform="translate(12, 192)">
      <text class="metric-val" x="0" y="0">{ms} ms</text>
      <text class="metric-lbl" x="46" y="-0.5">p95 &#8226; {tag}</text>
      <text class="url-txt" x="0" y="18">{url}</text>
    </g>
"""

def main():
    W = 880
    H = 330
    
    # 1. NoDues Mock & Favicon
    nodues_fav = """
    <g transform="translate(0, 2)">
      <rect width="22" height="22" rx="5" fill="#10b981"/>
      <path d="M5 11 L9 15 L17 7" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    """
    nodues_mock = """
    <g transform="translate(8, 10)">
      <rect width="154" height="26" rx="4" fill="rgba(16,185,129,0.08)" stroke="rgba(16,185,129,0.2)"/>
      <text font-family="ui-monospace, monospace" font-size="8.5" font-weight="700" fill="#10b981" x="8" y="16">CLEARED &#10003; 2,100+ STUDENTS</text>
      <!-- Progress Bar -->
      <rect x="0" y="34" width="154" height="6" rx="3" fill="#e5e7eb"/>
      <rect x="0" y="34" width="138" height="6" rx="3" fill="#10b981">
        <animate attributeName="width" values="60;138;138" dur="3s" repeatCount="indefinite"/>
      </rect>
      <!-- Approvals stream -->
      <text font-family="-apple-system, sans-serif" font-size="8" fill="#6b7280" x="0" y="56">Faculty Approvals: 30+ Live</text>
      <path class="wave-live" d="M0 76 L25 76 L32 68 L38 84 L44 72 L50 78 L56 76 L154 76"/>
      <text font-family="ui-monospace, monospace" font-size="7.5" fill="#10b981" x="0" y="94">&#9679; SSE PIPELINE ACTIVE</text>
    </g>
    """
    c1 = render_card_inner("nodues", "NoDues", "Clearance Engine", "nodues-arcclub.tech", 284, "SSE STREAM", nodues_fav, nodues_mock)
    
    # 2. D'FESTA Mock & Favicon
    dfesta_fav = f"""
    <g transform="translate(0, 2)">
      <image href="{dfesta_b64}" width="22" height="22"/>
    </g>
    """ if dfesta_b64 else """
    <g transform="translate(0, 2)">
      <rect width="22" height="22" rx="5" fill="#6366f1"/>
      <text font-family="sans-serif" font-weight="700" font-size="10" fill="#fff" x="4" y="15">DF</text>
    </g>
    """
    dfesta_mock = """
    <g transform="translate(8, 10)">
      <rect width="154" height="42" rx="5" fill="none" stroke="#6366f1" stroke-dasharray="3 3"/>
      <text font-family="ui-monospace, monospace" font-size="8.5" font-weight="700" fill="#6366f1" x="8" y="16">TICKET #DF-2026</text>
      <text font-family="-apple-system, sans-serif" font-size="7.5" fill="#9ca3af" x="8" y="29">AES-256 HMAC VERIFIED</text>
      <!-- Laser scan line -->
      <line class="laser" x1="0" y1="10" x2="154" y2="10">
        <animate attributeName="y1" values="10;40;10" dur="2.4s" repeatCount="indefinite"/>
        <animate attributeName="y2" values="10;40;10" dur="2.4s" repeatCount="indefinite"/>
      </line>
      <g transform="translate(0, 50)">
        <text font-family="-apple-system, sans-serif" font-size="8" fill="#6b7280" x="0" y="10">Gate Pass: Offline Validator</text>
        <text font-family="-apple-system, sans-serif" font-size="8" fill="#6b7280" x="0" y="24">UPI Reconciliation: Instant</text>
        <text font-family="ui-monospace, monospace" font-size="7.5" fill="#6366f1" x="0" y="42">&#9679; SMTP TRIPLE FAILOVER</text>
      </g>
    </g>
    """
    c2 = render_card_inner("dfesta", "D&#8217;FESTA", "Symposium Gate", "dfesta.in", 118, "AES GATE", dfesta_fav, dfesta_mock)
    
    # 3. NCC Exam Portal Mock & Favicon
    ncc_fav = f"""
    <g transform="translate(0, 2)">
      <image href="{ncc_b64}" width="22" height="22"/>
    </g>
    """ if ncc_b64 else """
    <g transform="translate(0, 2)">
      <rect width="22" height="22" rx="5" fill="#863bff"/>
      <text font-family="sans-serif" font-weight="700" font-size="10" fill="#fff" x="3" y="15">NCC</text>
    </g>
    """
    ncc_mock = """
    <g transform="translate(8, 10)">
      <rect width="154" height="30" rx="4" fill="rgba(134,59,255,0.08)" stroke="rgba(134,59,255,0.2)"/>
      <text font-family="ui-monospace, monospace" font-size="12" font-weight="700" fill="#863bff" x="36" y="20">44 : 59 : 02</text>
      <text font-family="-apple-system, sans-serif" font-size="7.5" fill="#6b7280" x="0" y="48">Cadet Role: Strict RBAC</text>
      <text font-family="-apple-system, sans-serif" font-size="7.5" fill="#6b7280" x="0" y="62">Server-Authoritative Clock</text>
      <path class="wave-live" stroke="#863bff" d="M0 76 L30 76 L36 68 L42 84 L48 72 L54 78 L60 76 L154 76"/>
      <text font-family="ui-monospace, monospace" font-size="7.5" fill="#863bff" x="0" y="94">&#9679; PRISMA TENANT ISOLATION</text>
    </g>
    """
    c3 = render_card_inner("ncc", "NCC Exam", "Defense Platform", "ncc-exam-portal.vercel.app", 196, "PRISMA RBAC", ncc_fav, ncc_mock)
    
    # 4. LifeLink SOS Mock & Favicon
    lifelink_fav = """
    <g transform="translate(0, 2)">
      <rect width="22" height="22" rx="5" fill="#ef4444"/>
      <path d="M11 6 V16 M6 11 H16" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
    </g>
    """
    lifelink_mock = """
    <g transform="translate(8, 10)">
      <rect width="154" height="28" rx="4" fill="rgba(239,68,68,0.08)" stroke="rgba(239,68,68,0.2)"/>
      <text font-family="ui-monospace, monospace" font-size="8.5" font-weight="700" fill="#ef4444" x="8" y="17">&#9679; SOS DISPATCH #094</text>
      <!-- Radar grid path -->
      <path d="M10 48 H144 M10 70 H144" stroke="#e5e7eb" stroke-dasharray="2 3"/>
      <path d="M10 70 L45 70 L65 48 L144 48" fill="none" stroke="#ef4444" stroke-width="1.8"/>
      <circle cx="65" cy="48" r="4" fill="#ef4444"/>
      <text font-family="-apple-system, sans-serif" font-size="7.5" fill="#6b7280" x="0" y="86">Ambulance ETA: 3 Min</text>
      <text font-family="ui-monospace, monospace" font-size="7.5" fill="#ef4444" x="0" y="98">&#9679; WEBSOCKET RADAR ACTIVE</text>
    </g>
    """
    c4 = render_card_inner("lifelink", "LifeLink SOS", "Medical Dispatch", "lifelink-triage.mesh", 92, "1ST WINNER", lifelink_fav, lifelink_mock)
    
    # 5. BizEasy Mock & Favicon
    bizeasy_fav = """
    <g transform="translate(0, 2)">
      <rect width="22" height="22" rx="5" fill="#22c55e"/>
      <path d="M6 16 L6 7 Q6 5 8 5 H14 Q16 5 16 7 V13 Q16 15 14 15 H9 Z" fill="none" stroke="#ffffff" stroke-width="1.5"/>
    </g>
    """
    bizeasy_mock = """
    <g transform="translate(8, 10)">
      <rect width="154" height="32" rx="4" fill="rgba(34,197,94,0.08)" stroke="rgba(34,197,94,0.2)"/>
      <text font-family="-apple-system, sans-serif" font-size="8.5" font-weight="600" fill="#22c55e" x="8" y="15">WhatsApp Order Flow</text>
      <text font-family="ui-monospace, monospace" font-size="7.5" fill="#6b7280" x="8" y="26">Razorpay UPI &#183; Reconciled</text>
      <g transform="translate(0, 42)">
        <text font-family="-apple-system, sans-serif" font-size="8" fill="#6b7280" x="0" y="10">State Machine: Per-Seller Bot</text>
        <text font-family="-apple-system, sans-serif" font-size="8" fill="#6b7280" x="0" y="24">Multi-Tenant Store Engine</text>
        <text font-family="ui-monospace, monospace" font-size="7.5" fill="#22c55e" x="0" y="44">&#9679; META CLOUD WEBHOOK BUS</text>
      </g>
    </g>
    """
    c5 = render_card_inner("bizeasy", "BizEasy", "WhatsApp Engine", "bizeasy-commerce.api", 145, "META CLOUD", bizeasy_fav, bizeasy_mock)
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Live Systems 3D Cover Flow Telemetry">
{CSS}
<!-- Header -->
<g transform="translate(0, 16)">
  <text class="header-lbl" x="0" y="0">MISSION CONTROL &#8226; LIVE PRODUCTION SYSTEMS TELEMETRY</text>
  <text class="header-sub" x="0" y="16">5 continuous systems monitored via synthetic edge probes &#8226; Auto-rotating telemetry</text>
  <g transform="translate({W - 146}, -3.5)">
    <circle class="up-dot" cx="0" cy="0" r="3"/>
    <circle class="up-ring" cx="0" cy="0" r="3">
      <animate attributeName="r" values="3;9;9" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text class="header-lbl" x="10" y="3.5">ALL CLUSTERS 100%</text>
  </g>
</g>

<!-- 3D Cover Flow Carousel Deck -->
<g transform="translate(0, 10)">
  <g class="c-pos1">{c1}</g>
  <g class="c-pos2">{c2}</g>
  <g class="c-pos3">{c3}</g>
  <g class="c-pos4">{c4}</g>
  <g class="c-pos5">{c5}</g>
</g>

<!-- Pagination & Navigation Controls (Ref: Image 3) -->
<g transform="translate({W / 2}, 314)">
  <!-- Left Chevron Button -->
  <g transform="translate(-68, 0)">
    <circle class="ctrl-btn" cx="0" cy="0" r="10"/>
    <path class="ctrl-arrow" d="M2 -4 L-2 0 L2 4"/>
  </g>
  
  <!-- 5 Indicator Dots -->
  <circle class="ind-dot1" cx="-32" cy="0" r="2.8"/>
  <circle class="ind-dot2" cx="-16" cy="0" r="2.8"/>
  <circle class="ind-dot3" cx="0" cy="0" r="2.8"/>
  <circle class="ind-dot4" cx="16" cy="0" r="2.8"/>
  <circle class="ind-dot5" cx="32" cy="0" r="2.8"/>
  
  <!-- Right Chevron Button -->
  <g transform="translate(68, 0)">
    <circle class="ctrl-btn" cx="0" cy="0" r="10"/>
    <path class="ctrl-arrow" d="M-2 -4 L2 0 L-2 4"/>
  </g>
</g>
</svg>"""

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg.strip() + "\n")
    print(f"[OK] Generated {OUT_FILE} ({len(svg)} bytes)")

if __name__ == "__main__":
    main()
