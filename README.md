# 🎙️ Asistan Morty - Sesli Asistan Projesi (v1.0.1)

Asistan Morty; Python tabanlı, Windows sistemleriyle derin entegrasyon sağlayan, günlük işleri ve teknik süreçleri sesli komutlarla yönetebilen gelişmiş bir dijital asistandır.

## 🚀 Öne Çıkan Özellikler

- **Gelişmiş Ses Deneyimi:** Google Speech Recognition ile hassas tanıma ve `edge-tts` (Azure altyapısı) ile doğal Türkçe seslendirme.
    
- **Teknik Denetim:** "Piton" komutuyla sesli kütüphane (pip) yükleme ve sistem kaynaklarını (CPU/RAM) anlık izleme.
    
- **Multimedya Hakimiyeti:** YouTube, YouTube Müzik ve **Spotify** üzerinden içerik başlatma; donanımsal ses kontrolü.
    
- **Haber & Bilgi:** Technopat ve IGN üzerinden güncel haber başlıkları, Wikipedia özetleri ve canlı döviz kurları.
    
- **Sistem Otomasyonu:** Dinamik klasör tarama ve yerel ağdaki (LAN) cihazları listeleme.
    
- **Karakterli Etkileşim:** `cevaplar.json` mimarisi ile doğal selamlaşma ve akıllı sohbet yeteneği.
    

---

## 🛠️ Kurulum

Sisteminizde **Python 3.7+** yüklü olduğundan emin olun.

### 1. Projeyi İndirin

Bash

```
git clone https://github.com/kullaniciadi/asistan-morty.git
cd asistan-morty
```

### 2. Bağımlılıkları Yükleyin

Bash

```
pip install -r requirements.txt
```

> **Not:** `PyAudio` kurulumunda hata alırsanız Windows için `pip install pipwin` ve `pipwin install pyaudio` komutlarını kullanın.

---

## 🖥️ Kullanım ve Komut Örnekleri

Asistanı başlatmak için: `python Asistan_Morty.py`

|**Kategori**|**Komut Örneği**|**İşlev**|
|---|---|---|
|**Sohbet**|"Morty selam" / "Morty nasılsın?"|Karşılıklı etkileşim kurar.|
|**Bilgi**|"Morty wikipedia Elon Musk"|Wikipedia özetini okur.|
|**Müzik**|"Morty spotify Barış Manço"|Spotify araması başlatır.|
|**Sistem**|"Morty sistem bilgisi"|CPU ve RAM kullanımını söyler.|
|**Geliştirici**|"Morty piton pandas"|Pandas kütüphanesini yükler.|
|**Finans**|"Morty dolar kaç tl?"|Güncel kuru bildirir.|
|**Navigasyon**|"Morty klasör indirilenler"|İlgili klasörü tarar.|

---

## 📂 Proje Yapısı

- `Asistan_Morty.py`: Ana motor ve komut yönetim merkezi.
    
- `cevaplar.json`: Diyalog veri seti ve asistan hafızası.
    
- `sesli_haber.py`: Web scraping (haber çekme) modülü.
    
- `kur.py`: API tabanlı finansal veri çekme modülü.
    
- `requirements.txt`: Gerekli tüm kütüphanelerin listesi.
    

---

## ⚠️ Önemli Hatırlatmalar

- **İnternet:** Ses tanıma ve TTS motoru için stabil bir internet bağlantısı şarttır.
    
- **İzinler:** Dosya tarama ve pip yükleme gibi özellikler için terminalin **Yönetici** olarak çalıştırılması önerilir.
    
- **Gizlilik:** `Asistan_Morty.py` içindeki kişisel dosya yollarını kendi bilgisayarınıza göre düzenlediğinizden emin olun.
    

---

### **Neler Değişti?**

1. **Sürüm Numarası:** v1.0.1 olarak güncellendi.
    
2. **Tablo:** Spotify ve "Piton" (modül yükleme) komutları eklendi.
    
3. **Özellikler:** Sistem bilgisi ve klasör tarama gibi teknik detaylar vurgulandı.
