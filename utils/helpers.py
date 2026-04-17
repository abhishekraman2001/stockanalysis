from datetime import datetime, timedelta

def filter_next_30_days(calendar):
    today = datetime.today().date()
    end = today + timedelta(days=30)

    results = []
    for item in calendar:
        date_str = item.get("date")
        if not date_str:
            continue
        try:
            d = datetime.fromisoformat(date_str).date()
        except ValueError:
            continue
        if today <= d <= end:
            results.append(item)

    return results
