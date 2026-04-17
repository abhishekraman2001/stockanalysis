def summarize_company(ticker, fundamentals, earnings, score):
    summary = f"""
Company: {ticker}

Revenue Trend:
"""
    if len(fundamentals) >= 2:
        summary += f"- Last Quarter Revenue: {fundamentals[0]['revenue']:,}\n"
        summary += f"- Previous Quarter Revenue: {fundamentals[1]['revenue']:,}\n"

    summary += "\nEarnings Performance:\n"
    for e in earnings[:3]:
        summary += f"- {e['date']}: Actual {e['epsActual']} vs Est {e['epsEstimated']}\n"

    summary += f"\nOverall Status: {score}\n"

    return summary
