import webbrowser as w
import os
import time
import edge_tts
import asyncio
import pygame
from sesli_haber import technopat,trign
import requests
import json
import speech_recognition as sr
import pyautogui
import pyperclip
import wikipedia
from kur import doviz_cek
import subprocess
import re
import requests
from bs4 import BeautifulSoup
import random
import psutil
wikipedia.set_lang("tr")

VOICE = "tr-TR-AhmetNeural"

pygame.mixer.init()

async def _konus(metin):
    file_path = "morty.mp3"
    communicate = edge_tts.Communicate(metin, VOICE, rate="-6%", pitch="-8Hz")
    await communicate.save(file_path)

    
    if not pygame.mixer.get_init():
        pygame.mixer.init()
        
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.music.unload() 
    
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Dosya silme hatası: {e}")

def sohbet(katagori):
    with open("cevaplar.json", "r", encoding="utf-8") as s:
        veriler = json.load(s)
        if katagori in veriler:
            secilen = random.choice(veriler[katagori])
            konus(secilen)
        else:
            konus("bunun hakında bir bilgi vermediniz efendim")
 
                     
def sistem_bilgisi():
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent 
    cevap = f"Sistem analizi tamamlandı efendim. İşlemci yükü yüzde {cpu}, bellek kullanımı ise yüzde {ram} kapasitede."
    konus(cevap)            



def youtube_arama(komut):
    url = f"https://www.youtube.com/results?search_query={komut}"
    w.open(url)
    konus(f"{komut} açıldı")
def web_browser(webilgi):
    url = f"https://www.google.com/search?q={webilgi}"
    w.open(url)
    konus(f"{webilgi} açıldı")
def yotube_muzik(muzik):
    url = f"https://music.youtube.com/search?q={muzik}"
    w.open(url)
    konus(f"{muzik}açıldı")
def spotify_muzik(muzik):
    url = f"https://open.spotify.com/search/{muzik}"
    w.open(url)
    konus(f"{muzik}açıldı")
def konus(metin):
    asyncio.run(_konus(metin))
def wikibig(konu):
    try:
        ozet = wikipedia.summary(konu, sentences=2)
        konus(f"{konu} hakkında bulduklarım şöyle: {ozet}")
    except wikipedia.exceptions.DisambiguationError:
        konus("Çok genel bir şey söyledin, biraz daha detay ver.")

def havadurumu(city):
    try:

        response = requests.get(f"https://wttr.in/{city}?format=j1")
        response.raise_for_status() 
        
        data = response.json()
        weather = data['current_condition'][0]
        
    
        return {
            "sicaklik": weather['temp_C'],
            "hissedilen": weather['FeelsLikeC'],
            "durum": weather['weatherDesc'][0]['value']
        }
    except Exception as e:
        return {"hata": f"Veri çekilemedi: {str(e)}"}
def py_modul(modul):
    subprocess.run(["pip", "install", modul], check=True)
def agdaki_cihazlar():
    try:

        cikti = subprocess.check_output(["arp", "-a"]).decode("cp857")
        
        print("\n" + "="*50)
        print("MORTY AĞ TARAMA VE IP ANALİZİ")
        print("="*50)
        
       
        ip_listesi = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', cikti)
        benzersiz_ipler = list(set(ip_listesi))
        
        if not benzersiz_ipler:
            konus("Ağda hiç cihaz bulamadım efendim, bir şeyler ters gitti.")
            return

        konus(f"Ağda {len(benzersiz_ipler)} nokta tespit ettim. Analiz ediyorum.")

        for ip in benzersiz_ipler:
          
            if ip.startswith("192.168") or ip.startswith("10.0") or ip.startswith("127.0") or ip.startswith("255."):
                print(f"[YEREL] {ip} - Cihaz senin ağında.")
                continue
                
            try:
                res = requests.get(f"http://ip-api.com/json/{ip}", timeout=1).json()
                if res.get('status') == 'success':
                    info = f"[DIŞ IP] {ip} -> {res['city']}/{res['country']} ({res['isp']})"
                    print(info)
                else:
                    print(f"[BİLİNMEYEN] {ip}")
            except:
                print(f"[TARAMA DIŞI] {ip}")

        print("="*50)
        konus("Tarama bitti, detaylar terminalde.")

    except Exception as e:
        print(f"Sistem Hatası: {e}")
        konus("Ağ verilerini alırken sistem hata verdi.")

def dinamik_c_taramasi(hedef_klasor_adi):
    ana_dizin = "C:\\"
    atlanacak_klasorler = ["Windows", "Program Files", "Program Files (x86)", "$Recycle.Bin", "System Volume Information"]
    
    bulunan_yol = None
    
    try:
        ana_klasor_listesi = [klasor for klasor in os.listdir(ana_dizin) if os.path.isdir(os.path.join(ana_dizin, klasor))]
        
        for klasor in ana_klasor_listesi:
            if klasor in atlanacak_klasorler:
                continue
                
            su_anki_yol = os.path.join(ana_dizin, klasor)
            
            if klasor.lower() == hedef_klasor_adi.lower():
                bulunan_yol = su_anki_yol
                break
            
            try:
                for kok_dizin, alt_klasorler, dosyalar in os.walk(su_anki_yol):
                    if hedef_klasor_adi.lower() in [d.lower() for d in alt_klasorler]:
                        bulunan_yol = os.path.join(kok_dizin, hedef_klasor_adi)
                        break
                    
                    derinlik = kok_dizin.count(os.sep) - su_anki_yol.count(os.sep)
                    if derinlik >= 2:
                        del alt_klasorler[:] 
                
                if bulunan_yol: 
                    break
            except PermissionError:
                continue 
                
    except Exception as hata:
        print(f"Tarama sırasında bir patlak verdi: {hata}")

    if bulunan_yol:
        subprocess.Popen(["explorer", bulunan_yol])
        konus(f"{hedef_klasor_adi} klasörünü açtım efendim.")
    else:
        konus(f"C sürücüsünde {hedef_klasor_adi} isminde bir klasör bulamadım.")
def sesli_komut_dinle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ortam sesi ayarlanıyor...")
        r.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                # print("Dinliyorum...")
                audio = r.listen(source, timeout=None, phrase_time_limit=10)
                komut = r.recognize_google(audio, language="tr-TR").lower()
                # print(f"söylenen:{komut}")
                if"morty" in komut:
                    if "browser" in komut:
                        arama = komut.replace("morty", "").replace("browser", "").strip()
                        web_browser(arama)
                    elif "youtube" in komut:
                        baglantı = komut.replace("morty", "").replace("youtube", "").strip()
                        youtube_arama(baglantı)
                    elif "yt müzik" in komut:
                        baglantı = komut.replace("morty", "").replace("yt", "").replace("müzik","").strip()
                        yotube_muzik(baglantı)
                    elif "spotify" in komut:
                        baglantı = komut.replace("morty", "").replace("spotify", "").strip()
                        spotify_muzik(baglantı)
                    elif "haberler" in komut:
                        haberler = technopat()
                        oyun = trign()
                        konus(f"technpoat haberleri : {haberler} trigin haberleri : {oyun}")
                    elif "wikipedia" in komut:
                        ara = komut.replace("wikipedia", "").replace("morty", "").strip()
                        wikibig(ara)
                    elif "button" in komut:
                        pyautogui.press("k")
                    elif "esc" in komut:
                        pyautogui.press("esc")
                    elif"boşluk" in komut:
                        pyautogui.press("space")
                    elif "dolar" in komut:
                        döviz = doviz_cek()
                        dolar_degeri = döviz["dolar"]
                        mesaj = f"dolar şu anda{dolar_degeri}tl'dir"
                        konus(mesaj)
                    elif "euro" in komut:
                        döviz = doviz_cek()
                        euro_degeri = döviz["euro"]
                        mesaj = f"euro şu anda{euro_degeri}tl'dir"
                        konus(mesaj)
                    elif "hava durumu" in komut:
                        ara = komut.replace("hava durumu","").replace("morty","").strip()
                        hava = havadurumu(ara)
                        sicaklik = hava["sicaklik"]
                        durum = hava["durum"]
                        mesaj = f"{ara} şehrinde hava şu an {sicaklik} derece ve {durum}"
                        konus(mesaj) 
                    elif "sesi arttır" in komut:
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                    elif "sesi kıs" in komut:
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        mod = komut.replace("morty","").replace("piton","").strip()
                        py_modul(mod)
                        konus("modül indirldi")
                    elif "yazdır"in komut:
                        üret = komut.replace("morty","").replace("yazdır","").strip()
                        pyperclip.copy(üret)
                        pyautogui.hotkey('ctrl', 'v')
                    elif "enter"in komut:
                        pyautogui.press("enter")
                    elif"harf"in komut:
                        üret = komut.replace("morty","").replace("harf","").strip()
                        pyautogui.press(f"{üret}")
                    
                        
                    elif "internet" in komut:
                        agdaki_cihazlar()
                    elif "klasör" in komut:
                        hedef = komut.replace("morty", "").replace("klasör", "").strip()
                        
                        if hedef:
                            konus(f"{hedef} aranıyor...")
                            dinamik_c_taramasi(hedef)
                    elif"sistem bilgisi" in komut:
                        sistem_bilgisi()
                    elif"teşekkürler"in komut:
                        sohbet("teşekkürler")
                    elif"selam" in komut:
                        sohbet("selam")
                    elif"nasılsın" in komut:
                        sohbet("nasılsın")
                    elif "neler yapabilirsin" in komut:
                        sohbet("yetenekler")
            except sr.UnknownValueError:
                continue
            except Exception as e:
                print(f"Hata oluştu: {e}")
                continue

if __name__ == "__main__":
    sesli_komut_dinle()
