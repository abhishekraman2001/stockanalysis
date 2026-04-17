import requests
from config import BASE_URL, FMP_API_KEY

def fetch_earnings_history(ticker):
    url = f"{BASE_URL}/historical/earning_calendar/{ticker}"
    params = {"limit": 4, "apikey": FMP_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()
