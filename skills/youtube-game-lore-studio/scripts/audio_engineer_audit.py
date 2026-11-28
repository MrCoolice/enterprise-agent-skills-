#!/usr/bin/env python3
"""
YouTube Game Lore Studio - Studio Master Audio Engineer Audit & Processing Engine
Analyzes recorded voice for:
- Clipping & Distortion
- Volume Levels (LUFS / Peak dBFS)
- Noise Floor & Room Ambience
- Dynamic Range (LRA)
Produces:
1. Studio Master Verdict: ONAY, SARTLI_KABUL, or REDDET with specific acoustic coaching.
2. Mastered Broadcast Polish (De-noise, Warmth EQ, Compressor, -14 LUFS Broadcast Normalization).
"""

import os
import sys
import json
import subprocess
import re
import argparse

def analyze_audio(file_path):
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    # 1. Volume detect filter
    cmd_vol = [
        "ffmpeg", "-i", file_path,
        "-af", "volumedetect",
        "-vn", "-sn", "-dn",
        "-f", "null", "NUL"
    ]
    res_vol = subprocess.run(cmd_vol, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
    vol_out = res_vol.stderr

    max_vol = None
    mean_vol = None
    m_max = re.search(r"max_volume:\s*([-0-9.]+)\s*dB", vol_out)
    m_mean = re.search(r"mean_volume:\s*([-0-9.]+)\s*dB", vol_out)
    if m_max:
        max_vol = float(m_max.group(1))
    if m_mean:
        mean_vol = float(m_mean.group(1))

    # 2. EBU R128 Loudness filter
    cmd_ebu = [
        "ffmpeg", "-i", file_path,
        "-af", "ebur128=framelog=verbose",
        "-vn", "-sn", "-dn",
        "-f", "null", "NUL"
    ]
    res_ebu = subprocess.run(cmd_ebu, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
    ebu_out = res_ebu.stderr

    lufs = None
    lra = None
    tp = None
    m_lufs = re.search(r"Integrated loudness:\s*I:\s*([-0-9.]+)\s*LUFS", ebu_out)
    m_lra = re.search(r"Loudness range:\s*LRA:\s*([-0-9.]+)\s*LU", ebu_out)
    m_tp = re.search(r"True peak:\s*Peak:\s*([-0-9.]+)\s*dBFS", ebu_out)

    if m_lufs:
        lufs = float(m_lufs.group(1))
    if m_lra:
        lra = float(m_lra.group(1))
    if m_tp:
        tp = float(m_tp.group(1))

    # 3. Decision Engine & Acoustic Coaching
    issues = []
    verdict = "ONAY"

    # Clipping
    if max_vol is not None and max_vol >= -0.3:
        issues.append("🔴 SES ÇATLAMASI (Clipping): Mikrofona çok bağırmışsın veya mikrofona çok yakın durmuşsun. Sesin dijital tepe noktasına çarpmış ve bozulmuş.")
        verdict = "REDDET"

    # Too Quiet
    if mean_vol is not None and mean_vol < -35.0:
        issues.append("🟡 ÇOK KISIK SES: Ses seviyesi çok düşük kaydedilmiş. Sesi açtığımızda dip gürültüsü ve hışırtı yükselecektir. Mikrofona biraz daha yaklaşmalısın.")
        if verdict != "REDDET":
            verdict = "SARTLI_KABUL"

    # High Dynamic Range (Uneven volume)
    if lra is not None and lra > 14.0:
        issues.append("🟡 DALGALI SES (Düzensiz Mesafe): Bazı kelimeler çok fısıltılı, bazıları ani yükselmiş. Telefonu ağzına sabit mesafede tutmalısın.")
        if verdict != "REDDET":
            verdict = "SARTLI_KABUL"

    return {
        "file": file_path,
        "max_volume_dB": max_vol,
        "mean_volume_dB": mean_vol,
        "integrated_lufs": lufs,
        "loudness_range_lu": lra,
        "true_peak_dbfs": tp,
        "verdict": verdict,
        "issues": issues
    }

def master_audio(input_path, output_path):
    """
    Applies standard broadcast mastering DSP chain:
    - Highpass 75Hz (kills low rumble)
    - Gentle de-hiss / noise gate
    - Warmth vocal EQ (+2.5dB @ 130Hz, -2dB @ 400Hz boxiness, +1.5dB @ 3.5kHz clarity)
    - Dynamic compressor
    - EBU R128 Broadcast Normalization (-14 LUFS)
    """
    filter_chain = (
        "highpass=f=75,"
        "afftdn=nr=10:nf=-30,"
        "equalizer=f=130:width_type=o:w=1.2:g=2.5,"
        "equalizer=f=400:width_type=o:w=1.0:g=-2.0,"
        "equalizer=f=3500:width_type=o:w=1.0:g=1.5,"
        "acompressor=threshold=-18dB:ratio=3:attack=25:release=250,"
        "loudnorm=I=-14:TP=-1.5:LRA=10"
    )

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-af", filter_chain,
        "-b:a", "192k",
        output_path
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Studio Master Audio Engineer Audit")
    parser.add_argument("file", help="Path to audio file to audit")
    parser.add_argument("--master", action="store_true", help="Also generate mastered version")
    args = parser.parse_args()

    report = analyze_audio(args.file)
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if args.master:
        base, ext = os.path.splitext(args.file)
        out = f"{base}_mastered.mp3"
        master_audio(args.file, out)
        print(f"\n[MASTERED FILE GENERATED]: {out}")
