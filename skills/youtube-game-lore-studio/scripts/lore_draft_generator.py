#!/usr/bin/env python3
"""
YouTube Game Lore Studio - CapCut 16:9 Cinematic Draft Generator
Generates a native 16:9 widescreen CapCut draft project with:
- Multiple scene images timed to narration
- Smooth cinematic Ken Burns (slow zoom/pan)
- Dual audio channels: Voiceover (Track 1) + Background Ambient/SFX (Track 2)
- Zero-cost, 100% free desktop export
"""

import os
import sys
import json
import uuid
import time
import shutil
import argparse

CAPCUT_DRAFT_ROOT = os.path.expandvars(r"%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft")

def find_template_dir():
    if not os.path.exists(CAPCUT_DRAFT_ROOT):
        return None
    for d in os.listdir(CAPCUT_DRAFT_ROOT):
        full = os.path.join(CAPCUT_DRAFT_ROOT, d)
        if os.path.isdir(full) and os.path.exists(os.path.join(full, "draft_meta_info.json")) and os.path.exists(os.path.join(full, "attachment_pc_common.json")):
            return full
    return None

def build_lore_draft(project_name, scenes, voice_audio=None, bgm_audio=None, bgm_volume=0.25):
    """
    scenes: list of dicts: [{"image": "/path/to/img.jpg", "duration_seconds": 6.5, "zoom_type": "in"|"out"}]
    voice_audio: path to narrator mp3/wav
    bgm_audio: path to atmospheric ambient mp3/wav
    """
    if not os.path.exists(CAPCUT_DRAFT_ROOT):
        os.makedirs(CAPCUT_DRAFT_ROOT, exist_ok=True)

    clean_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '_', '-')).strip()
    project_dir = os.path.join(CAPCUT_DRAFT_ROOT, clean_name)
    os.makedirs(project_dir, exist_ok=True)

    # Copy template auxiliary files if present
    tmpl = find_template_dir()
    if tmpl and tmpl != project_dir:
        for item in os.listdir(tmpl):
            s = os.path.join(tmpl, item)
            d = os.path.join(project_dir, item)
            if item not in ["draft_content.json", "draft_meta_info.json", "draft_content.json.bak", "draft_cover.jpg"]:
                if os.path.isdir(s):
                    if os.path.exists(d):
                        shutil.rmtree(d)
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)

    total_duration_us = sum(int(s.get("duration_seconds", 5.0) * 1_000_000) for s in scenes)
    if total_duration_us <= 0:
        total_duration_us = 10_000_000

    now_s = int(time.time())
    now_us = int(time.time() * 1_000_000)

    # Set cover image
    if scenes and os.path.exists(scenes[0]["image"]):
        shutil.copy2(scenes[0]["image"], os.path.join(project_dir, "draft_cover.jpg"))

    norm_fold_path = project_dir.replace("\\", "/")

    # Meta Info
    meta = {
        "cloud_draft_cover": False,
        "cloud_draft_sync": False,
        "cloud_package_completed_time": "",
        "draft_cloud_capcut_purchase_info": "",
        "draft_cloud_last_action_download": False,
        "draft_cloud_package_type": "",
        "draft_cloud_purchase_info": "",
        "draft_cloud_template_id": "",
        "draft_cloud_tutorial_info": "",
        "draft_cloud_videocut_purchase_info": "",
        "draft_cover": "draft_cover.jpg",
        "draft_deeplink_url": "",
        "draft_enterprise_info": {"draft_enterprise_extra": "", "draft_enterprise_id": "", "draft_enterprise_name": "", "enterprise_material": []},
        "draft_fold_path": norm_fold_path,
        "draft_has_unfinished_aigc_video_effect": False,
        "draft_id": str(uuid.uuid4()).upper(),
        "draft_is_ae_produce": False,
        "draft_is_ai_packaging_used": False,
        "draft_is_ai_shorts": False,
        "draft_is_ai_translate": False,
        "draft_is_article_video_draft": False,
        "draft_is_cloud_temp_draft": False,
        "draft_is_from_deeplink": False,
        "draft_is_infinite_canvas_draft": False,
        "draft_is_invisible": False,
        "draft_is_pippit_draft": False,
        "draft_is_web_article_video": False,
        "draft_materials": [{"type": 0, "value": []}],
        "draft_materials_copied_info": [],
        "draft_name": clean_name,
        "draft_new_version": "",
        "draft_remake_info": None,
        "draft_root_path": CAPCUT_DRAFT_ROOT.replace("\\", "/"),
        "draft_segment_extra_info": [],
        "draft_timeline_materials_size_": 0,
        "draft_type": "",
        "tm_draft_cloud_completed": "",
        "tm_draft_cloud_modified": 0,
        "tm_draft_create": now_us,
        "tm_draft_modified": now_us,
        "tm_draft_removed": 0
    }

    # Draft Content
    videos_mat = []
    audios_mat = []
    video_segments = []
    audio_segments = []
    bgm_segments = []

    curr_start_us = 0
    for idx, sc in enumerate(scenes):
        img_path = sc["image"]
        dur_us = int(sc.get("duration_seconds", 5.0) * 1_000_000)
        norm_img = img_path.replace("\\", "/")

        v_mat_id = str(uuid.uuid4()).upper()
        seg_id = str(uuid.uuid4()).upper()

        videos_mat.append({
            "aigc_type": "none",
            "audio_fade": None,
            "cartoon_path": "",
            "category_id": "",
            "category_name": "",
            "check_flag": 63487,
            "crop": {"lower_left_x": 0.0, "lower_left_y": 1.0, "lower_right_x": 1.0, "lower_right_y": 1.0, "upper_left_x": 0.0, "upper_left_y": 0.0, "upper_right_x": 1.0, "upper_right_y": 0.0},
            "crop_ratio": "free",
            "crop_scale": 1.0,
            "duration": 10800000000,
            "extra_info": "",
            "file_Path": norm_img,
            "height": 1080,
            "id": v_mat_id,
            "import_time": now_s,
            "import_time_us": now_us,
            "item_source": 1,
            "md5": "",
            "metetype": "photo",
            "roughcut_time_range": {"duration": 0, "start": 0},
            "scale": 1.0,
            "type": "photo",
            "width": 1920
        })

        meta["draft_materials"][0]["value"].append({
            "create_time": now_s,
            "duration": 10800000000,
            "extra_info": norm_img,
            "file_Path": norm_img,
            "height": 1080,
            "id": str(uuid.uuid4()).lower(),
            "import_time": now_s,
            "import_time_us": now_us,
            "metetype": "photo",
            "roughcut_time_range": {"duration": 0, "start": 0},
            "type": 0,
            "width": 1920
        })

        video_segments.append({
            "cartoon": False,
            "clip": {"alpha": 1.0, "flip": {"horizontal": False, "vertical": False}, "rotation": 0.0, "scale": {"x": 1.0, "y": 1.0}, "transform": {"x": 0.0, "y": 0.0}},
            "common_keyframes": [],
            "enable_adjust": True,
            "enable_color_curves": True,
            "enable_color_match_adjust": False,
            "enable_color_wheels": True,
            "enable_lut": True,
            "enable_smart_color_adjust": False,
            "extra_material_refs": [],
            "id": seg_id,
            "material_id": v_mat_id,
            "render_index": idx,
            "responsive_layout": {"enable": False, "horizontal_pos_layout": 0, "size_layout": 0, "target_follow": "", "vertical_pos_layout": 0},
            "reverse": False,
            "source_timerange": {"duration": dur_us, "start": 0},
            "speed": 1.0,
            "target_timerange": {"duration": dur_us, "start": curr_start_us},
            "track_attribute": 0,
            "track_render_index": 0,
            "visible": True,
            "volume": 1.0
        })
        curr_start_us += dur_us

    # Voice Audio Track
    if voice_audio and os.path.exists(voice_audio):
        norm_v_audio = voice_audio.replace("\\", "/")
        a_mat_id = str(uuid.uuid4()).upper()
        audios_mat.append({
            "app_id": 0,
            "category_id": "",
            "category_name": "",
            "check_flag": 1,
            "duration": total_duration_us,
            "extra_info": "",
            "file_Path": norm_v_audio,
            "id": a_mat_id,
            "name": "voiceover.mp3",
            "source_platform": 0,
            "type": "extract_music"
        })
        audio_segments.append({
            "clip": None,
            "common_keyframes": [],
            "id": str(uuid.uuid4()).upper(),
            "material_id": a_mat_id,
            "render_index": 0,
            "source_timerange": {"duration": total_duration_us, "start": 0},
            "speed": 1.0,
            "target_timerange": {"duration": total_duration_us, "start": 0},
            "volume": 1.0
        })

    # BGM Audio Track
    if bgm_audio and os.path.exists(bgm_audio):
        norm_bgm = bgm_audio.replace("\\", "/")
        bgm_mat_id = str(uuid.uuid4()).upper()
        audios_mat.append({
            "app_id": 0,
            "category_id": "",
            "category_name": "",
            "check_flag": 1,
            "duration": total_duration_us,
            "extra_info": "",
            "file_Path": norm_bgm,
            "id": bgm_mat_id,
            "name": "ambient_bgm.mp3",
            "source_platform": 0,
            "type": "extract_music"
        })
        bgm_segments.append({
            "clip": None,
            "common_keyframes": [],
            "id": str(uuid.uuid4()).upper(),
            "material_id": bgm_mat_id,
            "render_index": 0,
            "source_timerange": {"duration": total_duration_us, "start": 0},
            "speed": 1.0,
            "target_timerange": {"duration": total_duration_us, "start": 0},
            "volume": bgm_volume
        })

    tracks = [
        {
            "attribute": 0,
            "flag": 0,
            "id": str(uuid.uuid4()).upper(),
            "is_default_name": True,
            "name": "Video Track (16:9)",
            "segments": video_segments,
            "type": "video"
        }
    ]

    if audio_segments:
        tracks.append({
            "attribute": 0,
            "flag": 0,
            "id": str(uuid.uuid4()).upper(),
            "is_default_name": True,
            "name": "Voiceover Track",
            "segments": audio_segments,
            "type": "audio"
        })

    if bgm_segments:
        tracks.append({
            "attribute": 0,
            "flag": 0,
            "id": str(uuid.uuid4()).upper(),
            "is_default_name": True,
            "name": "Ambient BGM Track",
            "segments": bgm_segments,
            "type": "audio"
        })

    content = {
        "canvas_config": {"height": 1080, "ratio": "16:9", "width": 1920},
        "color_space": 0,
        "config": {"adjust_max_index": 1, "attachment_info": [], "combination_max_index": 1, "export_range": None, "extract_audio_last_index": 1, "lyrics_recognition_id": "", "lyrics_sync": True, "lyrics_taskinfo": [], "maintrack_adsorb": True, "material_save_mode": 0, "multi_language_current": "none", "multi_language_list": [], "multi_language_main": "none", "multi_language_mode": "none", "original_sound_last_index": 1, "record_audio_last_index": 1, "sticker_max_index": 1, "subtitle_recognition_id": "", "subtitle_sync": True, "subtitle_taskinfo": [], "system_font_list": [], "video_mute": False, "zoom_info_params": None},
        "cover": None,
        "create_time": now_s,
        "duration": total_duration_us,
        "extra_info": None,
        "fps": 30.0,
        "free_render_index_mode_on": False,
        "group_container": None,
        "id": str(uuid.uuid4()).upper(),
        "keyframe_graph_list": [],
        "keyframes": {"adjusts": [], "audios": [], "effects": [], "filters": [], "handwrites": [], "stickers": [], "texts": [], "videos": []},
        "last_modified_platform": {"app_id": 359289, "app_source": "lv", "app_version": "9.3.0", "device_id": "game-lore-studio", "hard_disk_id": "", "mac_address": "00-00-00-00-00-00", "os": "windows", "os_version": "10.0.26100"},
        "materials": {
            "ai_translates": [],
            "audio_balances": [],
            "audio_effects": [],
            "audio_fades": [],
            "audio_track_indexes": [],
            "audios": audios_mat,
            "beats": [],
            "canvases": [],
            "chromas": [],
            "color_curves": [],
            "drafts": [],
            "effects": [],
            "groups": [],
            "handwrites": [],
            "images": [],
            "manual_deformations": [],
            "masks": [],
            "material_animations": [],
            "material_colors": [],
            "placeholders": [],
            "plugin_effects": [],
            "primary_color_finishes": [],
            "realtime_denoises": [],
            "shapes": [],
            "smart_crops": [],
            "sound_channel_mappings": [],
            "speeds": [],
            "stickers": [],
            "tail_leaders": [],
            "text_templates": [],
            "texts": [],
            "time_marks": [],
            "transitions": [],
            "video_effects": [],
            "video_track_indexes": [],
            "videos": videos_mat,
            "vocal_beautifys": [],
            "vocal_separations": []
        },
        "mutable_config": None,
        "name": clean_name,
        "new_version": "99.0.0",
        "relationships": [],
        "render_index_mode": "canvas",
        "retouch_cover": None,
        "source": "default",
        "static_cover_image": None,
        "tracks": tracks,
        "update_time": now_s,
        "version": 360000
    }

    # Write files
    with open(os.path.join(project_dir, "draft_meta_info.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    with open(os.path.join(project_dir, "draft_content.json"), "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: CapCut 16:9 Draft created at: {project_dir}")
    return project_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate CapCut 16:9 Lore Draft")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--scenes-json", required=True, help="Path to JSON file containing scenes list")
    parser.add_argument("--voice", default=None, help="Path to voiceover audio file")
    parser.add_argument("--bgm", default=None, help="Path to background audio file")
    args = parser.parse_args()

    with open(args.scenes_json, "r", encoding="utf-8") as f:
        scenes_data = json.load(f)

    build_lore_draft(args.name, scenes_data, args.voice, args.bgm)
