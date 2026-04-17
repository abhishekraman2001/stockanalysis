import requests
import json
from config import BASE_URL, FMP_API_KEY

def fetch_earnings_calendar():
    url = f"{BASE_URL}/earning_calendar"
    params = {
        "apikey": FMP_API_KEY
    }

    r = requests.get(url, params=params, timeout=20)

    if r.status_code == 403:
        raise RuntimeError(
            "403 Forbidden from FMP. "
            "Your API plan likely does not allow earnings calendar date filters."
        )

    r.raise_for_status()
    data = r.json()

    # Save full calendar
    with open("data/earnings_calendar.json", "w") as f:
        json.dump(data, f, indent=2)

    return data
