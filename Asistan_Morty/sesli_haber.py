import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "tr-TR,tr;q=0.9",
    "Referer": "https://www.google.com/"
}

# ---------------- TECHNOPAT ----------------
def technopat():
    url = "https://www.technopat.net/"
    sonuc = []

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return sonuc  

        soup = BeautifulSoup(r.text, "html.parser")

        haberler = soup.select("h3.jeg_post_title > a")[:5]

        for h in haberler:
            baslik = h.get_text(strip=True)
            link = h.get("href")

            if baslik:
                sonuc.append({
                    "baslik":baslik
                })

        return sonuc

    except Exception as e:
        return sonuc


# ---------------- TR IGN ----------------
def trign():
    url = "https://tr.ign.com/"
    sonuc = []

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return sonuc

        soup = BeautifulSoup(r.text, "html.parser")

        haberler = soup.select("span.caption")[:5]

        for h in haberler:
            baslik = h.get_text(strip=True)
            if baslik:
                sonuc.append({
                    "baslik": baslik
                })

        return sonuc

    except Exception as e:
        return sonuc
