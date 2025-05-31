import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.title("전세계 시가총액 Top 10 기업의 지난 3년간 주가 변화")

# Top 10 기업 티커 (예시)
tickers = [
    "AAPL",      # Apple
    "MSFT",      # Microsoft
    "AMZN",      # Amazon
    "GOOGL",     # Alphabet (Google)
    "META",      # Meta Platforms (Facebook)
    "TSLA",      # Tesla
    "BRK-B",     # Berkshire Hathaway
    "NVDA",      # Nvidia
    "TSM",       # Taiwan Semiconductor Manufacturing
    "2222.SR"    # Saudi Aramco (티커가 다를 수 있습니다)
]

# 지난 3년 데이터를 위해 시작일과 종료일 계산
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)  # 약 3년

st.write(f"데이터 조회 기간: {start_date.date()} ~ {end_date.date()}")

@st.cache_data(show_spinner=False)
def load_data(ticker, start, end):
    # yfinance를 사용하여 지정 기간의 데이터를 다운로드
    df = yf.download(ticker, start=start, end=end)
    if not df.empty:
        df.reset_index(inplace=True)
        df = df[['Date', 'Close']].copy()
        df['Ticker'] = ticker
    return df

# 모든 티커의 데이터를 결합
all_data = pd.DataFrame()
for tic in tickers:
    df_tic = load_data(tic, start_date, end_date)
    if df_tic is not None and not df_tic.empty:
        all_data = pd.concat([all_data, df_tic], ignore_index=True)

if all_data.empty:
    st.error("데이터를 불러올 수 없습니다. 티커 혹은 네트워크 상태를 확인하세요.")
else:
    # Plotly로 인터랙티브 라인 차트 생성
    fig = px.line(
        all_data,
        x="Date",
        y="Close",
        color="Ticker",
        title="전세계 Top 10 기업 주가 변화 (지난 3년)",
        labels={"Close": "종가", "Date": "날짜"}
    )
    st.plotly_chart(fig, use_container_width=True)
