# 🎙️ Asistan Morty - Sesli Otomasyon & Sistem Yönetimi (v1.0.1)

Asistan Morty; Python tabanlı, Windows sistemleriyle derin entegrasyon sağlayan, günlük işleri, sistem yönetimini ve teknik süreçleri sesli komutlarla yönetebilen **modüler bir otomasyon hub'ıdır.**

## 🚀 Öne Çıkan Özellikler

- **Gelişmiş Ses Deneyimi:** Google Speech Recognition ile hassas tanıma ve `edge-tts` (Azure altyapısı) ile doğal Türkçe seslendirme (`AhmetNeural`).
    
- **Sistem Otomasyonu:** Dinamik klasör tarama (C sürücüsünde akıllı arama), işletim sistemi seviyesinde kapatma/uygulama kontrolleri.
    
- **Ağ Analizi (Network):** `ARP` protokolü üzerinden yerel ağdaki (LAN) cihazları listeleme ve dış IP'lerin coğrafi konum analizi.
    
- **Teknik Denetim:** "Piton" komutuyla dinamik kütüphane (`pip`) yükleme ve `psutil` ile CPU/RAM kaynaklarını anlık izleme.
    
- **Gelişmiş Multimedya:** YouTube, YouTube Müzik ve Spotify üzerinden içerik yönetimi; ses seviyesi ve klavye kısayol simülasyonları (`pyautogui`).
    
- **Haber & Bilgi Entegrasyonu:** Technopat ve IGN üzerinden scraping ile güncel haber başlıkları, Wikipedia özetleri ve `wttr.in` üzerinden canlı hava durumu.
    
- **Akıllı Diyalog:** `cevaplar.json` mimarisi ile genişletilebilir sohbet yeteneği ve durum farkındalığı.
    

---

## 🛠️ Kurulum

Sisteminizde **Python 3.8+** yüklü olduğundan emin olun.

### 1. Projeyi İndirin

Bash

```
git clone https://github.com/kullaniciadi/asistan-morty.git
cd asistan-morty
```

### 2. Bağımlılıkları Yükleyin

Proje, sistem seviyesi kütüphaneler kullandığı için bağımlılıkların eksiksiz kurulması önemlidir:

Bash

```
pip install -r requirements.txt
```

---

## 🖥️ Komut ve Yetenek Örnekleri

|**Kategori**|**Komut Örneği**|**Teknik İşlev**|
|---|---|---|
|**Sistem Analizi**|"Morty sistem bilgisi"|Anlık CPU ve RAM yüzdesini raporlar.|
|**Geliştirici**|"Morty piton [modül_adı]"|`subprocess` ile arka planda pip kurulumu yapar.|
|**Dosya Sistemi**|"Morty klasör [isim]"|`os.walk` ile dinamik dizin taraması ve explorer açılışı.|
|**Ağ Güvenliği**|"Morty internet"|ARP tablosunu çeker ve IP-API üzerinden analiz yapar.|
|**Bilgi Servisi**|"Morty hava durumu [şehir]"|REST API üzerinden anlık durum ve sıcaklık çeker.|
|**Klavye Kontrol**|"Morty yazdır [metin]"|`pyperclip` ve `hotkey` simülasyonu ile metin yapıştırır.|

---

## 📂 Proje Yapısı

- `Asistan_Morty.py`: Ana asenkron döngü ve komut yönetim merkezi.
    
- `cevaplar.json`: JSON tabanlı diyalog seti ve asistan hafızası.
    
- `sesli_haber.py`: BeautifulSoup tabanlı haber scraping modülü.
    
- `kur.py`: Finansal veri çekme (Döviz/Altın) modülü.
    
- `requirements.txt`: Projenin çalışması için gereken tüm kütüphaneler.
