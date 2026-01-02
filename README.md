
# 🎙️ Asistan Morty - Sesli Asistan Projesi

Asistan Morty; Python tabanlı, sesli komutlarla web araması yapabilen, güncel haberleri ve döviz kurlarını takip eden, medya kontrolü (ses artırma/azaltma, duraklatma) sağlayabilen kişisel bir sesli asistandır.

## 🚀 Özellikler

- **Sesli Komut Tanıma:** Google Speech Recognition API ile sesinizi metne dönüştürür.
    
- **Doğal Ses Sentezi:** `edge-tts` kullanarak Microsoft Azure sesleriyle akıcı geri bildirim verir.
    
- **Haber Takibi:** Technopat ve IGN Türkiye üzerinden güncel başlıkları anlık olarak çeker (Web Scraping).
    
- **Hava Durumu:** Belirttiğiniz şehrin hava durumunu ve sıcaklığını sesli olarak bildirir.
    
- **Finansal Veriler:** Güncel Dolar ve Euro kurlarını anlık olarak aktarır.
    
- **Medya & Tarayıcı Kontrolü:** YouTube, Spotify ve Google aramalarını başlatır; sistem ses seviyesini kontrol eder.
    
- **Wikipedia Entegrasyonu:** Aradığınız terimlerin özet bilgilerini sesli olarak okur.
    

---

## 🛠️ Kurulum

Projenin çalışması için sisteminizde Python 3.7+ yüklü olmalıdır.

### 1. Depoyu Klonlayın

Bash

```
git clone https://github.com/kullaniciadi/asistan-morty.git
cd asistan-morty
```

### 2. Gerekli Kütüphaneleri Yükleyin

Uygulamanın bağımlılıklarını aşağıdaki komutla yükleyebilirsiniz:

Bash

```
pip install requests beautifulsoup4 edge-tts pygame SpeechRecognition pyautogui pyperclip wikipedia
```

> **Not:** Ses tanıma özelliğinin kararlı çalışması için sisteminizde `PyAudio` yüklü olmalıdır. Eğer hata alırsanız işletim sisteminize uygun PyAudio kurulumunu yapınız.

---

## 🖥️ Kullanım

Asistanı başlatmak için terminale şu komutu yazın:

Bash

```
python Asistan_Morty.py
```

Uygulama başladığında ortam sesini ayarlayacak ve sizi dinlemeye başlayacaktır. Tüm komutların başında **"Morty"** anahtar kelimesini kullanmanız gerekmektedir.

### Örnek Komutlar

| **İşlem**              | **Komut Örneği**                         |
| ---------------------- | ---------------------------------------- |
| **Google Araması**     | "Morty browser Python dersleri"          |
| **YouTube Araması**    | "Morty youtube Barış Özcan"              |
| **Haberleri Dinleme**  | "Morty haberler"                         |
| **Döviz Kuru**         | "Morty dolar kaç tl?" veya "Morty euro"  |
| **Hava Durumu**        | "Morty hava durumu İstanbul"             |
| **Bilgi Alma**         | "Morty wikipedia Yapay Zeka"             |
| **Medya Kontrolü**     | "Morty sesi arttır" / "Morty sesi kıs"   |
| Yt Müzik               | "Morty yt müzik ahmet kaya"              |
| Spotifiy Müzik         | "Morty spotifiy ahmet kaya"              |
| Uygulamayı kapatmak    | "morty kapat"                            |

---

## 📂 Dosya Yapısı

- `Asistan_Morty.py`: Ana uygulama döngüsü ve sesli komut işleme mantığı.
    
- `sesli_haber.py`: Technopat ve IGN üzerinden veri çeken scraping fonksiyonları.
    
- `kur.py`: ExchangeRate API üzerinden güncel döviz verilerini çeken modül.
    

---
## Gereksinimler
| **Kütüphane**         | **Kullanım Amacı**                                                                                                    |     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- | --- |
| **SpeechRecognition** | Mikrofon üzerinden alınan sesli komutları metne (String) çevirmek için kullanılır.                                    |     |
| **edge-tts**          | Microsoft Azure altyapısını kullanarak metinleri doğal ve akıcı bir sese dönüştürür.                                  |     |
| **BeautifulSoup4**    | Technopat ve IGN gibi web sitelerinin HTML yapısını analiz edip haber içeriklerini çekmek (scraping) için kullanılır. |     |
| **pyautogui**         | Sistem düzeyinde klavye (tuş basımı) ve ses seviyesi kontrollerini simüle etmek için kullanılır.                      |     |
| **pygame**            | Kaydedilen ses dosyalarını (MP3) belleğe yükleyip oynatmak ve ses kanallarını yönetmek için kullanılır.               |     |
| **requests**          | API çağrıları yapmak ve web sitelerinin kaynak kodlarına erişmek için kullanılır.                                     |     |
| **wikipedia**         | Wikipedia üzerinden hızlı ve özet bilgi çekmek için kullanılır.                                                       |     |

---

## ⚠️ Önemli Notlar

- **İnternet Bağlantısı:** Ses tanıma (Google) ve ses sentezi (Edge-TTS) işlemleri için aktif internet bağlantısı gereklidir.
    
- **Mikrofon Erişimi:** Uygulamanın mikrofonunuza erişim izni olduğundan emin olun. bu kadarı yeterlimi sence
