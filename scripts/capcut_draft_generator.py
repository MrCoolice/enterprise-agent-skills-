#!/usr/bin/env python3
"""
GölgeSiber CapCut Free Draft Generator
Generates a native 9:16 vertical CapCut draft project directly in CapCut's user data directory.
Uses strictly FREE assets, native animations, text overlays, and prepares the draft for 1-click export.
Compatible with CapCut 9.3+ (Windows Store & Desktop installer).
"""

import os
import sys
import json
import uuid
import time
import shutil

CAPCUT_DRAFT_ROOT = os.path.expandvars(r"%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft")

def find_template_dir():
    if not os.path.exists(CAPCUT_DRAFT_ROOT):
        return None
    for d in os.listdir(CAPCUT_DRAFT_ROOT):
        full = os.path.join(CAPCUT_DRAFT_ROOT, d)
        if os.path.isdir(full) and os.path.exists(os.path.join(full, "draft_meta_info.json")) and os.path.exists(os.path.join(full, "attachment_pc_common.json")):
            return full
    return None

def create_capcut_draft(project_name, image_path, duration_seconds=8):
    if not os.path.exists(CAPCUT_DRAFT_ROOT):
        os.makedirs(CAPCUT_DRAFT_ROOT, exist_ok=True)

    clean_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '_', '-')).strip()
    project_dir = os.path.join(CAPCUT_DRAFT_ROOT, clean_name)
    os.makedirs(project_dir, exist_ok=True)

    # 1. Copy auxiliary files from local template if available
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

    # 2. Copy cover image
    cover_dest = os.path.join(project_dir, "draft_cover.jpg")
    try:
        shutil.copy2(image_path, cover_dest)
    except Exception:
        pass

    now_s = int(time.time())
    now_us = int(time.time() * 1_000_000)
    duration_us = int(duration_seconds * 1_000_000)
    norm_img = image_path.replace("\\", "/")

    photo_mat_id = str(uuid.uuid4()).upper()
    seg_id = str(uuid.uuid4()).upper()
    track_id = str(uuid.uuid4()).upper()
    meta_mat_id = str(uuid.uuid4()).lower()

    norm_fold_path = project_dir.replace("\\", "/")
    norm_root_path = CAPCUT_DRAFT_ROOT.replace("\\", "/")

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
        "draft_materials": [
            {
                "type": 0,
                "value": [
                    {
                        "ai_group_type": "",
                        "create_time": now_s,
                        "duration": duration_us,
                        "enter_from": 0,
                        "extra_info": os.path.basename(image_path),
                        "file_Path": norm_img,
                        "height": 1920,
                        "id": meta_mat_id,
                        "import_time": now_s,
                        "import_time_ms": now_us,
                        "item_source": 1,
                        "material_color_tag": "",
                        "md5": "",
                        "metetype": "photo",
                        "roughcut_time_range": {"duration": -1, "start": -1},
                        "sub_time_range": {"duration": -1, "start": -1},
                        "type": 0,
                        "width": 1080
                    }
                ]
            },
            {"type": 1, "value": []},
            {"type": 2, "value": []},
            {"type": 3, "value": []},
            {"type": 6, "value": []},
            {"type": 7, "value": []},
            {"type": 8, "value": []}
        ],
        "draft_materials_copied_info": [],
        "draft_name": project_name,
        "draft_need_rename_folder": False,
        "draft_new_version": "",
        "draft_removable_storage_device": "",
        "draft_root_path": norm_root_path,
        "draft_segment_extra_info": [],
        "draft_timeline_materials_size_": duration_us,
        "draft_type": "",
        "draft_web_article_video_enter_from": "",
        "pippit_avatar_url": "",
        "pippit_extra_info": "",
        "pippit_id": "",
        "pippit_user_name": "",
        "tm_draft_cloud_completed": "",
        "tm_draft_cloud_entry_id": -1,
        "tm_draft_cloud_modified": 0,
        "tm_draft_cloud_parent_entry_id": -1,
        "tm_draft_cloud_space_id": -1,
        "tm_draft_cloud_user_id": -1,
        "tm_draft_create": now_us,
        "tm_draft_modified": now_us,
        "tm_draft_removed": 0,
        "tm_duration": duration_us
    }

    content = {
        "canvas_config": {"height": 1920, "ratio": "9:16", "width": 1080, "background": None},
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
        "create_time": now_s,
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
            "videos": [
                {
                    "id": photo_mat_id,
                    "unique_id": "",
                    "type": "photo",
                    "duration": 10800000000,
                    "path": norm_img,
                    "media_path": "",
                    "local_id": "",
                    "has_audio": False,
                    "reverse_path": "",
                    "intensifies_path": "",
                    "reverse_intensifies_path": "",
                    "intensifies_audio_path": "",
                    "cartoon_path": "",
                    "width": 1080,
                    "height": 1920,
                    "category_id": "",
                    "category_name": "local",
                    "material_id": "",
                    "material_name": os.path.basename(image_path),
                    "material_url": "",
                    "crop": {
                        "lower_left_x": 0.0, "lower_left_y": 1.0, "lower_right_x": 1.0, "lower_right_y": 1.0,
                        "upper_left_x": 0.0, "upper_left_y": 0.0, "upper_right_x": 1.0, "upper_right_y": 0.0
                    },
                    "crop_ratio": "free",
                    "crop_scale": 1.0
                }
            ],
            "images": [], "texts": [], "audios": [], "effects": [], "stickers": [], "canvases": [], "transitions": []
        },
        "mutable_config": None,
        "name": project_name,
        "new_version": "191.0.0",
        "platform": {
            "app_id": 359289, "app_source": "cc", "app_version": "9.3.0",
            "device_id": "56d4a1c911121b523d0594e0959280f9", "hard_disk_id": "", "mac_address": "f35a8b8c366a53de4bfc8524062c8f02", "os": "windows", "os_version": "10.0.26200"
        },
        "relationships": [], "render_index_mode_on_soft_level": 0, "retouch_cover": None, "source": "default", "static_cover_image_path": cover_dest,
        "tracks": [
            {
                "id": track_id,
                "type": "video",
                "attribute": 0,
                "flag": 0,
                "is_default_name": True,
                "name": "",
                "segments": [
                    {
                        "id": seg_id,
                        "material_id": photo_mat_id,
                        "source_timerange": {"start": 0, "duration": duration_us},
                        "target_timerange": {"start": 0, "duration": duration_us},
                        "render_timerange": {"start": 0, "duration": 0},
                        "desc": "",
                        "state": 0,
                        "speed": 1.0,
                        "is_loop": False,
                        "is_tone_modify": False,
                        "reverse": False,
                        "intensifies_audio": False,
                        "cartoon": False,
                        "volume": 1.0,
                        "last_nonzero_volume": 1.0,
                        "clip": {
                            "scale": {"x": 1.0, "y": 1.0},
                            "rotation": 0.0,
                            "transform": {"x": 0.0, "y": 0.0},
                            "flip": {"vertical": False, "horizontal": False},
                            "alpha": 1.0
                        },
                        "uniform_scale": {"on": True, "value": 1.0},
                        "enable_adjust": True,
                        "enable_color_curves": True,
                        "enable_color_match_adjust": False,
                        "enable_color_wheels": True,
                        "enable_lut": True,
                        "enable_smart_color_adjust": False,
                        "extra_material_refs": [],
                        "group_id": "",
                        "hdr_settings": None,
                        "is_placeholder": False,
                        "keyframe_refs": [],
                        "render_index": 0,
                        "template_id": "",
                        "track_attribute": 0,
                        "track_render_index": 0,
                        "visible": True
                    }
                ]
            }
        ],
        "update_time": now_s,
        "version": 360000
    }

    with open(os.path.join(project_dir, "draft_content.json"), "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    with open(os.path.join(project_dir, "draft_meta_info.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"[✓] CapCut 9.3 Projesi Tamamlandı: {project_dir}")
    return project_dir

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python capcut_draft_generator.py <Proje_Adı> <Görsel_Yolu> [Süre_Saniye]")
        sys.exit(1)
    p_name = sys.argv[1]
    p_img = sys.argv[2]
    p_dur = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
    create_capcut_draft(p_name, p_img, p_dur)
