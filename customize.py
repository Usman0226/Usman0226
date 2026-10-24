#!/usr/bin/env python3
"""Convenience root wrapper for scripts/customize.py.
Run:
  python customize.py
"""
import os
import sys

scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
sys.path.insert(0, scripts_dir)

import customize

if __name__ == "__main__":
    customize.main()
