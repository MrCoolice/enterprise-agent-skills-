<!-- BEGIN:universal-agent-rules -->
# 🛡️ GölgeSiber Kurumsal Ajan Direktifleri ve Çalışma Standardı

Bu proje ve altındaki tüm sohbet pencereleri aşağıdaki evrensel standartlara bağlıdır:

1. **Dil Standardı:** Kullanıcı aksini istemedikçe HER ZAMAN akıcı, teknik açıdan yetkin ve doğal Türkçe kullan. Yapay zeka kalıplarından arındırılmış konuş.
2. **Yerel Ortam ve Doğrulama:**
   - Python 3.12: `C:\Users\MrCoolice\AppData\Local\Programs\Python\Python312\python.exe`
   - Node.js & npm: `C:\Program Files\nodejs\node.exe`
   - Blender 5.3: `C:\Program Files\Blender Foundation\Blender 5.3\blender.exe`
   - GPU / VRAM: NVIDIA GeForce RTX 4070 (12 GB VRAM, Ada Lovelace, Compute Cap 8.9)
   - Yerel AI Servisleri: Ollama (11434 - deepseek-r1:14b, qwen2.5-coder:14b), Antigravity Gateway (51001)
3. **Kör Kodlama Yapma:** Kod yazdıktan sonra projeyi derle veya lint testini çalıştır; hata olmadığından emin olmadan işi bitirme.
4. **Hafıza & Mimari:** Kalıcı mimari haritası `ARCHITECTURE.md` dosyasındadır. Değişiklik yaptığında tarihi güncelle.
5. **Akıllı Model Seçimi ve Görev Hiyerarşisi (Pragmatik Mühendislik Prensibi):**
   - **TİER S (Kritik Kodlama, Hata Ayıklama & Mimari):** Asla sırf bedava olsun diye küçük modellere kaçma. Next.js 16, TypeScript, Proxmox ZFS, OPNsense, güvenlik açığı avı ve vergi/muhasebe hesaplarında doğrudan **EN YETKİN PRO / SOTA MODELİ** (Google Gemini 2.5 Pro / Claude 3.7 Sonnet / NVIDIA NIM Llama-70B) kullan. Bir kerede hatasız ve sağlam kod üretmek saatler sürecek debug işkencesinden ucuzdur.
   - **TİER A (Rutin Sistem, Bot, Bash & Müzik Analizi):** Yerel NVIDIA RTX 4070 üzerindeki **Ollama (`qwen2.5-coder:14b` & `deepseek-r1:14b`)** modelini kullan. Eğer Ollama kapalıysa bedava `flash_lite` alt ajanına geç ($0 maliyet, yerel gizlilik).
   - **TİER B (Metin Taslağı, SEO & Sosyal Medya):** Hız ve sıfır gecikme için buluttaki **Gemini 2.5 Flash-Lite** kullan ($0 kota tasarrufu).
   - **TİER GPU (3D, Video & Render):** Doğrudan yerel donanımın **RTX 4070 OptiX CUDA (Blender)** ve **NVENC (Video/Remotion/FFmpeg)** donanım hızlandırmasını kullan.
<!-- END:universal-agent-rules -->
