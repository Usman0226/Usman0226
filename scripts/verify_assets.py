#!/usr/bin/env python3
import re
import os

with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

matches = set(re.findall(r'src=["\']\./(assets/[^"\']+)["\']', text))
all_ok = True
for m in sorted(matches):
    exists = os.path.exists(m)
    size = os.path.getsize(m) if exists else 0
    status = "OK" if exists and size > 0 else "FAIL"
    if not (exists and size > 0):
        all_ok = False
    print(f"[{status}] {m} ({size:,} bytes)")

if all_ok:
    print(f"\nAll {len(matches)} referenced assets exist and are non-empty.")
else:
    print("\nSome assets failed verification!")
    exit(1)
