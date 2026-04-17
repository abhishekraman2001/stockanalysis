def score_company(fundamentals, earnings):
    score = 0

    # Revenue growth
    if len(fundamentals) >= 2:
        rev_now = fundamentals[0]["revenue"]
        rev_prev = fundamentals[1]["revenue"]
        if rev_now > rev_prev:
            score += 1

    # Earnings beats
    for e in earnings[:3]:
        if e.get("epsActual") and e.get("epsEstimated"):
            if e["epsActual"] > e["epsEstimated"]:
                score += 1

    if score >= 3:
        return "🟢 Bullish"
    elif score == 2:
        return "🟡 Neutral"
    else:
        return "🔴 Risky"
