---
name: character-animation-studio
description: >
  2D/3D character animation and cinematic Reels studio combining Kling AI, Gemini Omni 1.2, Blender 5.3 and 2.5D Parallax. Use for animated stories, cartoon explainers, and consistent character Reels.
---

# 🎭 Character Animation & Cartoon Short-Film Studio (`character-animation-studio`)

This skill transforms Antigravity into an end-to-end **Character Animation Director** capable of producing consistent human, cartoon, anime, and stylized 3D short films (e.g., *Efsanevi Hacker Hikâyeleri*, *Cyber-Thriller Dramatizations*, *GölgeSiber Animated Explainers*).

> **Core Golden Rule (Anti-Primitive Rule):** Never try to sculpt human characters, faces, hands, or cartoons from raw Blender primitive cubes/spheres. Always use the right character engine for the job (Kling AI Elements, Gemini Omni 1.2 Flash, or Blender Mixamo/Rigify + rigged assets).

---

## 🧭 1. Engine Routing Matrix (Pick the Best Tool First)

| Goal / Style | Primary Engine | Why |
| :--- | :--- | :--- |
| **Realistic Human / Cinematic Cyber-Thriller / True-Crime** *(e.g., Famous Hacker Stories)* | **Kling AI (`element_create` + `omni_ref_video` / `image_to_video`)** | Unmatched facial acting, lighting realism, and multi-shot character consistency via reusable Elements. |
| **2D/2.5D Cartoon, Anime, Spider-Verse / Stylized Story** | **Kling AI (`text_to_image` Character Sheet → `element_create` → `image_to_video`)** or **Gemini Omni 1.2 Flash** | Consistent stylized characters across every shot without manual 3D rigging. |
| **First-Frame → Last-Frame Seamless Transitions & Video Edits** | **Gemini Omni 1.2 Flash (`gemini-omni-flash-api`)** | Native first/last keyframe interpolation, video extension, and audio regeneration. |
| **3D Hardware + Human/Character Mix (100% Local Free GPU Render)** | **Blender 5.3 MCP + Adobe Mixamo (`.fbx`) + Rigify + Sketchfab Rigged Models** | Zero API credit cost on RTX 4070 OptiX (`~0.8s/frame`), full camera/lighting control, optional Toon Shader. |

---

## 🎨 2. Phase 1 — Character Design & Consistency Gate (Mandatory)

Before generating ANY video clips, lock character identity so the protagonist looks **100% identical** from Shot 1 to Shot 5:

1. **Character Bible (1-Paragraph Lock):** Define exact age, hair, eyewear, signature jacket/hoodie color, silhouette, and art style (e.g., *"Arcane/Spider-Verse stylized 3D, dark slate hoodie with subtle cyan trim, round glasses, warm tungsten rim light"*).
2. **Multi-View Character Reference Sheet:**
   - Generate a clean 16:9 turnaround sheet (Front, 3/4, Side + 2 key expressions) via `kling-ai:text_to_image` or `image-generator`.
   - **For Kling AI:** Register the approved character immediately with `kling-ai:element_create` so every subsequent shot references the exact same `element_id` (Zero face-drift!).
3. **Credit & Cost Protection Gate:**
   - Check credits first (`kling-ai:query_membership_and_credits`) before launching multi-shot video batches.
   - Present the **4–6 Shot Storyboard Table** (Shot #, Duration 5s, Visual Action, Camera Move, Turkish Narration, Audio/SFX) and get **explicit user approval** before spending video generation credits!

---

## 🎬 3. Phase 2 — Production Pipelines

### Pipeline A: Kling AI Character Film (Recommended for Human & Cartoon Reels)
1. **Verify Auth & Credits:** Call `who_am_i` / `query_membership_and_credits`.
2. **Lock Character Element:** Create or list reusable subject (`element_list` / `element_create`).
3. **Generate Keyframe Stills (Optional for Complex Framing):** Use `text_to_image` / `image_to_image` to lock exact 9:16 (`1080×1920`) shot compositions first.
4. **Animate Shots (`5s` per shot):**
   - Use `omni_ref_video` (with Element reference) or `image_to_video` for each shot.
   - Use `motion_control` when exact camera pan/push-in/orbit or character action timing is needed.
   - Keep camera prompts cinematic & physical: *"Slow macro dolly-in, 50mm f/1.8 shallow depth of field, subtle handheld tension, rim-lit silhouettes."*
5. **Poll & Download:** Track via `query_tasks`, save raw clips strictly to local `%LOCALAPPDATA%\golgesiber-video-studio\<project>\shots\`.

### Pipeline B: Gemini Omni 1.2 Flash (Transitions & Reference Video)
- Use `gemini-omni-1.2-flash` for first-frame-to-last-frame transitions (e.g., transforming a real-world object into a stylized cartoon world), video extensions, or audio-stripped sound regeneration.
- Always pre-optimize high-res inputs with FFmpeg per `gemini-omni-flash-api` guidelines.

### Pipeline C: Blender 5.3 Local 3D Character Pipeline (Zero API Cost, RTX GPU)
1. **Acquire Rigged Character:** Import a rigged character from **Sketchfab** (`search_assets` / `import_asset`) or an **Adobe Mixamo** `.fbx` (with free mocap animations: typing, walking, sneaking, surprised, talking).
2. **Never Call `read_factory_settings`:** Clear scenes via `bpy.data.objects.remove(...)` so the Blender MCP socket (`localhost:9876`) never drops.
3. **Retarget & Style:**
   - Apply Mixamo action cleanly to the armature (or Rigify control rig).
   - For **Cartoon / Cel-Shaded Look**: Use Shader-to-RGB + Constant ColorRamp (3-step cel shading) + Freestyle/Solidify inverted-hull black outlines.
   - For **Zack D. / Photorealistic Look**: Use Cycles **OptiX GPU** (`32–48 samples`, Adaptive Sampling `0.04`, Persistent Data `True`, AgX Punchy).
4. **Headless Render:** Save `.blend` locally and render via `blender.exe -b <file>.blend -a` for max speed and zero MCP socket timeouts.

### Pipeline D: 2.5D Concept Art & Graphic Novel Parallax (The Visual Parity Guarantee)
When procedural 3D box/primitive geometry cannot match the atmospheric mood of approved AAA concept art, or when cloud AI video generation quotas are exhausted:
1. **Visual Parity Gate:** If the user approves a 2D/3D concept preview (e.g. *Siber Şehir Kuşatması*), NEVER replace it with primitive procedural cubes. The final video MUST deliver 100% of the visual fidelity shown in the preview.
2. **4K Super-Resolution:** Upscale approved master artwork to 4K (`3840×2160`) via Lanczos or Real-ESRGAN to provide sub-pixel panning buffer for 9:16 vertical cuts (`1080×1920`).
3. **Cinematic 5-Shot Mapping:** Map every sentence of narration to distinct physical focal points of the canvas:
   - Outer Threat Zone (Left) → Central Bastion/Gateway (Center) → Defense/Shield Interface (Macro) → Secure Corridor/Passage → Thriving Cyber Metropolis (Right/Top).
4. **Multi-Layer Dynamic FX:** Add real-time procedural atmospheric layers in Python/FFmpeg:
   - Angled wind-driven rain particles (`30 FPS`).
   - Sinusoidal pulsing laser beams (`draw.line`) & impact spark bursts.
   - Hexagonal energy shield breathing luminescence.
   - Handheld camera rumble & micro-shakes during attacks.
   - Tactical HUD glass cards (`Y: 240–340`) with real-time incident telemetry.
5. **Direct NVENC Piped Stream:** Pipe RGB24 frames directly into `ffmpeg -f rawvideo -c:v h264_nvenc -preset p4 -cq 18` for instant 30 FPS hardware encoding with zero disk I/O waste.

---

## 🔊 4. Phase 3 — Voiceover, SFX, Subtitles & Safe-Zone Master Cut

Every finished character short film MUST pass this 4-point broadcast polish gate:

1. **Narration Rhythm & Audio-First Rule (Strict `atempo ≤ 1.15x`):**
   - **Turkish Natural Pacing:** Because Turkish is agglutinative, natural documentary/storytelling speech runs **~2.0–2.3 Turkish words/sec** (~120–140 Turkish WPM). For a 28–30s Reel, keep the script to **55–65 Turkish words**; for an 85-word script, extend the video duration to **38–42s**.
   - **NEVER speed up voiceover beyond `1.15x` (`atempo > 1.15`)** just to squeeze long text into a fixed duration — always either extend the video timeline to match natural ElevenLabs audio OR tighten the script before recording!
   - Structure: **0–3s Shock Hook** → **Conflict/Twist** → **Technical Cybersecurity Takeaway** → **Comment CTA** (*"Sırada hangi efsanevi hikâye gelsin? Yorumlarda buluşalım."*).
2. **Voice, Optional Background Music & Sound Design:**
   - Draft/Zero-Cost Voice: `msedge-tts` (`tr-TR-AhmetNeural` / `tr-TR-EmelNeural`).
   - Final Flagship Voice & SFX: **ElevenLabs MCP** (`eleven_v4`/`eleven_multilingual_v2` + `sound-effects` for footsteps, keyboard clatter, phone ring, alarm, bass drops; keep SFX `-18` to `-24 dB` under voice).
   - **Optional Background Music (`Nextcloud\Music`):** Always offer optional background music from `C:\Users\devops-engineer\Nextcloud\Music\` (e.g., `02_DARK_MELANCHOLY`, `09_FILM_OYUN_SOUNDTRACK`, `12_CYBERPUNK_DARK_TECHNO`, `11_SYNTHWAVE_OUTRUN`, `04_SOFT_CHILL`). Mix strictly at **`-20` to `-24 dB`** under voice with FFmpeg `sidechaincompress` ducking + `1.5 kHz` vocal-clarity EQ dip (`-4 dB`) so narration is never masked (and note copyright if using commercial tracks on public YouTube/Reels).
3. **Instagram / Shorts Safe Zone & Loudness:**
   - Resolution: `1080×1920` (`9:16`, `30 FPS`, H.264 `yuv420p`, `+faststart`).
   - Subtitles/HUD strictly inside Safe Zone (`Y: 240–320` top badge, `Y: 1350–1520` bottom kinetic captions — never covered by Reels UI!).
   - Audio loudness normalized via FFmpeg: `loudnorm=I=-14:TP=-1.5:LRA=11`.
4. **SSD & Nextcloud Storage Hygiene:**
   - Keep raw clips, `.blend` files, and caches strictly in `%LOCALAPPDATA%\golgesiber-video-studio\<project>\`.
   - Copy **ONLY** the final `.mp4`, `.srt`, and `storyboard.md` into Nextcloud `02_GolgeSiber_Web_ve_Sosyal\Reels_ve_Story_Medya\<project>\`.

---

## 🎨 5. Visual Style & Animation Genre Taxonomy (Prompt Token Bank)

When directing **Kling AI**, **Gemini Omni**, or **image-generator** character sheets and shots, select one of these 8 iconic animation genres (or blend two for a signature look) instead of generic "3D cartoon" prompts:

1. **Classical Hand-Drawn 2D:** `hand-drawn frame-by-frame animation, paper texture, rough expressive ink lines, vivid flat coloring, subtle cel shadows` *(Ghibli / Fleischer / vintage 2D feel)*.
2. **Silhouette Animation *(Killer for Cyber-Thrillers)*:** `backlit paper cut-out silhouette animation, stark high-contrast vector shadows, duotone cyan-and-obsidian backdrop, expressive glowing eyes, Lotte Reiniger inspired`.
3. **Stop-Motion Miniature:** `handcrafted stop-motion animation, felt and fabric textures, miniature cardboard/wood set under directional studio lighting, tactile micro-imperfections, Laika Studios aesthetic`.
4. **Claymation:** `stop-motion claymation, soft plasticine clay surface, subtle finger-modeled details and thumbprint textures, exaggerated elastic expressions, Aardman studio lighting`.
5. **Cutout / Collage *(Killer for IT & Cyber Comedy Shorts)*:** `flat paper cutout animation, layered construction paper and rough magazine edges, crisp drop shadows, punchy graphic simplicity, South Park / collage aesthetic`.
6. **Rotoscoping *(Killer for Dark Hacker Documentaries)*:** `rotoscope animation, traced live-action realism, bold inked outlines, flat high-contrast cel textures, surreal graphic-novel tension, A Scanner Darkly / Waking Life aesthetic`.
7. **Anime (Cyberpunk / Mecha / Shonen / J-Horror):** `cinematic Japanese cyberpunk anime frame, dramatic rim lighting, crisp cel shading, high-contrast neon atmosphere, expressive eyes, Satoshi Kon / Akira aesthetic`.
8. **Stylized 3D CGI Sub-Genres:** Specify exact sub-style — `low-poly 3D`, `voxel animation`, `hand-painted 3D (Arcane/Spider-Verse)`, `glitch CGI`, `1980s vector-lines 3D`, or `hyper-realistic raytraced 3D (Zack D. Films)`.
9. **Style Blending (Signature Mashups):** Combine a genre with an unexpected art movement (e.g., `Brutalist graphic novel + hacker thriller`, `Sumi-e ink wash + cyberpunk server room`, `1980s neon vector 3D + retro terminal`).
