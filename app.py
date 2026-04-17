import streamlit as st

from collectors.earnings_calendar import fetch_earnings_calendar
from collectors.company_fundamentals import fetch_fundamentals
from collectors.earnings_history import fetch_earnings_history
from analysis.scorer import score_company
from analysis.summarizer import summarize_company
from utils.helpers import filter_next_30_days

# --------------------------------------------------
# Streamlit page config
# --------------------------------------------------
st.set_page_config(page_title="Earnings Intelligence Bot", layout="wide")
st.title("📊 Earnings Intelligence Bot")

# --------------------------------------------------
# Load earnings calendar
# --------------------------------------------------
if st.button("📅 Load Earnings (Next 30 Days)"):
    with st.spinner("Fetching earnings calendar..."):
        calendar = fetch_earnings_calendar()

    if not calendar:
        st.warning("No earnings data returned from API.")
    else:
        calendar_30 = filter_next_30_days(calendar)

        if not calendar_30:
            st.warning("No earnings found in the next 30 days.")
        else:
            tickers = sorted(
                {item.get("symbol") for item in calendar_30 if item.get("symbol")}
            )

            st.session_state["calendar_30"] = calendar_30
            st.session_state["tickers"] = tickers

            st.success(f"Loaded {len(calendar_30)} earnings events for {len(tickers)} companies")

# --------------------------------------------------
# Company selection
# --------------------------------------------------
if "tickers" in st.session_state and st.session_state["tickers"]:
    ticker = st.selectbox(
        "Select Company",
        st.session_state["tickers"],
        index=0
    )

    # --------------------------------------------------
    # Analyze company
    # --------------------------------------------------
    if st.button("Analyze Company"):
        with st.spinner(f"Analyzing {ticker}..."):
            fundamentals = fetch_fundamentals(ticker)
            earnings = fetch_earnings_history(ticker)

            if not fundamentals:
                st.error("No fundamentals data available.")
            elif not earnings:
                st.error("No earnings history available.")
            else:
                score = score_company(fundamentals, earnings)
                summary = summarize_company(ticker, fundamentals, earnings, score)

                st.subheader("📌 Earnings Summary")
                st.text(summary)
