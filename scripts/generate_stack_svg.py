#!/usr/bin/env python3
"""Generate a clean, spacious, minimalist logo grid for the engineering stack.
Inspired directly by high-end tech logo showcases (Apple/Vercel/Linear style).
Features authentic vector logos with centered typographic labels underneath.
"""
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ICONS_DIR = os.path.join(SCRIPT_DIR, "..", "assets", "icons")
OUT_FILE = os.path.join(SCRIPT_DIR, "..", "assets", "stack.svg")

ADAPTIVE_ICONS = {"express", "nextjs", "prisma", "github", "vercel", "socketdotio"}

CSS = """<style>
.title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 21px; font-weight: 700; fill: #111827; text-anchor: middle; }
.sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 400; fill: #6b7280; text-anchor: middle; }
.lbl { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; font-weight: 500; fill: #4b5563; text-anchor: middle; }
.mono-icon { fill: #111827; }
.icon-group { transition: transform 0.2s ease; }
.icon-group:hover { transform: translateY(-2px); }

@media (prefers-color-scheme: dark) {
  .title { fill: #f9fafb; }
  .sub { fill: #9ca3af; }
  .lbl { fill: #9ca3af; }
  .mono-icon { fill: #ffffff !important; }
}
</style>"""

def xml_escape(text):
    if not text:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def load_icon_inner(name):
    if not name:
        return None, 24, 24
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
        inner = re.sub(r'fill=["\']#(?:000(?:000)?|fff(?:fff)?|000)["\']', 'class="mono-icon"', inner)
        inner = re.sub(r'fill=["\'](?:black|white)["\']', 'class="mono-icon"', inner)
        if 'class="mono-icon"' not in inner and 'stroke=' not in inner:
            inner = f'<g class="mono-icon">{inner}</g>'
    
    return inner, vw, vh

def render_logo_item(center_x, top_y, icon_name, label):
    inner, vw, vh = load_icon_inner(icon_name)
    max_icon_box = 30.0
    scale = max_icon_box / max(vw, vh)
    rendered_w = vw * scale
    rendered_h = vh * scale
    
    icon_x = center_x - (rendered_w / 2.0)
    icon_y = top_y + ((max_icon_box - rendered_h) / 2.0)
    label_y = top_y + max_icon_box + 16.0
    esc_label = xml_escape(label)
    
    return f"""
  <g class="icon-group">
    <g transform="translate({icon_x:.2f}, {icon_y:.2f}) scale({scale:.4f})">
      {inner}
    </g>
    <text class="lbl" x="{center_x}" y="{label_y:.1f}">{esc_label}</text>
  </g>
"""

def main():
    W = 880
    H = 340
    
    # Row 1 (8 items)
    row1 = [
        ("react", "React"),
        ("nextjs", "Next.js"),
        ("typescript", "TypeScript"),
        ("tailwindcss", "Tailwind CSS"),
        ("nodejs", "Node.js"),
        ("express", "Express"),
        ("fastapi", "FastAPI"),
        ("python", "Python"),
    ]
    
    # Row 2 (8 items)
    row2 = [
        ("postgresql", "PostgreSQL"),
        ("mongodb", "MongoDB"),
        ("prisma", "Prisma"),
        ("redis", "Redis"),
        ("langchain", "LangChain"),
        ("groq", "Groq"),
        ("socketdotio", "Socket.io"),
        ("docker", "Docker"),
    ]
    
    # Row 3 (6 items centered)
    row3 = [
        ("git", "Git"),
        ("github", "GitHub"),
        ("vercel", "Vercel"),
        ("azure", "Azure"),
        ("firebase", "Firebase"),
        ("framer", "Framer Motion"),
    ]
    
    elements = []
    
    # Render Row 1
    col_w1 = W / len(row1)  # 110px
    for i, (icon, label) in enumerate(row1):
        cx = (i + 0.5) * col_w1
        elements.append(render_logo_item(cx, 95, icon, label))
        
    # Render Row 2
    col_w2 = W / len(row2)  # 110px
    for i, (icon, label) in enumerate(row2):
        cx = (i + 0.5) * col_w2
        elements.append(render_logo_item(cx, 175, icon, label))
        
    # Render Row 3 (centered 6 items)
    row3_start_x = (W - (len(row3) * 110)) / 2.0
    for i, (icon, label) in enumerate(row3):
        cx = row3_start_x + (i + 0.5) * 110
        elements.append(render_logo_item(cx, 255, icon, label))
        
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Core Engineering Stack">
{CSS}
<!-- Header -->
<text class="title" x="{W / 2}" y="38">Core Engineering Stack</text>
<text class="sub" x="{W / 2}" y="60">Production-tested frameworks, distributed systems, persistence, and AI runtimes</text>

<!-- Logo Grid -->
{''.join(elements)}
</svg>"""

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg.strip() + "\n")
    print(f"[OK] Generated {OUT_FILE} ({len(svg)} bytes)")

if __name__ == "__main__":
    main()
