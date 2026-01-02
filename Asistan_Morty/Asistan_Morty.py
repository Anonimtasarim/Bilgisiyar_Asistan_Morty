import os
import webbrowser as w
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

wikipedia.set_lang("tr")

VOICE = "tr-TR-AhmetNeural"

pygame.mixer.init()

async def _konus(metin):
    file_path = "morty.mp3"
    communicate = edge_tts.Communicate(metin, VOICE)
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


def sesli_komut_dinle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ortam sesi ayarlanıyor...")
        r.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                audio = r.listen(source, timeout=None, phrase_time_limit=10)
                komut = r.recognize_google(audio, language="tr-TR").lower()
                # print(f"Söylenen: {komut}")
                if"morty" in komut:    
                    if "browser" in komut:
                        konus("browsera baglandı")
                        arama = komut.replace("morty", "").replace("browser", "").strip()
                        web_browser(arama)
                    elif "youtube" in komut:
                        konus("yotube'ye baglandı")
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
                    elif "buton" in komut:
                        pyautogui.press("k")
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
                    elif "kapat" in komut:
                        break
                        

            except sr.UnknownValueError:
                continue
            except Exception as e:
                print(f"Hata oluştu: {e}")
                continue

if __name__ == "__main__":
    sesli_komut_dinle()