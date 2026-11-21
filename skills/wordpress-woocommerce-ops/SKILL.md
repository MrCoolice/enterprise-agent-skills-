---
name: wordpress-woocommerce-ops
description: >-
  WordPress & WooCommerce operations, safe www-data WP-CLI maintenance, HPOS, PHP 8.4-FPM,
  caching/WebP, and custom plugin security (golge-watermark, golge-isbn, golge-nadir-import) for
  GolgeKitabeviWP (CT 113, ecommerce.example.com). Use when running WP-CLI, optimizing WooCommerce,
  or hardening WP plugins. Do NOT use for Next.js/CWV engineering (use
  web-quality-modern-guidance), SEO blog writing (use seo-content-master), or LXC backups (use
  proxmox-ve-ops).
---

# 📚 WordPress & WooCommerce Operasyon, WP-CLI & Güvenlik Becerisi

Bu beceri; resmi **WordPress/agent-skills** (`wp-wpcli-and-ops`, eklenti güvenlik standartları) ve resmi **woocommerce/agent-skills** (HPOS, modern Blocks ve servis standartları) rehberlerini **`GolgeKitabeviWP` (`LXC 113` — `ecommerce.example.com`)** altyapısına özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **WordPress/WooCommerce uygulama bakımı, güvenli `WP-CLI`, PHP 8.4-FPM/veritabanı/önbellek hızlandırma ve özel eklenti güvenliği** içindir. Genel Core Web Vitals/Next.js için `web-quality-modern-guidance`, SEO makale/şema yazımı için `seo-content-master`, LXC/PBS yedeği için `proxmox-ve-ops`, 502/SSL arızası için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik, Yedekleme ve WP-CLI Güvenlik Kuralları

1. **Veritabanı / Toplu Değişiklik Öncesi Zorunlu Yedek (FAZ 0):** `wp search-replace`, eklenti/çekirdek güncelleme, toplu kategori/görsel betiği veya HPOS geçişi öncesi daima `wp db export` (sıkıştırılmış yerel yedek) + gerekirse `CT 113` snapshot alınır.
2. **WP-CLI Kullanıcı Kuralı:** `wp` komutlarını `root` ile `--allow-root` basarak dosya sahipliğini bozma; her zaman web kullanıcısıyla (`sudo -u www-data wp --path=/var/www/html/wordpress ...`) çalıştır.
3. **Kimlik Bilgisi Hijyeni:** `wp-config.php` DB parolaları, auth salt'ları, WooCommerce REST `ck_`/`cs_` anahtarları ve SMTP parolaları asla yanıta veya git reposuna yazılmaz (`[MASKED]`).

---

## 🧭 1. `GolgeKitabeviWP` (`CT 113`) Altyapı Bağlamı

- **Sunucu & Repo:** `LXC 113` (`10.10.10.113`, VLAN 20 WEB, 4 vCPU, 2 GB RAM, 25 GB Disk — ~18 GB boş), Repo: `admin_user/golgekitabevi-wp`, Kök: `/var/www/html/wordpress`, Runtime: **PHP 8.4-FPM**.
- **Aktif Performans Yığını:** `WP Fastest Cache` (`44ms` hedefi) + `WebP Express` (`CDN friendly` `<picture>` modu) + yeni yüklemelerde **`1400px` otomatik görsel küçültme koruması** (TBW & disk şişmesi önleme).
- **Özel Modüller:** `golge-watermark`, `golge-nadir-import`, `golge-isbn`, `stats-ajax`, UTF-8 `llms.txt` ve KVKK/Gizlilik/Çerez sayfaları.

---

## 🛠️ 2. Resmi `WP-CLI` Bakım, Veritabanı & Katalog Disiplini
*(Resmi `WordPress/agent-skills` `wp-wpcli-and-ops` kurallarından uyarlanmıştır)*

### A. Salt-Okunur Sağlık & Hijyen Taraması (Önce Oku)
```bash
WP="sudo -u www-data wp --path=/var/www/html/wordpress"
$WP core verify-checksums
$WP plugin status
$WP option list --autoload=on --format=total_bytes
$WP cron event list --fields=hook,next_run_relative
$WP transient list --format=count
```
- **Autoload Eşiği:** `wp_options` autoload toplamı **`800 KB`–`1 MB`** üstüne çıkarsa en büyük 10 satırı tespit edip temizle/autoload kapat (her sayfa yükünde PHP bellek ve TTFB'yi doğrudan etkiler).

### B. Güvenli Arama-Değiştirme & Toplu İşlem Kuralı
- `wp search-replace` **her zaman önce `--dry-run` ile** çalıştırılır; serileştirilmiş (serialized) PHP dizilerini bozmamak için doğrudan SQL `UPDATE` yerine daima WP-CLI kullanılır.
- Büyük katalog/görsel işlerinde (`golge-nadir-import` vb.) bellek taşmasını (`2 GB RAM`) önlemek için batch (ör. 200'lük parçalar) + `wp_cache_flush()` kullan; yükleme anında `1400px` sınırı ve WebP uyumu korunmalıdır.

---

## 🛒 3. Modern WooCommerce & Özel Eklenti Güvenlik Standartları
*(Resmi `woocommerce/agent-skills` & `WordPress/agent-skills` kurallarından uyarlanmıştır)*

1. **HPOS (High-Performance Order Storage) Uyumu:** Yeni veya güncellenen her kodda eski `wp_posts` / `get_post_meta()` sipariş sorguları yerine resmi **`wc_get_orders()` / `$order->get_meta()` CRUD API** kullanılır (`FeaturesUtil::declare_compatibility('custom_order_tables', ...)`).
2. **Özel Eklenti & AJAX Güvenlik Kapısı (`golge-*`, `stats-ajax`):**
   - Her form/AJAX isteğinde **`check_ajax_referer()` / `wp_verify_nonce()`** doğrulaması,
   - Yetkili işlemlerde **`current_user_can()`** kontrolü,
   - Girdide `sanitize_text_field()` / `absint()`, SQL'de daima **`$wpdb->prepare()`**, çıktıda **`esc_html()` / `esc_attr()` / `esc_url()`** zorunludur.
   - Public AJAX uçlarında (`stats-ajax`, favori ekleme) IP/oturum bazlı **rate-limit** korunur.
3. **WordPress Zırhlama Kontrol Listesi:**
   - `DISALLOW_FILE_EDIT` = `true` (`wp-config.php`), `xmlrpc.php` kapalı (Cloudflare WAF + Nginx), `WP_DEBUG_DISPLAY` = `false` (üretimde hata ekrana basılmaz), yönetici 2FA aktif, `wp-content/uploads/` içinde PHP yürütmesi engelli.
   - **Cron & Cache:** `DISABLE_WP_CRON` = `true` yapılıp gerçek Debian **System Cron** (`*/5 * * * *`) kullanılır; `WP Fastest Cache` değişimlerinde Cloudflare cache uyumu doğrulanır.

---

## 📋 4. Standart WordPress Operasyon Çıktı Formatı

1. **Ön Koşul & Yedek (FAZ 0):** `wp db export` / `CT 113` snapshot gereksinimi ve RAM/disk (`1400px` kuralı) etkisi.
2. **Uygulanabilir `WP-CLI` / PHP / Nginx Adımları:** Önce `--dry-run` veya salt-okunur tanı, ardından güvenli uygulama.
3. **Doğrulama:** `wp core verify-checksums`, TTFB / HTTP 200 kontrolü, `error.log` taraması ve `WP Fastest Cache` önbellek yenileme teyidi.
