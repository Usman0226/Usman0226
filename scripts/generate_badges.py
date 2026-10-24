#!/usr/bin/env python3
"""Generate unified, pixel-perfect SVG badge strips for project tools and stack.
Eliminates all Markdown baseline misalignment, broken padding, and dark-mode invisibility.
"""
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ICONS_DIR = os.path.join(SCRIPT_DIR, "..", "assets", "icons")
BADGES_DIR = os.path.join(SCRIPT_DIR, "..", "assets", "badges")
os.makedirs(BADGES_DIR, exist_ok=True)

# Custom color/invert overrides for monochrome brand icons
ADAPTIVE_ICONS = {"express", "nextjs", "prisma", "github", "vercel", "socketdotio"}

BADGE_CSS = """<style>
.badge-bg { fill: #f6f8fa; stroke: #d0d7de; stroke-width: 1px; }
.badge-txt { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; font-weight: 600; fill: #24292f; }
.mono-icon { fill: #24292f; }
.dim-txt { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 10px; font-weight: 600; fill: #57606a; }
.pill-plain { fill: #f6f8fa; stroke: #d0d7de; stroke-width: 1px; }
@media (prefers-color-scheme: dark) {
  .badge-bg { fill: rgba(255, 255, 255, 0.06); stroke: rgba(255, 255, 255, 0.14); }
  .badge-txt { fill: #f0f6fc; }
  .mono-icon { fill: #ffffff !important; }
  .dim-txt { fill: #8b949e; }
  .pill-plain { fill: rgba(255, 255, 255, 0.05); stroke: rgba(255, 255, 255, 0.12); }
}
</style>"""

def load_icon_inner(name):
    path = os.path.join(ICONS_DIR, f"{name}.svg")
    if not os.path.exists(path):
        return None, 24, 24
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    # Strip XML declaration and comments
    content = re.sub(r'<\?xml[^>]*\?>', '', content)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Extract outer viewBox
    vb_match = re.search(r'viewBox=["\']0 0 ([\d\.]+) ([\d\.]+)["\']', content)
    vw, vh = (24.0, 24.0)
    if vb_match:
        vw, vh = float(vb_match.group(1)), float(vb_match.group(2))
    
    # Extract inner svg content
    inner = content
    svg_body_match = re.search(r'<svg[^>]*>(.*)</svg>', content, flags=re.DOTALL)
    if svg_body_match:
        inner = svg_body_match.group(1).strip()
    
    # Strip nested <svg> or <title>
    inner = re.sub(r'<title>[^<]*</title>', '', inner).strip()
    inner = re.sub(r'<\/?svg[^>]*>', '', inner).strip()
    
    if name in ADAPTIVE_ICONS:
        # replace fill="#000000", fill="black", fill="#000", or fill="#fff" with class="mono-icon"
        inner = re.sub(r'fill=["\']#(?:000(?:000)?|fff(?:fff)?|000)["\']', 'class="mono-icon"', inner)
        inner = re.sub(r'fill=["\'](?:black|white)["\']', 'class="mono-icon"', inner)
        if 'class="mono-icon"' not in inner and 'stroke=' not in inner:
            inner = f'<g class="mono-icon">{inner}</g>'
    
    return inner, vw, vh

def calc_pill_width(label, has_icon=True):
    # Char width in 11px system font is approx 6.6px
    text_width = len(label) * 6.6
    if has_icon:
        return int(27 + text_width + 8)
    else:
        return int(8 + text_width + 8)

PROJECT_BADGES = {
    "nodues-stack": [
        ("react", "React"),
        ("express", "Express"),
        ("mongodb", "MongoDB"),
        ("nodejs", "Node.js"),
        (None, "SSE"),
        (None, "xlsx"),
    ],
    "lifelink-stack": [
        ("react", "React"),
        ("nodejs", "Node.js"),
        ("socketdotio", "Socket.io"),
        ("leaflet", "Leaflet"),
        (None, "GeoJSON"),
    ],
    "dfesta-stack": [
        ("nextjs", "Next.js"),
        ("typescript", "TypeScript"),
        ("mongodb", "MongoDB"),
        ("tailwindcss", "Tailwind"),
    ],
    "bizeasy-stack": [
        ("nodejs", "Node.js"),
        ("meta", "Meta Cloud API"),
        ("razorpay", "Razorpay"),
        (None, "Webhooks"),
    ],
    "hireminds-stack": [
        ("fastapi", "FastAPI"),
        ("python", "Python"),
        ("groq", "Groq"),
        ("react", "React"),
        (None, "AsyncIO"),
    ],
    "ncc-stack": [
        ("react", "React"),
        ("express", "Express"),
        ("postgresql", "PostgreSQL"),
        ("prisma", "Prisma"),
    ],
}

def generate_badge_strip(name, items):
    H = 26
    gap = 8
    elements = []
    current_x = 0
    
    for icon_name, label in items:
        has_icon = icon_name is not None
        pill_w = calc_pill_width(label, has_icon=has_icon)
        
        bg_class = "badge-bg" if has_icon else "pill-plain"
        elements.append(f'<g transform="translate({current_x}, 1)">')
        elements.append(f'  <rect class="{bg_class}" width="{pill_w}" height="{H-2}" rx="5"/>')
        
        if has_icon:
            inner, vw, vh = load_icon_inner(icon_name)
            s = 13.5 / max(vw, vh)
            icon_x = 7
            icon_y = (H - 2 - (vh * s)) / 2
            elements.append(f'  <g transform="translate({icon_x:.1f}, {icon_y:.1f}) scale({s:.4f})">{inner}</g>')
            text_x = 26
            elements.append(f'  <text class="badge-txt" x="{text_x}" y="16">{label}</text>')
        else:
            text_x = 8
            elements.append(f'  <text class="dim-txt" x="{text_x}" y="15.5">{label}</text>')
            
        elements.append('</g>')
        current_x += pill_w + gap
        
    total_w = current_x - gap if current_x > 0 else 0
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {H}" width="{total_w}" height="{H}" role="img" aria-label="{name}">
{BADGE_CSS}
{''.join(elements)}
</svg>"""

    out_file = os.path.join(BADGES_DIR, f"{name}.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg.strip() + "\n")
    print(f"[OK] Generated assets/badges/{name}.svg ({total_w}x{H}px)")

def main():
    for name, items in PROJECT_BADGES.items():
        generate_badge_strip(name, items)
    print("\nAll project badge strips generated successfully!")

if __name__ == "__main__":
    main()
