import urllib.request
import json

def doviz_cek():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            usd = data["rates"].get("TRY")
            eur = usd / data["rates"].get("EUR")
            
            return {
                "dolar": round(usd, 2),
                "euro": round(eur, 2)
            }
    except Exception as e:
        return {"hata": "Kur verisi alınamadı"}