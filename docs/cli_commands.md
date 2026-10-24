### How to Use

#### 1. Interactive Menu Mode
Run this command from your terminal:
```bash
python customize.py
```
You will get an interactive menu:
```text
=============================================
  PROFILE CUSTOMIZER & ASSET BUILDER
=============================================
 1) Choose Preset Color Theme
 2) Enter Custom Hex Accent Color
 3) Edit Hero Metrics & Subtitles
 4) Edit Freelance / Availability Status
 5) Edit GitHub Activity Username
 6) View Current Configuration
 7) Apply Changes & Rebuild All Assets
 0) Exit
=============================================
```
Selecting any option updates your settings and automatically re-generates and verifies all assets across your profile.

---

#### 2. Quick One-Line CLI Commands

You can also pass arguments directly without entering the menu:

* **Switch to a preset theme**:
  ```bash
  python customize.py --theme emerald    # Emerald green
  python customize.py --theme violet     # Modern Linear violet
  python customize.py --theme amber      # Sunset amber/orange
  python customize.py --theme rose       # Sleek crimson rose
  python customize.py --theme cyan       # Cyber cyan/teal
  python customize.py --theme blue       # Electric blue (default)
  python customize.py --theme monochrome # Minimalist B&W
  ```

* **Use ANY custom color (Hex)**:
  ```bash
  python customize.py --color "#6366f1"  # Automatically creates light/dark shades & subtle background tints
  ```

* **Update Freelance / Availability Status**:
  ```bash
  python customize.py --status "Available for freelance contracts & MVPs"
  ```

* **Update GitHub Username**:
  ```bash
  python customize.py --user YourGitHubUsername
  ```

* **Rebuild & Verify All 20 Assets**:
  ```bash
  python customize.py --build
  ```

* **List available presets**:
  ```bash
  python customize.py --list
  ```

---

### Direct JSON Config (Optional)
All values are persisted in [scripts/profile_config.json](file:///c:/Users/chand/Usman0226/scripts/profile_config.json). If you prefer manual editing, you can tweak the JSON directly and run:
```bash
python customize.py --build
```