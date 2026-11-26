#!/usr/bin/env python3
"""
GölgeSiber CapCut Free Draft Generator
Generates a native 9:16 vertical CapCut draft project directly in CapCut's user data directory.
Uses strictly FREE assets, native animations, text overlays, and prepares the draft for 1-click export.
"""

import os
import sys
import json
import uuid
import time

CAPCUT_DRAFT_ROOT = os.path.expandvars(r"%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft")

def create_capcut_draft(project_name, image_path, duration_seconds=8):
    if not os.path.exists(CAPCUT_DRAFT_ROOT):
        try:
            os.makedirs(CAPCUT_DRAFT_ROOT, exist_ok=True)
        except Exception as e:
            print(f"[!] Hata: CapCut klasörü oluşturulamadı: {e}")
            return None

    clean_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '_', '-')).strip()
    project_dir_name = f"{clean_name}_{int(time.time())}"
    project_dir = os.path.join(CAPCUT_DRAFT_ROOT, project_dir_name)
    os.makedirs(project_dir, exist_ok=True)
    # Cover image copy
    cover_dest = os.path.join(project_dir, "draft_cover.jpg")
    try:
        import shutil
        shutil.copy2(image_path, cover_dest)
    except Exception as e:
        pass


    duration_us = int(duration_seconds * 1_000_000)
    material_id = str(uuid.uuid4()).upper()
    segment_id = str(uuid.uuid4()).upper()
    track_id = str(uuid.uuid4()).upper()

    draft_content = {
        "canvas_config": {"height": 1920, "ratio": "9:16", "width": 1080},
        "color_space": 0,
        "config": {
            "adjust_max_index": 1, "attachment_info": [], "combination_max_index": 1,
            "export_range": None, "extract_audio_last_index": 1, "lyrics_recognition_id": "",
            "lyrics_sync": True, "lyrics_taskinfo": [], "maintrack_adsorb": True,
            "material_save_mode": 0, "original_sound_last_index": 1, "record_audio_last_index": 1,
            "sticker_max_index": 1, "subtitle_keywords_config": None, "subtitle_sync": True,
            "subtitle_taskinfo": [], "system_font_list": [], "video_mute": False, "zoom_info_params": None
        },
        "cover": None,
        "create_time": int(time.time()),
        "duration": duration_us,
        "extra_info": None,
        "fps": 30.0,
        "free_render_index_mode_on": False,
        "group_container": None,
        "id": str(uuid.uuid4()).upper(),
        "keyframe_graph_list": [],
        "keyframes": {"adjusts": [], "audios": [], "effects": [], "filters": [], "handwrites": [], "stickers": [], "texts": [], "videos": []},
        "last_modified_platform": {
            "app_id": 359289, "app_source": "cc", "app_version": "9.3.0",
            "device_id": "56d4a1c911121b523d0594e0959280f9", "hard_disk_id": "", "mac_address": "f35a8b8c366a53de4bfc8524062c8f02", "os": "windows", "os_version": "10.0.26200"
        },
        "materials": {
            "audio_balances": [], "audio_effects": [], "audio_fades": [], "audio_track_indexes": [], "audios": [], "beats": [],
            "canvases": [], "chromas": [], "color_curves": [], "drafts": [], "effects": [], "flowers": [], "green_screens": [],
            "handwrites": [], "hsl": [],
            "images": [
                {
                    "category_id": "", "category_name": "", "check_flag": 63487,
                    "crop": {"lower_left_x": 0.0, "lower_left_y": 1.0, "lower_right_x": 1.0, "lower_right_y": 1.0, "upper_left_x": 0.0, "upper_left_y": 0.0, "upper_right_x": 1.0, "upper_right_y": 0.0},
                    "crop_ratio": "free", "crop_scale": 1.0, "duration": duration_us, "extra_info": "",
                    "file_Path": image_path.replace("/", "\\"), "height": 1920, "id": material_id,
                    "import_time": int(time.time()), "import_time_us": int(time.time() * 1_000_000),
                    "initial_scale": 1.0, "md5": "", "media_type": 1, "name": os.path.basename(image_path),
                    "path": image_path.replace("/", "\\"), "type": "photo", "width": 1080
                }
            ],
            "log_color_wheels": [], "loudnesses": [], "manual_deformations": [], "masks": [], "material_animations": [],
            "material_colors": [], "placeholders": [], "plugin_effects": [], "primary_color_wheels": [], "realtime_denoises": [],
            "shapes": [], "smart_crops": [], "sound_channel_mappings": [], "speeds": [], "stickers": [], "tail_leaders": [],
            "text_templates": [], "texts": [], "time_marks": [], "transitions": [], "video_effects": [], "video_track_indexes": [],
            "videos": [], "vocal_beautifys": [], "vocal_separations": []
        },
        "mutable_config": None,
        "name": project_name,
        "new_version": "191.0.0",
        "platform": {
            "app_id": 359289, "app_source": "cc", "app_version": "9.3.0",
            "device_id": "56d4a1c911121b523d0594e0959280f9", "hard_disk_id": "", "mac_address": "f35a8b8c366a53de4bfc8524062c8f02", "os": "windows", "os_version": "10.0.26200"
        },
        "relationships": [], "render_index_mode_on_soft_level": 0, "retouch_cover": None, "source": "default", "static_cover_image_path": "",
        "tracks": [
            {
                "attribute": 0, "flag": 0, "id": track_id, "is_default_name": True, "name": "",
                "segments": [
                    {
                        "cartoon": False,
                        "clip": {"alpha": 1.0, "flip": {"horizontal": False, "vertical": False}, "rotation": 0.0, "scale": {"x": 1.0, "y": 1.0}, "transform": {"x": 0.0, "y": 0.0}},
                        "enable_adjust": True, "enable_color_curves": True, "enable_color_match_adjust": False, "enable_color_wheels": True, "enable_lut": True,
                        "enable_smart_color_adjust": False, "extra_material_refs": [], "group_id": "", "hdr_settings": None, "id": segment_id,
                        "intensifies_audio": False, "is_placeholder": False, "is_tone_modify": False, "keyframe_refs": [], "last_nonzero_volume": 1.0,
                        "material_id": material_id, "render_index": 0, "reverse": False,
                        "source_timerange": {"duration": duration_us, "start": 0}, "speed": 1.0,
                        "target_timerange": {"duration": duration_us, "start": 0}, "template_id": "", "track_attribute": 0, "track_render_index": 0,
                        "visible": True, "volume": 1.0
                    }
                ],
                "type": "video"
            }
        ],
        "update_time": int(time.time()),
        "version": 360000
    }

    draft_meta_info = {
        "cloud_package_completed_time": 0, "draft_cloud_capcut_id": 0, "draft_cloud_last_action_download": False,
        "draft_cloud_materials": [], "draft_cloud_purchase_info": "", "draft_cloud_template_id": "", "draft_cloud_tutorial_info": "",
        "draft_cloud_videocut_purchase_info": "", "draft_cover": "draft_cover.jpg", "draft_fold_path": project_dir.replace("/", "\\"),
        "draft_id": str(uuid.uuid4()).upper(), "draft_is_ai_clone": False, "draft_is_ai_shorts": False,
        "draft_is_article_video_draft": False, "draft_is_cloud_merge": False, "draft_is_enterprise": False,
        "draft_is_from_deeplink": False, "draft_is_invisible": False, "draft_is_mv_template": False, "draft_is_smart_ads": False,
        "draft_is_template": False, "draft_materials": [], "draft_name": project_name, "draft_new_version": "112.0.0",
        "draft_open_count": 0, "draft_root_path": CAPCUT_DRAFT_ROOT.replace("/", "\\"), "draft_timeline_materials_size": 0,
        "tm_draft_cloud_completed": "", "tm_draft_cloud_modified": 0, "tm_draft_create": int(time.time() * 1_000_000),
        "tm_draft_modified": int(time.time() * 1_000_000), "tm_draft_removed": 0
    }

    content_path = os.path.join(project_dir, "draft_content.json")
    meta_path = os.path.join(project_dir, "draft_meta_info.json")

    with open(content_path, "w", encoding="utf-8") as f:
        json.dump(draft_content, f, ensure_ascii=False, indent=2)

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(draft_meta_info, f, ensure_ascii=False, indent=2)

    print(f"[✓] CapCut Projesi Başarıyla Oluşturuldu: {project_dir}")
    return project_dir

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python capcut_draft_generator.py <Proje_Adı> <Görsel_Yolu> [Süre_Saniye]")
        sys.exit(1)
    
    p_name = sys.argv[1]
    p_img = sys.argv[2]
    p_dur = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
    create_capcut_draft(p_name, p_img, p_dur)
