---
name: quiz-word-game-master
description: >-
  Web & mobile game engineering studio for GolGeSiber Quiz/Trivia, Word Games (Turkish/TDK),
  Memory puzzles, and 2D HTML5 Canvas arcade games (state machines, distractors, Web Audio FX,
  haptics, retention). Use when building or upgrading browser games or game mechanics. Do NOT
  use for general websites/art direction (use editorial-web-design-studio), Next.js/Prisma site
  CWV audits (use web-quality-modern-guidance), or Steam library management (use
  steam-library-assistant).
---

# 🎮 GölgeSiber Game Studio Master (Evrensel Web & Mobil Oyun Mimarı)

Bu beceri; **Bilgi Yarışması (Quiz/Trivia)**, **Kelime Bulmaca & Anagram**, **Hafıza/Kart Eşleştirme** ve **2D HTML5 Canvas/Arcade** oyunları geliştiren stüdyolar için uçtan uca oyun mühendisliği, algoritmik adalet, ses/dokunma hissi ("juice") ve oyuncu bağlılığı standartlarını tek çatı altında toplar.

---

## 🧭 1. Temel Oyun Tasarımı ve Denge Prensipleri

### 1.1 Zorluk Eğrisi: Testere Dişi Pacing Kuralı (Saw-Tooth Curve)
* **Doğrusal Zorluk Tuzağı (Anti-Pattern):** Seviye 1'den 100'e dümdüz artan zorluk zihinsel yorgunluk (*cognitive fatigue*) yaratır ve terk edilmeye (*churn*) yol açar.
* **Altın Standart (Testere Dişi Dalga Eğrisi):** Oyun her 10-15 seviyede bir dalgalı bir ritim izler:
  1. **Isınma (Warmup):** Rahat, akıcı, dopamin toplatır.
  2. **Tırmanış (Ramp):** Soru zorlaşır, harf veya kart sayısı artar.
  3. **Zirve / Boss Etabı:** Büyük meydan okuma, dar süre, zorlayıcı soru/kelime.
  4. **Nefes Alma & Şölen (Breather / Reward):** Zirveyi aşan oyuncuya hemen ardından gelen kolay, bol bonuslu ferahlatıcı seviye. Oyuncu rahatlar ve oyunu bırakamaz!

### 1.2 "Anti-Slop" Dokunsal Oyun Hissi ve 60 FPS Hareket Standartları (Game Juice & 60fps.design)
* **Yasak:** Yapay zekanın sıkıcı "mor-indigo SaaS kartları" ve donuk statik tıklamalar yasaktır.
* **Akıcı 60 FPS Yaylanma Fiziği (`60fps.design` İlkesi):** 
  - Harf ve kart seçimlerinde doğrusal (linear) animasyon kullanılmaz; `cubic-bezier(0.34, 1.56, 0.64, 1)` (spring/bounce) elastik geçişleri zorunludur.
  - Kart çevirme (flip): GPU-accelerated `transform: perspective(1000px) rotateY(180deg)` ile 60 FPS akışkanlık.
* **Tepki ve Haptik Geri Bildirim:**
  - Yanlış cevap: 300ms sönümlenen mikro sarsıntı (`translateX(-8px) -> translateX(8px)` sönümlü sinüs dalgası).
  - Doğru cevap: Hafif büyüme (`scale(1.08)`), ardışık basamaklı (staggered) harf animasyonu ve Web Audio tatmin edici tık/zil efekti.
* **Kutlama Parçacıkları (Particle Burst):** Doğru cevap ve seviye sonlarında DOM'u kasmayan hafif HTML5 Canvas tabanlı 60 FPS neon parçacık veya konfeti patlaması.
* **Mobilde Başparmak Ergonomisi:** Minimum 48x48px dokunma hedefleri, safe area uyumu.

---

## 🛠️ 2. Dört Temel Çalışma Modu (Modes of Operation)

Bu beceri, ajan çağrıldığında kullanıcının ihtiyacına göre şu 4 moddan birinde tam otonom hareket eder:

### 🧩 Mod A: Trivia & Quiz Soru Fabrikası (`trivia-anti-bias-generator`)
* **Ne Zaman Kullanılır:** Yeni quiz kategorileri (JSON) oluştururken veya mevcut soruları genişletirken.
* **Katı Şık Eşitliği Kuralı:** Doğru şık, yanlış şıkların ortalama karakter uzunluğundan en fazla **1.25 kat** uzun olabilir. Uzunsa çeldiriciler zenginleştirilir veya doğru şık sadeleştirilir.
* **Tembel Çeldirici Yasağı:** *"Yukarıdakilerin hepsi"*, *"Hiçbiri"* veya bariz alakasız saçma şıklar kesinlikle yasaktır; çeldiriciler konuyu yarım bilen birinin en sık düşeceği kavram yanılgılarını (*misconceptions*) hedefler.
* **Trivia Ayrımı:** Doğru şıkkı açıklayıcı ek ansiklopedik bilgi doğrudan `trivia` alanına taşınır; şıkkın içine gömülmez.
* **Dengeli Cevap İndeksi:** `correctAnswer` (0, 1, 2, 3) indeksleri eşit dağıtılır (her biri ~%25).
* **Boss Soru Ritim Dağılımı:** 12 soruluk sette 4. ve 8. sorular `mini-boss`, 12. soru ise yüksek puanlı ve dar süreli `final-boss` olmalıdır.

### 🔤 Mod B: Kelime & Anagram Seviye Mühendisi (`puzzle-generator-skill`)
* **Ne Zaman Kullanılır:** Kelime bulmaca seviyeleri (`levels.ts`) üretirken veya sözlük eklerken.
* **76.000 Kelimelik TDK Uyumu:** Yalnızca TDK sözlüğünde (`tdk_words_76k.txt`) yer alan meşru Türkçe kökler ve türetimler kullanılır. Argo veya geçersiz uydurma kelimeler elenir.
* **Sesli-Sessiz Harf Dengesi:** Verilen harf havuzu asla çözümsüz veya boğucu olamaz; en az 2 sesli harf ve akıllı karıştırma (`smartShuffleLetters`) kuralı uygulanır.
* **Hedef ve Bonus Kelimeler:** Ana ızgarada yer alan hedef kelimelerin yanı sıra, o harflerden türetilebilen geçerli diğer sözlük kelimeleri `bonusWords` havuzuna kaydedilir ve oyuncuya ekstra puan verir.

### 🤖 Mod C: Otonom QA Playtester & Denge Denetimi (`game-qa-playtester`)
* **Ne Zaman Kullanılır:** Oyun yayınlanmadan veya seviye paketi güncellendikten sonra denetim için.
* **Headless Regresyon Denetimi:** `scripts/audit-quiz-balance.mjs` ve `scripts/audit-wordgame.mjs` test motorlarını çalıştırır.
* **Hata ve Çıkmaz (Deadlock) Tespiti:** 
  - Çözülemeyen anagram veya eksik harf kombinasyonlarını yakalar.
  - Şık bias'ı (sürekli C şıkkının doğru olması veya doğru şıkkın hep bariz uzun olması) durumunda alarm verir.
  - UTF-8 Türkçe karakter bozulmalarını (*Mojibake: `Ã§`, `Ä±` vb.*) otomatik tespit eder ve temizler.

### 🚀 Mod D: Viral Tutundurma & Story Kart Motoru (`viral-loop-engine`)
* **Ne Zaman Kullanılır:** Oyuncu skor kartı, sosyal medya paylaşımı veya unvan tasarımlarında.
* **1080x1920 Dikey Story Kartı:** HTML5 Canvas veya Remotion ile oyuncunun CyberRank unvanını, hız bonusunu ve çözdüğü soruları gösteren yüksek kontrastlı hikaye kartı üretir.
* **Wordle Stili Emoji Izgarası:** Skor kopyalandığında renkli emojilerle sosyal medyada viral paylaşım sağlar (`🟩🟨⬜`).
* **Kıl Payı Kaçırma (Near-Miss) Psikolojisi:** Oyuncuya son 1 harf kala veya 1 saniye kala kaybettiğini hissettirip *"Bir el daha!"* döngüsünü tetikleyen anlık dopamin geri bildirimi sunar.

---

## ❓ 3. Bilgi Yarışması (Quiz & Trivia) Motoru Standartları

### 2.1 Çeldirici (Şık) Tasarım Algoritması
Yapay zekanın yaptığı en büyük hata, doğru cevabı aşırı uzun, yanlış şıkları ise çok kısa veya alakasız yazmaktır.
* **Şık Uzunluğu Kuralı:** 4 şıkkın karakter uzunlukları birbirine yakın olmalıdır (±%20 tolerans).
* **Akademik Çeldirici İlkesi:** Yanlış şıklar rastgele uydurulmaz; konuyu yüzeysel bilen birinin en sık düşeceği kavram yanılgılarından (*misconceptions*) seçilir.

### 2.2 Soru Bankası Taksonomisi ve Adalet Metrikleri
```
┌────────────────────────────────────────────────────────────────────────┐
│ Seviye 1: Isınma (Genel halk bilgisi, %90 doğru yanıt oranı)           │
│ Seviye 2: Orta (Temel kavramlar, %60 doğru yanıt oranı)                │
│ Seviye 3: İleri (Detay bilgi, %35 doğru yanıt oranı)                   │
│ Seviye 4: Uzman / Boss (Tarihler, RFC kuralları, %15 doğru yanıt oranı)│
└────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Geri Sayım & Dinamik Adrenalin Motoru
* Süre işlerken Web Audio osilatörüyle her saniye hafif bir "tık" sesi üretilir.
* **Son 5 Saniye:** Ses perdesi yükselir ve kalp atışı ritmine geçer ($A_4 \rightarrow C_5$); arayüz kenarlarında hafif kırmızı nabız efekti başlar.
* **Süre Bonusu Formülü:**
  $$\text{Kazanılan Puan} = \text{Temel Soru Puanı} \times \left(1 + \frac{\text{Kalan Süre}}{\text{Toplam Süre}}\right)$$

### 2.4 Joker Mekanikleri (Bakiye Entegrasyonu)
* **%50 Jokeri:** Rastgele değil, en az mantıklı olan 2 yanlış şıkkı siler.
* **Seyirci / İpucu Jokeri:** Soruyla ilgili 1 cümlelik düşündürücü ipucu verir.
* **Çift Cevap Jokeri:** İlk yanlışta oyun bitmez, ikinci şansı tanır.

---

## 🔤 3. Kelime Oyunları ve Dil Algoritmaları

1. **Türkçe Karakter Duyarlılığı:** Standart `toUpperCase()` yasaktır. Daima `toLocaleUpperCase('tr-TR')` kullanılır (`i` -> `İ`, `ı` -> `I`).
2. **Sözlük Performansı:** On binlerce kelimelik sözlüklerde dizi araması yerine $O(1)$ Hash Set ve Trie mimarisi.
3. **Bonus Kelime Havuzu:** Çark harfleriyle türetilen ancak ana bulmaca ızgarasında olmayan geçerli sözlük kelimelerine ekstra puan ödülü verilir.

---

## 🃏 4. Kart, Hafıza ve Tahta Oyunları Mimarisi

1. **Kusursuz Karıştırma (Fisher-Yates Shuffle):** Kartlar dizi içinde asla `Math.random() - 0.5` ile karıştırılmaz; adil ve istatistiksel olarak eşit dağılan Fisher-Yates algoritması kullanılır.
2. **Durum Kilidi (State Lock / Debounce):** Oyuncu peş peşe 3 karta tıklayamaz. 2 kart açıldığında etkileşim kilitlenir; eşleşme kontrol edilir (0.6 sn bekleme), eşleşmediyse kartlar geri döner ve kilit açılır.
3. **Kart Çevirme Performansı:** Animasyonlar ana iş parçacığını yormamak için CSS `transform: rotateY()` ve `will-change: transform` ile GPU hızlandırmalı çalıştırılır.

---

## 🕹️ 5. Evrensel 2D Web / Canvas Oyun Motoru

İleride geliştireceğiniz mini arcade veya refleks oyunları için temel kurallar:
* **FPS Bağımsız Oyun Döngüsü (Delta Time):**
  ```javascript
  let lastTime = performance.now();
  function gameLoop(now) {
    const deltaTime = (now - lastTime) / 1000;
    lastTime = now;
    update(deltaTime);
    render();
    requestAnimationFrame(gameLoop);
  }
  ```
* **AABB Çarpışma Tespiti (Collision):** Mermi, engel ve karakter temaslarında hafif ve hızlı kutu/çember sınır kontrolleri.

---

## 🎮 6. Konsol Seviyesinde Mühendislik Standartları

1. **Çoklu Giriş Soyutlaması:** Dokunmatik, Fare ve Klavye (`A-Z`, `Space`, `Enter`, `1-4` tuşları) aynı `dispatch({ type: 'ACTION' })` havuzuna bağlanır.
2. **Durum ve Görünüm Ayrımı (UI-State Decoupling):** UI bileşeni asla oyun değişkenini doğrudan değiştiremez; durumu sadece State Machine günceller.
3. **Sıfır Bayt Prosedürel Web Audio:** Harici MP3 yüklemek yerine Web Audio API osilatörleri ile doğru/yanlış, combo ve seviye atlama sesleri sıfır gecikmeyle üretilir.

---

## 🔍 7. Web & Oyun İçi SEO / ASO Standartları

* **`VideoGame` / `SoftwareApplication` Şeması:** Oyun kategorisi, puanı ve fiyatını Google'a tanıtır.
* **`Quiz` & `Question` Şeması:** Bilgi yarışması soruları Google arama zengin sonuçlarında (Rich Snippets) doğrudan indekslenir.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Quiz",
  "name": "Gölge Siber Güvenlik Quiz Maratonu",
  "hasPart": [
    {
      "@type": "Question",
      "name": "Firewall paket filtrelemesinde state tablosu ne işe yarar?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mevcut bağlantıların durumunu takip ederek meşru geri dönüş paketlerine izin verir."
      }
    }
  ]
}
</script>
```

---

## 🎨 8. Sosyal Virallik, Skor Kartı & Ekonomi

1. **Wordle Stili Emoji Izgarası:** Skor kopyalandığında renkli emojilerle sosyal medyada viral paylaşım sağlar (`🟩🟨⬜`).
2. **HTML5 Canvas Dinamik Skor Kartı:** Oyuncu skoru ve sertifikası sunucusuz şekilde tarayıcıda görselleştirilip PNG indirilebilir.
3. **Sink & Faucet Dengesi:** Altın girişi (musluk) ile ipucu/joker harcaması (lavabo) dengelenir; enflasyon engellenerek ödüllü reklam motivasyonu korunur.
4. **Sıfır Arayüz Zıplaması (Zero CLS):** Addy Osmani kuralları; oyun alanları iskeletle rezerve edilir, yüklenirken ekran kaymaz.
