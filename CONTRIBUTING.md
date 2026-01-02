# Katkıda Bulunma Rehberi

Asistan Morty projesine katkı sağlamak istediğiniz için teşekkür ederiz. Bu belge, geliştirme sürecimizin standartlarını ve teknik gereksinimlerini belirlemek amacıyla hazırlanmıştır.

## 1. Teknik Ön Koşullar

Projeye katkı sağlamadan önce aşağıdaki kütüphanelerin sisteminizde kurulu olduğundan ve düzgün çalıştığından emin olunuz:
* **Ses İşleme:** `edge_tts`, `speech_recognition`, `pygame`
* **Veri Kazıma & API:** `requests`, `beautifulsoup4`
* **Otomasyon:** `pyautogui`

## 2. Proje Yapısı ve Modülerlik

Proje üç ana bileşenden oluşmaktadır. Yapacağınız geliştirmeleri ilgili dosya içinde gerçekleştiriniz:
* `Asistan_Morty.py`: Ana kontrol döngüsü ve sesli komut işleme mantığı.
* `sesli_haber.py`: Web scraping (Technopat, IGN) işlevleri.
* `kur.py`: Döviz kuru API entegrasyonu.

## 3. Geliştirme Standartları

* **Yeni Komut Ekleme:** `Asistan_Morty.py` içerisindeki `sesli_komut_dinle` fonksiyonuna yeni bir `elif` bloğu eklemeden önce, eğer komut karmaşık bir mantık içeriyorsa, bu mantığı ayrı bir fonksiyonda tanımlayınız.
* **Hata Yönetimi:** Ağ istekleri (`requests`) ve dosya işlemleri (`os.remove`) sırasında oluşabilecek istisnaları (Exception) mutlaka `try-except` blokları ile kontrol altına alınız.
* **Kod Stili:** Python için PEP 8 standartlarına uyulması beklenmektedir.

## 4. Pull Request (PR) Süreci

1. Depoyu fork ediniz ve güncel `main` branch üzerinden yeni bir özellik dalı (`feature/ozellik-adi`) oluşturunuz.
2. Değişikliklerinizi commit ederken açıklayıcı mesajlar kullanınız (Örn: `feat: Spotify çalma listesi desteği eklendi`).
3. PR açıklamasında yaptığınız değişikliğin asistanın hangi komutuyla tetiklendiğini veya hangi hatayı giderdiğini belirtiniz.
4. Mevcut sesli komut yapısını bozmadığınızdan emin olmak için kodunuzu manuel olarak test ediniz.

## 5. Davranış Kuralları

Tüm katılımcıların [Code of Conduct](CODE_OF_CONDUCT.md) belgesindeki etik kurallara ve profesyonel iletişim standartlarına uyması zorunludur.

---
**İletişim:** Teknik sorularınız veya iş birliği talepleriniz için [anonimtasarim98@gmail.com] kanalını kullanabilirsiniz.
