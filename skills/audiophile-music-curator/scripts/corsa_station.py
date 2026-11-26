#!/usr/bin/env python3
"""
Opel Corsa Station -> Forwarding Wrapper to Universal Car Audio Station (v3.0)
Maintains 100% backward compatibility with existing shortcuts and automations.
"""
import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
UNIVERSAL_STATION = os.path.join(SCRIPT_DIR, "car_audio_station.py")

if __name__ == "__main__":
    if os.path.exists(UNIVERSAL_STATION):
        subprocess.run([sys.executable, UNIVERSAL_STATION] + sys.argv[1:])
    else:
        print("[HATA] car_audio_station.py bulunamadi!")
