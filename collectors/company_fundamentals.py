import requests
from config import BASE_URL, FMP_API_KEY

def fetch_fundamentals(ticker):
    url = f"{BASE_URL}/income-statement/{ticker}"
    params = {"limit": 4, "apikey": FMP_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()
