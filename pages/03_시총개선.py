import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.title("전세계 시가총액 Top 10 기업의 지난 3년간 주가 변화")

# Top 10 기업 티커 목록
tickers = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META",
    "TSLA", "BRK-B", "NVDA", "TSM", "2222.SR"
]

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)  # 3년 전

st.write(f"데이터 조회 기간: {start_date.date()} ~ {end_date.date()}")

@st.cache_data(show_spinner=True)
def load_data(ticker, start, end):
    """yfinance에서 데이터를 가져오고, 오류 처리 추가"""
    df = yf.download(ticker, start=start, end=end)
    if df.empty:
        st.warning(f"{ticker} 데이터를 가져올 수 없습니다.")
        return None  # 빈 데이터프레임 대신 None 반환

    df.reset_index(inplace=True)
    df = df[['Date', 'Close']].copy()
    df['Ticker'] = ticker
    df["Date"] = pd.to_datetime(df["Date"])  # 날짜 형식 변환
    return df

# 모든 티커 데이터를 가져와 결합
all_data = pd.DataFrame()
for tic in tickers:
    df_tic = load_data(tic, start_date, end_date)
    if df_tic is not None:  # 데이터가 있을 때만 추가
        all_data = pd.concat([all_data, df_tic], ignore_index=True)

# 데이터 확인 및 예외 처리
if all_data.empty:
    st.error("모든 기업 데이터를 불러올 수 없습니다. 네트워크 상태 또는 티커 목록을 확인하세요.")
    st.stop()  # 실행 중단

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
