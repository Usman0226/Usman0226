#!/usr/bin/env python3
"""Unified Profile Customization & Theme Switcher.
Allows changing theme colors, hero metrics, freelance status, and GitHub username,
and automatically regenerates and verifies all SVG assets across the repository.

Usage:
  Interactive Menu:
    python scripts/customize.py

  Direct CLI Options:
    python scripts/customize.py --theme emerald
    python scripts/customize.py --theme violet
    python scripts/customize.py --color "#6366f1"
    python scripts/customize.py --status "Available for freelance & contracts"
    python scripts/customize.py --user Usman0226
    python scripts/customize.py --build
    python scripts/customize.py --list
"""
import os
import sys
import json
import argparse
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "profile_config.json")

PRESETS = {
    "blue": {
        "name": "Electric Blue (Notion / Linear)",
        "light": "#2383e2",
        "dark": "#529cca",
        "bg_light": "#e7f3f8",
        "bg_dark": "#182833",
        "txt_light": "#1967b2",
        "txt_dark": "#6cb3e8",
    },
    "emerald": {
        "name": "Emerald Green (Terminal / Growth)",
        "light": "#10b981",
        "dark": "#34d399",
        "bg_light": "#ecfdf5",
        "bg_dark": "#132e22",
        "txt_light": "#047857",
        "txt_dark": "#6ee7b7",
    },
    "violet": {
        "name": "Linear Violet (AI / Modern)",
        "light": "#8b5cf6",
        "dark": "#a78bfa",
        "bg_light": "#f5f3ff",
        "bg_dark": "#231c38",
        "txt_light": "#6d28d9",
        "txt_dark": "#c4b5fd",
    },
    "amber": {
        "name": "Sunset Amber (Vibrant / Warm)",
        "light": "#f59e0b",
        "dark": "#fbbf24",
        "bg_light": "#fef3c7",
        "bg_dark": "#362615",
        "txt_light": "#b45309",
        "txt_dark": "#fde68a",
    },
    "rose": {
        "name": "Modern Rose (Sleek / Crimson)",
        "light": "#f43f5e",
        "dark": "#fb7185",
        "bg_light": "#ffe4e6",
        "bg_dark": "#381921",
        "txt_light": "#be123c",
        "txt_dark": "#fda4af",
    },
    "cyan": {
        "name": "Cyber Cyan (High Tech)",
        "light": "#06b6d4",
        "dark": "#38bdf8",
        "bg_light": "#e0f2fe",
        "bg_dark": "#132b38",
        "txt_light": "#0e7490",
        "txt_dark": "#7dd3fc",
    },
    "monochrome": {
        "name": "Monochrome (Minimalist Studio)",
        "light": "#161616",
        "dark": "#f0f0f0",
        "bg_light": "#f4f4f2",
        "bg_dark": "#242424",
        "txt_light": "#161616",
        "txt_dark": "#f0f0f0",
    },
}

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
    print(f"-> Configuration saved to {os.path.relpath(CONFIG_PATH, ROOT_DIR)}")

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    if len(hex_code) == 3:
        hex_code = "".join(c*2 for c in hex_code)
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f"#{max(0, min(255, int(r))):02x}{max(0, min(255, int(g))):02x}{max(0, min(255, int(b))):02x}"

def generate_custom_theme(hex_code):
    r, g, b = hex_to_rgb(hex_code)
    # Dark mode lighter variant (lighten by ~20%)
    dr = min(255, int(r + (255 - r) * 0.28))
    dg = min(255, int(g + (255 - g) * 0.28))
    db = min(255, int(b + (255 - b) * 0.28))
    dark_hex = rgb_to_hex(dr, dg, db)

    # Light BG tint (~90% white mix)
    bg_l_r = int(r * 0.12 + 255 * 0.88)
    bg_l_g = int(g * 0.12 + 255 * 0.88)
    bg_l_b = int(b * 0.12 + 255 * 0.88)
    bg_light = rgb_to_hex(bg_l_r, bg_l_g, bg_l_b)

    # Dark BG tint (~88% black mix)
    bg_d_r = int(r * 0.18 + 18 * 0.82)
    bg_d_g = int(g * 0.18 + 18 * 0.82)
    bg_d_b = int(b * 0.18 + 18 * 0.82)
    bg_dark = rgb_to_hex(bg_d_r, bg_d_g, bg_d_b)

    # Deep text shade for light mode
    txt_l_r = int(r * 0.8)
    txt_l_g = int(g * 0.8)
    txt_l_b = int(b * 0.8)
    txt_light = rgb_to_hex(txt_l_r, txt_l_g, txt_l_b)

    # Bright text shade for dark mode
    txt_dark = rgb_to_hex(min(255, dr + 20), min(255, dg + 20), min(255, db + 20))

    return {
        "name": f"Custom ({hex_code})",
        "light": hex_code,
        "dark": dark_hex,
        "bg_light": bg_light,
        "bg_dark": bg_dark,
        "txt_light": txt_light,
        "txt_dark": txt_dark,
    }

def apply_theme(cfg, theme_data, theme_id="custom"):
    cfg["theme"] = theme_id
    if "colors" not in cfg:
        cfg["colors"] = {}
    cfg["colors"]["primary"] = {
        "light": theme_data["light"],
        "dark": theme_data["dark"]
    }
    cfg["colors"]["primary_bg"] = {
        "light": theme_data["bg_light"],
        "dark": theme_data["bg_dark"]
    }
    cfg["colors"]["primary_txt"] = {
        "light": theme_data["txt_light"],
        "dark": theme_data["txt_dark"]
    }
    if "activity" not in cfg:
        cfg["activity"] = {}
    cfg["activity"]["color"] = {
        "light": theme_data["light"],
        "dark": theme_data["dark"]
    }

def rebuild_all_assets(cfg=None):
    print("\n" + "="*50)
    print("  REBUILDING & VERIFYING ALL PROFILE ASSETS")
    print("="*50)

    commands = [
        ("Hero SVG", [sys.executable, os.path.join(SCRIPT_DIR, "generate_hero_svg.py")]),
        ("Activity Graph", [sys.executable, os.path.join(SCRIPT_DIR, "activity.py")]),
        ("Work Showcase SVGs", [sys.executable, os.path.join(SCRIPT_DIR, "generate_work_svgs.py")]),
        ("Work Composite SVG", [sys.executable, os.path.join(SCRIPT_DIR, "generate_composite_work_svg.py")]),
        ("Project Badge Strips", [sys.executable, os.path.join(SCRIPT_DIR, "generate_badges.py")]),
        ("Stack Architecture Matrix", [sys.executable, os.path.join(SCRIPT_DIR, "generate_stack_svg.py")]),
        ("Recognition SVG", [sys.executable, os.path.join(SCRIPT_DIR, "generate_recognition_svg.py")]),
        ("Status Card", [sys.executable, os.path.join(SCRIPT_DIR, "status.py"), "--offline"]),
        ("Asset Verification Suite", [sys.executable, os.path.join(SCRIPT_DIR, "verify_assets.py")]),
    ]

    success = True
    for name, cmd in commands:
        try:
            res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True, check=True)
            print(f" [OK] {name}")
            if res.stdout.strip():
                for line in res.stdout.strip().splitlines():
                    print(f"      {line}")
        except subprocess.CalledProcessError as e:
            print(f" [ERR] {name} failed with code {e.returncode}:")
            print(f"      {e.stderr or e.stdout}")
            success = False

    print("="*50)
    if success:
        print(" -> All profile assets generated, synchronized and verified!\n")
    else:
        print(" -> Rebuild completed with warnings/errors above.\n")

def print_current_config(cfg):
    print("\n" + "-"*40)
    print(" CURRENT PROFILE CONFIGURATION")
    print("-" * 40)
    theme_name = cfg.get("theme", "blue")
    prim = cfg.get("colors", {}).get("primary", {})
    print(f" Theme:         {theme_name.upper()} (Light: {prim.get('light')}, Dark: {prim.get('dark')})")
    
    hero = cfg.get("hero", {})
    print(f" Name:          {hero.get('name')}")
    print(f" Status:        {hero.get('status')}")
    print(f" Bio L1:        {hero.get('bio1')}")
    print(f" Bio L2:        {hero.get('bio2')}")
    
    m1 = hero.get("metric1", {})
    m2 = hero.get("metric2", {})
    m3 = hero.get("metric3", {})
    print(f" Metric 1:      {m1.get('val')} - {m1.get('l1')} | {m1.get('l2')}")
    print(f" Metric 2:      {m2.get('val')} - {m2.get('l1')} | {m2.get('l2')}")
    print(f" Metric 3:      {m3.get('val')} - {m3.get('l1')} | {m3.get('l2')}")

    act = cfg.get("activity", {})
    print(f" Activity User: {act.get('username')}")
    print(f" Graph Color:   Light: {act.get('color', {}).get('light')}, Dark: {act.get('color', {}).get('dark')}")
    print("-" * 40 + "\n")

def interactive_menu():
    cfg = load_config()
    while True:
        print("\n" + "="*45)
        print("  PROFILE CUSTOMIZER & ASSET BUILDER")
        print("="*45)
        print(" 1) Choose Preset Color Theme")
        print(" 2) Enter Custom Hex Accent Color")
        print(" 3) Edit Hero Metrics & Subtitles")
        print(" 4) Edit Freelance / Availability Status")
        print(" 5) Edit GitHub Activity Username")
        print(" 6) View Current Configuration")
        print(" 7) Apply Changes & Rebuild All Assets")
        print(" 0) Exit")
        print("="*45)

        choice = input("Enter choice [0-7]: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            print("\nAvailable Presets:")
            preset_keys = list(PRESETS.keys())
            for idx, key in enumerate(preset_keys, 1):
                p = PRESETS[key]
                print(f"  {idx}) {p['name']} ({p['light']})")
            
            p_sel = input("Select preset number or name: ").strip().lower()
            sel_key = None
            if p_sel.isdigit() and 1 <= int(p_sel) <= len(preset_keys):
                sel_key = preset_keys[int(p_sel) - 1]
            elif p_sel in PRESETS:
                sel_key = p_sel

            if sel_key:
                apply_theme(cfg, PRESETS[sel_key], sel_key)
                save_config(cfg)
                rebuild_all_assets(cfg)
            else:
                print("Invalid preset choice.")

        elif choice == "2":
            hex_input = input("Enter hex color code (e.g. #6366f1, #0ea5e9, #ff4081): ").strip()
            if not hex_input.startswith("#"):
                hex_input = "#" + hex_input
            try:
                theme_data = generate_custom_theme(hex_input)
                apply_theme(cfg, theme_data, f"custom_{hex_input.lstrip('#')}")
                save_config(cfg)
                rebuild_all_assets(cfg)
            except Exception as e:
                print(f"Error parsing hex: {e}")

        elif choice == "3":
            hero = cfg.setdefault("hero", {})
            print("\nEditing Hero Metrics (Press Enter to keep current value):")
            for m_key in ["metric1", "metric2", "metric3"]:
                cur = hero.setdefault(m_key, {"val": "", "l1": "", "l2": ""})
                print(f"\n--- {m_key.upper()} ---")
                new_val = input(f"Value [{cur.get('val')}]: ").strip()
                if new_val: cur["val"] = new_val
                new_l1 = input(f"Subtitle Line 1 [{cur.get('l1')}]: ").strip()
                if new_l1: cur["l1"] = new_l1
                new_l2 = input(f"Subtitle Line 2 [{cur.get('l2')}]: ").strip()
                if new_l2: cur["l2"] = new_l2
            save_config(cfg)
            rebuild_all_assets(cfg)

        elif choice == "4":
            hero = cfg.setdefault("hero", {})
            cur_status = hero.get("status", "Available for freelance & contracts")
            new_status = input(f"New availability status [{cur_status}]: ").strip()
            if new_status:
                hero["status"] = new_status
                save_config(cfg)
                rebuild_all_assets(cfg)

        elif choice == "5":
            act = cfg.setdefault("activity", {})
            cur_user = act.get("username", "Usman0226")
            new_user = input(f"GitHub Username for activity graph [{cur_user}]: ").strip()
            if new_user:
                act["username"] = new_user
                save_config(cfg)
                rebuild_all_assets(cfg)

        elif choice == "6":
            print_current_config(cfg)

        elif choice == "7":
            save_config(cfg)
            rebuild_all_assets(cfg)

def main():
    parser = argparse.ArgumentParser(description="Profile Customizer & Asset Builder")
    parser.add_argument("--theme", choices=list(PRESETS.keys()), help="Apply a preset color theme")
    parser.add_argument("--color", help="Apply any custom hex accent color (e.g. #6366f1)")
    parser.add_argument("--status", help="Update the freelance availability badge text")
    parser.add_argument("--user", help="Update the GitHub username for the activity graph")
    parser.add_argument("--build", action="store_true", help="Rebuild and verify all SVG assets")
    parser.add_argument("--list", action="store_true", help="List all available preset themes")

    args = parser.parse_args()
    cfg = load_config()

    if args.list:
        print("\nAvailable Preset Themes:")
        for k, v in PRESETS.items():
            print(f"  * {k:<12}: {v['name']} (Light: {v['light']} | Dark: {v['dark']})")
        print()
        return

    modified = False

    if args.theme:
        apply_theme(cfg, PRESETS[args.theme], args.theme)
        print(f"-> Selected theme: {PRESETS[args.theme]['name']}")
        modified = True

    if args.color:
        theme_data = generate_custom_theme(args.color)
        apply_theme(cfg, theme_data, f"custom_{args.color.lstrip('#')}")
        print(f"-> Applied custom color: {args.color}")
        modified = True

    if args.status:
        cfg.setdefault("hero", {})["status"] = args.status
        print(f"-> Updated status: {args.status}")
        modified = True

    if args.user:
        cfg.setdefault("activity", {})["username"] = args.user
        print(f"-> Updated activity user: {args.user}")
        modified = True

    if modified:
        save_config(cfg)
        rebuild_all_assets(cfg)
    elif args.build:
        rebuild_all_assets(cfg)
    elif len(sys.argv) == 1:
        # No CLI arguments provided, launch interactive menu
        interactive_menu()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
