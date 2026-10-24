#!/usr/bin/env python3
"""Fetch brand SVG icons from thesvg.org CDN and save them locally in assets/icons/.
"""
import os
import urllib.request

ICONS = [
    "react", "nextjs", "typescript", "javascript", "tailwindcss", "framer",
    "nodejs", "express", "nestjs", "postgresql", "mongodb", "prisma", "redis",
    "python", "fastapi", "groq", "langchain", "meta", "razorpay",
    "vercel", "azure", "firebase", "github", "git", "docker", "socketdotio", "leaflet"
]

out_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
os.makedirs(out_dir, exist_ok=True)

for name in ICONS:
    url = f"https://thesvg.org/icons/{name}/default.svg"
    out_file = os.path.join(out_dir, f"{name}.svg")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=10).read()
        with open(out_file, "wb") as f:
            f.write(data)
        print(f"[OK] {name:<12} -> assets/icons/{name}.svg ({len(data)} bytes)")
    except Exception as e:
        print(f"[ERR] {name}: {e}")

print("\nDone fetching tool icons from thesvg.org!")
