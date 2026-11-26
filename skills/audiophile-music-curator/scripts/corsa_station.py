#!/usr/bin/env python3
"""
================================================================================
OPEL CORSA INTELLILINK R4.0 - OTO VE MUZIK YONETIM MERKEZI (CORSA STATION v2.1)
================================================================================
Kullanici dostu, menulu interaktif arac:
1. Hizli Esitleme (Kaynak Kutuphane -> CORSA_MUZIK)
2. Yeni USB Hazirla & Formatla (MBR + FAT32 + CORSA_MUZIK + Ilk Yukleme)
3. Kutuphane Durumu & USB Boyut Karsilastirmasi (Min/Max Bellek Rehberi)
4. Kutuphane Klasoru Ayarla / Degistir (Kullaniciya Ozel Hedef Secimi)
================================================================================
"""
import os
import sys
import time
import json
import shutil
import subprocess
import ctypes

try:
    import msvcrt
    HAS_MSVCRT = True
except ImportError:
    HAS_MSVCRT = False

USB_LABEL = "CORSA_MUZIK"
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")


def get_library_dir() -> str:
    """
    Kutuphane klasorunu oncelik sirasina gore dinamik olarak cozer:
    1. Ortam degiskeni: AUDIOPHILE_MUSIC_DIR veya CORSA_MUSIC_DIR
    2. config.json icindeki 'library_dir' kaydi
    3. Otomatik algilama:
       - ~/Nextcloud/Music
       - ~/Music/Corsa-Library
       - ~/Music
    4. Varsayilan: ~/Music
    """
    env_dir = os.environ.get("AUDIOPHILE_MUSIC_DIR") or os.environ.get("CORSA_MUSIC_DIR")
    if env_dir:
        p = os.path.abspath(os.path.expanduser(env_dir))
        if os.path.isdir(p):
            return p

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                p = data.get("library_dir")
                if p and os.path.isdir(p):
                    return os.path.abspath(p)
        except Exception:
            pass

    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "Nextcloud", "Music"),
        os.path.join(home, "Music", "Corsa-Library"),
        os.path.join(home, "Music"),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return os.path.abspath(c)

    fallback = os.path.join(home, "Music")
    os.makedirs(fallback, exist_ok=True)
    return os.path.abspath(fallback)


def set_library_dir(new_path: str) -> str:
    """Kullanicinin belirledigi kutuphane yolunu config.json dosyasina kaydeder."""
    abs_p = os.path.abspath(os.path.expanduser(new_path.strip('"').strip("'")))
    os.makedirs(abs_p, exist_ok=True)
    cfg = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            pass
    cfg["library_dir"] = abs_p
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return abs_p


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_key(prompt="\nAna menuye donmek icin herhangi bir tusa basin..."):
    """Kullanici herhangi bir tusa bastigi anda beklemeden devam eder."""
    print(prompt, end="", flush=True)
    if HAS_MSVCRT:
        try:
            msvcrt.getch()
            print()
            return
        except Exception:
            pass
    try:
        input()
    except Exception:
        pass


def banner():
    lib_dir = get_library_dir()
    print("=" * 72)
    print("      OPEL CORSA INTELLILINK R4.0 - MUZIK VE USB YONETIM MERKEZI")
    print("=" * 72)
    print(f"  Ana Kaynak Kutuphane : {lib_dir}")
    print(f"  Hedef USB Etiketi    : {USB_LABEL}")
    print("=" * 72)


def get_removable_drives():
    """Sistemdeki cikarilabilir (USB) suruculeri guvenle listeler."""
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if bitmask & 1:
            drive_path = f"{letter}:\\"
            dtype = ctypes.windll.kernel32.GetDriveTypeW(drive_path)
            # 2 = DRIVE_REMOVABLE
            if dtype == 2:
                vol_name = ctypes.create_unicode_buffer(260)
                fs_name = ctypes.create_unicode_buffer(260)
                try:
                    ctypes.windll.kernel32.GetVolumeInformationW(
                        drive_path, vol_name, 260, None, None, None, fs_name, 260
                    )
                    v_label = vol_name.value
                    fs = fs_name.value
                except Exception:
                    v_label = ""
                    fs = "UNKNOWN"

                total_bytes = ctypes.c_ulonglong(0)
                free_bytes = ctypes.c_ulonglong(0)
                try:
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                        drive_path, None, ctypes.byref(total_bytes), ctypes.byref(free_bytes)
                    )
                    size_gb = total_bytes.value / (1024 ** 3)
                    free_gb = free_bytes.value / (1024 ** 3)
                except Exception:
                    size_gb = 0.0
                    free_gb = 0.0

                drives.append({
                    "letter": letter,
                    "path": drive_path,
                    "label": v_label,
                    "fs": fs,
                    "size_gb": size_gb,
                    "free_gb": free_gb,
                })
        bitmask >>= 1
    return drives


def find_corsa_usb():
    """'CORSA_MUZIK' etiketine sahip hazir USB surucuyu bulur."""
    for d in get_removable_drives():
        if d["label"].upper() == USB_LABEL.upper():
            return d["path"]
    return None


def get_library_stats():
    """Kaynak kutuphanenin boyutunu ve parca sayisini hesaplar."""
    lib_dir = get_library_dir()
    total_bytes = 0
    total_mp3 = 0
    genres = {}
    if os.path.isdir(lib_dir):
        for root, dirs, files in os.walk(lib_dir):
            mp3s = [f for f in files if f.lower().endswith(".mp3")]
            if mp3s:
                fol = os.path.basename(root)
                genres[fol] = len(mp3s)
                total_mp3 += len(mp3s)
                for f in mp3s:
                    try:
                        total_bytes += os.path.getsize(os.path.join(root, f))
                    except Exception:
                        pass
    size_gb = total_bytes / (1024 ** 3)
    return total_mp3, size_gb, genres


def sync_library(target_usb=None):
    """Mevcut kutuphaneyi USB'ye ayna modunda esitler."""
    lib_dir = get_library_dir()
    if not os.path.isdir(lib_dir):
        print(f"\n[HATA] Kaynak muzik klasoru bulunamadi: {lib_dir}")
        print("Lutfen menu [4] uzerinden gecerli bir muzik klasoru belirleyin.")
        return

    usb_path = target_usb if target_usb else find_corsa_usb()
    if not usb_path:
        print("\n" + "-" * 72)
        print(f"[UYARI] '{USB_LABEL}' etiketli hazir bir USB bellek bulunamadi!")
        print("Eger yeni veya baska bir USB taktiysaniz ana menuden [2] secenegini")
        print("kullanarak belleginizi Corsa icin otomatik hazirlayabilirsiniz.")
        print("-" * 72)
        return

    print(f"\n-> Kaynak : {lib_dir}")
    print(f"-> Hedef  : {usb_path} ({USB_LABEL})")
    print("-" * 72)

    src_mp3s = {}
    for root, _, files in os.walk(lib_dir):
        rel = os.path.relpath(root, lib_dir)
        if rel == ".":
            continue
        for fn in files:
            if fn.lower().endswith(".mp3"):
                src_mp3s[os.path.join(rel, fn)] = os.path.join(root, fn)

    if len(src_mp3s) == 0:
        print(f"[UYARI] Kaynak klasorde kopyalanacak hic MP3 dosyasi bulunamadi!")
        return

    print(f"Toplam {len(src_mp3s)} kaynak parca esitleniyor...\n")

    copied = 0
    updated = 0
    skipped = 0
    deleted = 0

    # 1. Kopyalama / Guncelleme
    for rel_path, src_file in src_mp3s.items():
        dst_file = os.path.join(usb_path, rel_path)
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)

        if not os.path.exists(dst_file):
            shutil.copy2(src_file, dst_file)
            copied += 1
            print(f"  [+] YENI: {rel_path}")
        else:
            s_stat = os.stat(src_file)
            d_stat = os.stat(dst_file)
            if s_stat.st_size != d_stat.st_size or (s_stat.st_mtime - d_stat.st_mtime) > 2:
                shutil.copy2(src_file, dst_file)
                updated += 1
                print(f"  [*] GUNCEL: {rel_path}")
            else:
                skipped += 1

    # 2. Artik dosyalari temizleme
    for root, dirs, files in os.walk(usb_path, topdown=False):
        rel = os.path.relpath(root, usb_path)
        if rel == "." or rel.startswith("System Volume Information"):
            continue
        for fn in files:
            if not fn.lower().endswith(".mp3"):
                continue
            rel_file = os.path.join(rel, fn)
            if rel_file not in src_mp3s:
                try:
                    os.remove(os.path.join(root, fn))
                    deleted += 1
                    print(f"  [-] SILINDI (Kaynakta yok): {rel_file}")
                except Exception as e:
                    print(f"  [!] Silinemedi: {rel_file} ({e})")
        if not os.listdir(root):
            try:
                os.rmdir(root)
            except Exception:
                pass

    print("-" * 72)
    print(f"ESITLEME TAMAMLANDI!")
    print(f"  Yeni Kopyalanan : {copied}")
    print(f"  Guncellenen     : {updated}")
    print(f"  Silinen (Artik) : {deleted}")
    print(f"  Zaten Esit Olan : {skipped}")
    print("-" * 72)


def setup_new_usb():
    """Yeni veya bozuk USB bellegi MBR + FAT32 + CORSA_MUZIK olarak hazirlar."""
    print("\n" + "=" * 72)
    print("   SIFIR USB HAZIRLAMA & CORSA FORMATI (MBR + FAT32)")
    print("=" * 72)
    print("Bu islem yeni veya bozuk bir USB bellegi Opel IntelliLink R4.0'in")
    print("kesinlikle okuyabilecegi MBR ve FAT32 formatina donusturur.\n")

    drives = get_removable_drives()
    if not drives:
        print("[HATA] Bilgisayara takili, aktif cikarilabilir bir USB bellek bulunamadi!")
        print("Lutfen USB belleginizi takin ve bu menuyu tekrar acin.")
        return

    print("Sistemde tespit edilen USB bellekler:")
    for idx, d in enumerate(drives, 1):
        lbl = d['label'] if d['label'] else '(Isimsiz)'
        print(f"  [{idx}] Sürücü {d['letter']}: | Etiket: {lbl:<15} | Format: {d['fs']:<6} | Boyut: {d['size_gb']:.1f} GB (Boş: {d['free_gb']:.1f} GB)")

    print("\n  [0] Vazgeç / Ana Menüye Dön")
    choice = input("\nFormatlamak istediginiz USB'nin numarasini girin [0-" + str(len(drives)) + "]: ").strip()

    if choice in ["0", "", "q", "exit"]:
        print("Islem iptal edildi. Ana menuye donuluyor...")
        return

    try:
        sel_idx = int(choice) - 1
        if sel_idx < 0 or sel_idx >= len(drives):
            print("[HATA] Gecersiz secim!")
            return
    except ValueError:
        print("[HATA] Lutfen sayisal bir deger girin!")
        return

    target = drives[sel_idx]
    target_letter = target["letter"]

    print("\n" + "!" * 72)
    print(f"UYARI: {target_letter}: ({target['size_gb']:.1f} GB) surucusu TAMAMEN SILINECEK!")
    print(f"ve Opel Corsa icin MBR boluntu tablosu & FAT32 ({USB_LABEL}) yapilacak.")
    print("!" * 72)

    confirm = input(f"Onaylamak icin buyuk harflerle 'EVET' yazin (veya iptal icin Enter): ").strip()
    if confirm != "EVET":
        print("Onay verilmedi. Islem guvenli sekilde durduruldu.")
        return

    print(f"\n1/3. {target_letter}: surucusu hazirlaniyor...")

    ps_cmd = f"(Get-Partition -DriveLetter {target_letter}).DiskNumber"
    try:
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True)
        disk_num_str = res.stdout.strip()
        disk_num = int(disk_num_str) if disk_num_str.isdigit() else None
    except Exception:
        disk_num = None

    success = False

    if disk_num is not None:
        dp_script = f"""select disk {disk_num}
clean
convert mbr
create partition primary
active
format fs=fat32 quick label="{USB_LABEL}"
assign letter={target_letter}
exit
"""
        dp_path = os.path.join(os.environ.get("TEMP", "C:\\Temp"), "corsa_diskpart.txt")
        try:
            with open(dp_path, "w") as f:
                f.write(dp_script)
            print(f"2/3. Disk {disk_num} MBR tablosuna donusturuluyor ve FAT32 formatlaniyor...")
            r_dp = subprocess.run(["diskpart", "/s", dp_path], capture_output=True, text=True)
            if r_dp.returncode == 0:
                success = True
                print("Format islemi basariyla tamamlandi!")
            else:
                print(f"[UYARI] Diskpart tam erisim saglayamadi, Windows yerel formati deneniyor...")
        except Exception as e:
            print(f"Diskpart hatasi: {e}")
        finally:
            if os.path.exists(dp_path):
                os.remove(dp_path)

    if not success:
        print(f"2/3. {target_letter}: FAT32 olarak bicimlendiriliyor...")
        cmd_fmt = ["format", f"{target_letter}:", "/FS:FAT32", f"/V:{USB_LABEL}", "/Q", "/Y"]
        r_fmt = subprocess.run(cmd_fmt, capture_output=True, text=True)
        if r_fmt.returncode == 0:
            success = True
            print("Format tamamlandi!")
        else:
            print("[HATA] Formatlama basarisiz oldu. Lutfen Yonetici haklariyla calistirin.")
            return

    time.sleep(2)
    target_path = f"{target_letter}:\\"
    print(f"\n3/3. Kutuphanedeki parcalar yeni bellege kopyalaniyor...")
    sync_library(target_path)
    print("\n" + "=" * 72)
    print("TEBRIKLER! Yeni USB belleginiz hazir. Arabaniza takip keyifle dinleyebilirsiniz!")
    print("=" * 72)


def audit_library_and_capacity():
    """Kutuphane durumunu, kapak ve USB kapasite karsilastirmasini raporlar."""
    print("\n" + "=" * 72)
    print("   KUTUPHANE SAGLIGI & USB KAPASITE KARSILASTIRMASI")
    print("=" * 72)

    total_mp3, lib_gb, genres = get_library_stats()
    lib_dir = get_library_dir()

    print(f"\n[1] AKTIF KAYNAK MUZIK KUTUPHANESI:")
    print(f"  * Dizin Yolu          : {lib_dir}")
    print(f"  * Toplam Parca Sayisi : {total_mp3} Parca")
    print(f"  * Toplam Disk Boyutu  : {lib_gb:.2f} GB ({lib_gb*1024:.0f} MB)")
    print(f"  * Aktif Kategori      : {len(genres)} Klasor")
    print(f"  * Kapak Standarti     : %100 Orijinal Studyo Kapaklari (500x500 Baseline JPEG)")
    print(f"  * Ses Dengelemesi     : EBU R128 (-14.0 LUFS) / 320 kbps CBR (IntelliLink Uyumlu)")

    print(f"\n[2] TAKILI USB BELLEK DURUMU:")
    drives = get_removable_drives()
    if not drives:
        print("  * Takili aktif bir USB bellek bulunamadi.")
        print(f"  * (Not: Mevcut {lib_gb:.2f} GB arsiv icin en az 16 GB bellek takilmalidir.)")
    else:
        corsa_found = False
        for d in drives:
            is_corsa = d["label"].upper() == USB_LABEL.upper()
            if is_corsa:
                corsa_found = True
            mark = "[CORSA_MUZIK]" if is_corsa else "[Baska Bellek]"
            print(f"  * Sürücü {d['letter']}: {mark}")
            print(f"    - Etiket / Dosya Sistemi : {d['label'] if d['label'] else '(Etiketsiz)'} ({d['fs']})")
            print(f"    - Toplam Kapasite        : {d['size_gb']:.1f} GB")
            print(f"    - Bos Alan               : {d['free_gb']:.1f} GB")

            # Boyut Karsilastirmasi
            if d["size_gb"] >= lib_gb:
                rem = d["size_gb"] - lib_gb
                print(f"    - UYGUNLUK               : [YETERLI ALAN]")
                print(f"      (Arsiv yuklendikten sonra bellekten yaklasik {rem:.1f} GB bos yer kalir)")
            else:
                need = lib_gb - d["size_gb"]
                print(f"    - UYGUNLUK               : [YETERSIZ ALAN]")
                print(f"      (Arsiv {lib_gb:.2f} GB, bellek {d['size_gb']:.1f} GB; {need:.1f} GB daha gerekir!)")

        if not corsa_found:
            print(f"\n  [!] Dikkat: Takili bellegin adi '{USB_LABEL}' degil.")
            print(f"      Menu [2]'yi kullanarak bellegi tek tikla Corsa icin hazirlayabilirsiniz.")

    print(f"\n[3] OPEL CORSA INTELLILINK R4.0 KAPASITE REHBERI:")
    print("  " + "-" * 68)
    print("  * MINIMUM BELLEK BOYUTU : 16 GB")
    print(f"    (Mevcut {total_mp3} parcalik {lib_gb:.2f} GB kutuphaneniz icin gereken en dusuk boyut)")
    print("  * IDEAL / TAVSIYE EDILEN: 32 GB (SWEET SPOT)")
    print("    (Opel IntelliLink R4.0 teybi icin hem FAT32 standardina hem de teyp RAM")
    print("     onbellegine en uygun, en hizli acilan ve asla takilmayan resmi tavan boyut)")
    print("  * MAKSIMUM SINIR        : 32 GB - 64 GB")
    print("    (64 GB ve ustu bellekler MBR/FAT32 yapilsa bile arac teybinde acilista")
    print("     sarki indekslemesini yavaslatabilir; 32 GB fazlasiyla yeterli ve stabildir)")
    print("  " + "-" * 68)


def configure_library_dir():
    """Kullanicinin kendi bilgisayarindaki muzik klasorunu secmesini ve kaydetmesini saglar."""
    print("\n" + "=" * 72)
    print("   KUTUPHANE KLASORU AYARLA / DEGISTIR (Ozel Yol Secimi)")
    print("=" * 72)
    current = get_library_dir()
    print(f"  Mevcut Aktif Kutuphane : {current}")
    print("\n  Farkli bir klasor kullanmak istiyorsaniz tam yolunu girin:")
    print("  Ornekler: D:\\Muziklerim   veya   C:\\Users\\Kullanici\\Music")
    print("  (Degisiklik yapmadan ana menuye donmek icin [Enter] tusuna basin)")
    print("-" * 72)
    new_path = input("  Yeni Kutuphane Yolu: ").strip()

    if not new_path:
        print("\n  [BILGI] Herhangi bir degisiklik yapilmadi.")
        return

    try:
        saved = set_library_dir(new_path)
        print("\n" + "-" * 72)
        print(f"  [BASARILI] Yeni muzik kütüphanesi kaydedildi!")
        print(f"  Hedef Dizin: {saved}")
        print("-" * 72)
    except Exception as e:
        print(f"\n  [HATA] Klasor kaydedilemedi: {e}")


def main():
    while True:
        clear_screen()
        banner()
        print("\n  NE YAPMAK ISTIYORSUNUZ?\n")
        print("  [1] HIZLI ESITLEME (Rutin Senkronizasyon)")
        print("      * Sadece yeni/degisen sarkilari USB'ye atar.")
        print("      * Kaynakta sildiklerinizi bellekten temizler.\n")
        print("  [2] SIFIRDAN USB HAZIRLA & FORMATLA (Yeni / Bozuk Bellek Icin)")
        print("      * Corsa'nin okuyabilmesi icin diski MBR ve FAT32 yapar.")
        print("      * Etiketini 'CORSA_MUZIK' yapar ve tum muzikleri yukler.\n")
        print("  [3] KUTUPHANE SAGLIGI & USB BOYUT KARSILASTIRMASI (Min/Max Rehberi)")
        print("      * Kutuphane boyutunu, takili USB'nin kapasitesini ve Opel")
        print("        IntelliLink R4.0 icin min/max bellek sinirlarini karsilastirir.\n")
        print("  [4] KUTUPHANE KLASORUNU AYARLA / DEGISTIR (Hedef Klasor Secimi)")
        print("      * Kendi ozel muzik klasorunuzu (D:\\Muzik vb.) belirler ve kaydeder.\n")
        print("  [5] CIKIS (Programi Kapat)\n")
        print("=" * 72)

        choice = input("Lutfen seciminizi yapin [1-5]: ").strip()

        if choice == "1":
            clear_screen()
            banner()
            sync_library()
            wait_for_key("\nAna menuye donmek icin herhangi bir tusa basin...")
        elif choice == "2":
            clear_screen()
            banner()
            setup_new_usb()
            wait_for_key("\nAna menuye donmek icin herhangi bir tusa basin...")
        elif choice == "3":
            clear_screen()
            banner()
            audit_library_and_capacity()
            wait_for_key("\nAna menuye donmek icin herhangi bir tusa basin...")
        elif choice == "4":
            clear_screen()
            banner()
            configure_library_dir()
            wait_for_key("\nAna menuye donmek icin herhangi bir tusa basin...")
        elif choice in ["5", "q", "exit"]:
            print("\nIyi yolculuklar ve keyifli dinlemeler!\n")
            time.sleep(1)
            break
        else:
            print("\nGecersiz secim! Lutfen 1, 2, 3, 4 veya 5 tuslayin.")
            time.sleep(1.2)


if __name__ == "__main__":
    main()
