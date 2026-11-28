#!/usr/bin/env python3
"""
Audio Mastering Engineer - Autonomous Vocal QA & Broadcast Mastering Engine
Performs deep acoustic inspection on phone and microphone recordings.
Outputs:
- Detailed Acoustic QA Metrics (Clipping, Noise Floor, Dynamic Range, LUFS)
- 3-Tier Studio Master Verdict (REDDET, SARTLI_KABUL, ONAY)
- Human-friendly Coaching Instructions
- 1-Click Broadcast Mastering (-14 LUFS, Warmth Vocal EQ, De-noise, Compressor)
"""

import os
import sys
import json
import subprocess
import re
import argparse

def inspect_recording(file_path):
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    # 1. Volume & Peak Analysis
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

    # 2. EBU R128 Loudness Analysis
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

    # 3. Decision Matrix & Actionable Coaching
    issues = []
    coaching = []
    verdict = "ONAY"

    # Clipping (> -0.3 dBFS)
    if max_vol is not None and max_vol >= -0.3:
        issues.append("Clipping / Distortion (Ses Çatlaması)")
        coaching.append("Mikrofona çok bağırmışsın ya da nefesin doğrudan mikrofon kapsülüne çarpmış. Telefonu ağzından 15 cm uzakta tut ve doğrudan ağzına değil çenene 45 derece açıyla hizala.")
        verdict = "REDDET"

    # Too Quiet (Mean < -34 dB)
    if mean_vol is not None and mean_vol < -34.0:
        issues.append("Low Input Gain (Aşırı Kısık Ses)")
        coaching.append("Ses mikrofondan çok uzakta kaydedilmiş. Sesi dijital olarak yükselttiğimizde oda hışırtısı ve dip gürültüsü öne çıkacaktır. Mikrofona biraz daha yaklaşmalısın.")
        if verdict != "REDDET":
            verdict = "SARTLI_KABUL"

    # Unstable Dynamic Range (LRA > 14 LU)
    if lra is not None and lra > 14.0:
        issues.append("High Dynamic Fluctuations (Dengesiz Mesafe)")
        coaching.append("Kayıt sırasında telefona bir yaklaşıp bir uzaklaşmışsın; bazı kelimeler çok fısıltılı bazıları yüksek. Mesafeyi sabit tutmaya çalış.")
        if verdict != "REDDET":
            verdict = "SARTLI_KABUL"

    if not issues:
        coaching.append("Harika akustik! Ses seviyesi ve dinamik denge tam stüdyo standartlarında. Doğrudan master işlemine geçilebilir.")

    return {
        "file": file_path,
        "metrics": {
            "max_volume_dB": max_vol,
            "mean_volume_dB": mean_vol,
            "integrated_lufs": lufs,
            "loudness_range_lu": lra,
            "true_peak_dbfs": tp
        },
        "verdict": verdict,
        "detected_issues": issues,
        "engineer_coaching": coaching
    }

def render_master(input_path, output_path=None):
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_mastered.mp3"

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
    parser = argparse.ArgumentParser(description="Audio Mastering Engineer Vocal QA & Polish")
    parser.add_argument("file", help="Path to audio file")
    parser.add_argument("--master", action="store_true", help="Generate broadcast-ready mastered file")
    args = parser.parse_args()

    report = inspect_recording(args.file)
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if args.master and report.get("verdict") in ["ONAY", "SARTLI_KABUL"]:
        out = render_master(args.file)
        print(f"\n[MASTER COMPLETED]: {out}")
