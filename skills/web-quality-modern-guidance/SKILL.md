---
name: web-quality-modern-guidance
description: >-
  Modern web engineering, Core Web Vitals (LCP/INP/CLS), Lighthouse 95+, Next.js 16 (proxy.ts,
  use cache), React 19, Strict TS/Zod, Tailwind/shadcn/ui, Prisma/SQLite WAL, a11y, and JSON-LD
  hygiene (CT 115, hotel-suites.example.com). Use when auditing or refactoring web code and
  performance. Do NOT use for editorial art direction/URL DNA extraction (use
  editorial-web-design-studio), security pentesting (use code-security-audit), or WordPress/PHP
  ops (use wordpress-woocommerce-ops).
---

# ⚡ Modern Web Guidance & Web Quality Uzman Becerisi

Bu beceri; **GoogleChrome/modern-web-guidance** (Paul Irish) ve **addyosmani/web-quality-skills** standartlarını **hotel-suites.example.com**, **secops-domain.example.com** ve tüm web projelerinde uygulanabilir kalıcı mühendislik kurallarına dönüştürür.

---

## 🎯 1. Modern Web Primitifleri (Ağır JS Yerine Native Standartlar)

Kod yazarken veya mevcut siteyi düzeltirken eski/hantal JavaScript eklentileri yerine modern tarayıcı standartlarını tercih et:
1. **Native Modal & Popover:** Harici JS modal kütüphaneleri yerine HTML `<dialog>` ve `popover` API kullan.
2. **Modern CSS Düzeni:** Eski float/karmaşık flex hack'leri yerine `CSS Grid`, `Subgrid`, `clamp()` (akışkan tipografi) ve `Container Queries` kullan; `z-index` çakışmalarını CSS katmanlarıyla (`@layer`) veya temiz bir stacking context ile yönet.
3. **Resim ve Video Performansı:**
   - Her `<img>` etiketinde mutlaka geçerli `src`, anlamlı ve **benzersiz `alt`**, `width`/`height` (CLS önlemek için) ve ekran altı görsellerde `loading="lazy"` kullan.
   - `src=""` olan boş/hayalet `<img>` veya `<iframe>` etiketlerini asla DOM'da bırakma.
   - Kahraman (Hero) görselinde `fetchpriority="high"` kullan, mümkünse `WebP`/`AVIF` formatına dönüştür.
   - Harici videolarda kırık üçüncü parti indirme linkleri (`SaveClip`, vb.) yerine yerel optimize MP4/WebM + `poster` görseli kullan.

---

## 📊 2. Core Web Vitals & Lighthouse 95+ Kuralları

Bir site denetlendiğinde veya kodlandığında şu **4 metriği** zorunlu kontrol et:
1. **LCP (Largest Contentful Paint < 2.5s):** Hero alanı hızlı yüklenmeli; render-blocking CSS/JS ertelenmeli (`defer` / `async`).
2. **CLS (Cumulative Layout Shift < 0.1):** Resim, iframe, font ve dinamik widget'lar sonradan sayfayı kaydırmamalı (`font-display: swap`, sabit boyutlu konteynerler).
3. **INP (Interaction to Next Paint < 200ms):** Ana iş parçacığını (main thread) kilitleyen ağır animasyon, sahte popup toast döngüleri veya senkron script'lerden kaçın.
4. **Mobil Görünüm & İlk Ekran (Above-the-Fold CRO):**
   - `390x844` gibi standart mobil ekranlarda **ana başlık (H1) + birincil buton/CTA** kaydırma gerektirmeden ilk ekranda görünür olmalı.
   - Yüzen widget'lar (WhatsApp, Cookie banner, Dil seçici) birbiriyle veya form butonlarıyla üst üste binmemeli.

---

## 🌐 3. Çok Dilli Siteler & Çeviri Güvenliği (`GTranslate` / `Weglot` / Manuel)

1. **Bozulmaması Gereken Öğelere `notranslate` Ekle:**
   - Dil değiştirme butonları (`TR`, `EN`, `DE`, `RU`), marka adları (`Casa Turka`, `OPNsense`, `Proxmox`), şehir/özel isimler (`Dalaman`), ikonlar ve fiyat/kod alanları mutlaka `class="notranslate"` taşımalıdır.
2. **Tek Dil Tutarlılığı:**
   - Aynı sayfanın varsayılan halinde İngilizce ve Türkçe başlıklar birbirine karıştırılmamalıdır.
3. **Kırık / Boş Link Kontrolü:**
   - Hiçbir CTA butonu `href="#"` olarak bırakılmamalıdır; tüm aksiyon butonları gerçek bir hedefe (`wa.me/...`, `#section`, `/book`) bağlanmalıdır.

---

## 🔍 4. Teknik SEO, Erişilebilirlik & Yerel İşletme Hijyeni

1. **Temel Etiketler:** Her sayfada tek `<h1>`, benzersiz `<title>` (50–60 karakter), `<meta name="description">` (140–160 karakter) ve `<link rel="canonical">`.
2. **NAP Tutarlılığı (Name, Address, Phone):**
   - Web sitesi Footer, `Schema.org` JSON-LD (`LodgingBusiness` / `VacationRental` / `Organization`), Google İşletme Profili ve sosyal medya kanallarındaki **Adres ve Telefon** birebir aynı olmalıdır.
3. **Erişilebilirlik (A11y):**
   - Her buton ve ikonda erişilebilir etiket (`aria-label`), yeterli renk kontrastı ve klavye ile kapatılabilen overlay/hamburger menüler olmalıdır.

---

## 📋 5. Standart Denetim & Uygulama Çıktısı

Web sitesi incelemesi veya iyileştirmesi istendiğinde şu formatta rapor ver:
1. **Kritik Hatalar (🔴):** Kırık link/medya, mobil taşma, çeviri/UI çakışması, NAP/SEO uyumsuzluğu.
2. **Performans & Modern Standart Önerileri (🟡):** LCP/CLS/INP iyileştirmeleri ve eski JS yerine modern HTML/CSS çözümleri.
3. **Uygulanabilir Kod / Düzeltme Adımları (✅):** Doğrudan kopyalanabilir HTML/CSS/JS/JSON-LD yamaları.

---

## 🔄 6. Site Yeniden İnşa & Next.js 16 / React 19 / TS / Tailwind / Prisma-SQLite Standartları
*(vercel-labs/agent-skills `react-best-practices`, shadcn-ui/ui, wshobson `tailwind-design-system`, MengTo `tailwindcss`, resmi `prisma/skills`, `claude-mods/sqlite-ops` & `jeffallan/nextjs-developer` standartlarından uyarlanmıştır)*

`GolgeSiber-v3` (`CT 115`: Next.js 16 + React 19 + TypeScript + SQLite/Prisma + 22+ siber araç) veya yeni bir modern web ön yüzü geliştirileceğinde şu kuralları zorunlu uygula:
1. **Tailwind Tasarım Sistemi, Token & `shadcn/ui` Disiplini (`wshobson` + `MengTo` + `shadcn-ui/ui`):**
   - Renk paleti, tipografi (`clamp()`), boşluk, koyu/aydınlık tema (`dark:`) ve kırılma noktalarını (`390px` mobil, `1280px` masaüstü) `globals.css` / Tailwind v3–v4 semantik token'larına (`tailwind.config` / `@theme`) sabitle; bileşen içine rastgele hard-coded hex gömme.
   - Tekrar eden bileşen varyantlarında **`class-variance-authority` (CVA) + `cn()` (`clsx` + `tailwind-merge`)** kullan.
   - `shadcn/ui` bulunan projelerde mevcut **`components.json`** kurulumuna uy; erişilebilir Radix/shadcn primitiflerini kompozisyonla (`asChild`, klavye/ARIA tam destekli) kur.
   - Fontları harici Google Fonts `<link>` yerine **`next/font`** ile sıfır CLS ve gizlilikle (self-hosted) yükle.
2. **Next.js 16 & React 19 + Vercel React Performans Kuralları (`vercel-labs/react-best-practices`):**
   - **Next.js 16 Kırılan Değişiklikler:** `middleware.ts` yerine **`proxy.ts`**, dinamik **`params` ve `searchParams` her zaman `await` (async)**, eski örtük caching yerine açık **`"use cache"`** direktifi / Cache Components ve varsayılan **Turbopack**.
   - **React 19:** Kararlı **React Compiler** ile gereksiz manuel `useMemo`/`useCallback` kalabalığı yazma; form/mutasyonlarda **`useActionState`**, **`useOptimistic`**, **`useFormStatus`** ve `forwardRef` yerine doğrudan `ref` prop kullan.
   - **RSC-First:** Tüm bileşenleri varsayılan **React Server Components (RSC)** tut; `'use client'` yalnızca gerçekten tarayıcı etkileşimi/state gerektiren **en uç yaprak (leaf) bileşenlerde** kullanılır.
   - **Async Waterfall & Bundle Yasağı (Kritik):** Bağımsız sunucu veri çekimlerini **`Promise.all()` + `<Suspense>`** ile paralel çalıştır; barrel (`index.ts`) import yerine doğrudan yol importu ve ağır client modüllerde `next/dynamic` kullan.
   - **RSC Serialization & Re-Render:** RSC'den client'a yalnızca gereken minimum plain props geçir; türetilebilir state'te `useEffect` + `setState` kullanma; SEO'yu **`generateMetadata`**, görselleri **`next/image`**, sınırları **`loading.tsx` / `error.tsx`** ile kur.
3. **Strict TypeScript + Zod Girdi Güvenliği (22+ Siber Araç Koruması):**
   - `tsconfig.json` içinde `strict: true`, `noUncheckedIndexedAccess: true`, `verbatimModuleSyntax: true`; **`any` yasaktır** (`unknown` + type narrowing + discriminated unions).
   - Tüm API Route, Server Action ve siber araç girdilerini (IP, domain, CIDR, port, hash, regex) **`Zod` (`safeParse()` + `z.infer<typeof schema>`)** ile sunucu tarafında doğrula; özel RFC1918/loopback hedeflerine **SSRF**, karmaşık regex'lerde **ReDoS** ve shell çağrısında **Command Injection**'ı mutlak engelle.
4. **Prisma ORM + SQLite Üretim Disiplini (`prisma/skills` + `sqlite-ops`):**
   - Dev hot-reload bağlantı sızıntısını önlemek için tekil (`globalThis`) **Singleton `PrismaClient`** kullan.
   - Veritabanında kalıcı **`PRAGMA journal_mode=WAL;`** + `busy_timeout=5000` + `synchronous=NORMAL` aktif tut (`SQLITE_BUSY` / `"database is locked"` önlenir); arama/araç dizini için gerekirse **FTS5** kullan.
   - Şema değişikliğinde dev'de `prisma migrate dev`, üretimde (`CT 115`) **daima `npx prisma migrate deploy`** kullan — canlıda asla `db push --force-reset` çalıştırma!
5. **İçerik/Medya Temizliği & Canlı Tarayıcı Doğrulaması (Chrome DevTools):**
   - Eski kırık `src=""` görsellerini temizle, çok dillilikte GTranslate yerine JSON sözlük kullan.
   - Canlıya almadan önce kurulu **Chrome DevTools** (`chrome-devtools`, `debug-optimize-lcp`, `a11y-debugging`) ve (dev ortamında) Next.js 16 yerleşik **`/_next/mcp`** ile `390x844` ve `1280x800` çözünürlüklerinde LCP trace, `0` kırık görsel ve `0` konsol hatası testini geçir.

---

## 🎨 7. UI Eleştiri & "Anti-AI-Slop" Tasarım Denetimi
*(pbakaus/impeccable tasarım kalite çerçevesinden uyarlanmıştır — derin sanat yönetmenliği, DESIGN.md ve canlı URL tasarım DNA'sı sökümü için `editorial-web-design-studio` becerisini kullan)*

Yeni arayüz üretirken veya mevcut siteyi eleştirirken şu 4 "sıradan AI tasarımı" hatasını yakalayıp düzelt:
1. **Şablon Kart & Boşluk Simetrisi:** Yan yana duran kartların biri 3 satır diğeri 10 satır olup altta dev ölü boşluk bırakmasın; grid yüksekliğini ve iç dolguyu dengele.
2. **Jenerik Mor/Mavi Gradyan & Klişe İkon Yığını:** Marka kimliğiyle (`GölgeSiber` siber/nane yeşili, `Casa Turka` sıcak Akdeniz lüksü) alakasız varsayılan şablon renklerinden kaçın.
3. **Süslü ama İşlevsiz Widget Çakışması:** Yüzen butonlar, toast bildirimleri, cookie banner ve dil seçiciler asla CTA butonlarının veya form girişlerinin üstüne binmemeli.
4. **Mikro-Tipografi & Hizalama:** Telefon numaraları (`whitespace-nowrap`), fiyat birimleri ve rozetler ekran daraldığında satır ortasından çirkin şekilde kırılmamalı.
