import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.title("전세계 시가총액 Top 10 기업의 지난 3년간 주가 변화")

# Top 10 기업 티커 목록 (필요시 업데이트)
tickers = [
    "AAPL",    # Apple
    "MSFT",    # Microsoft
    "AMZN",    # Amazon
    "GOOGL",   # Alphabet (Google)
    "META",    # Meta Platforms (Facebook)
    "TSLA",    # Tesla
    "BRK-B",   # Berkshire Hathaway
    "NVDA",    # Nvidia
    "TSM",     # TSMC
    "2222.SR"  # Saudi Aramco (티커가 다르면 수정)
]

# 날짜 범위: 오늘부터 과거 3년
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)
st.write(f"데이터 조회 기간: {start_date.date()} ~ {end_date.date()}")

@st.cache_data(show_spinner=True)
def load_data(ticker, start, end):
    try:
        df = yf.download(ticker, start=start, end=end)
        if df.empty:
            st.warning(f"{ticker} 데이터를 가져올 수 없습니다.")
            return None
        df.reset_index(inplace=True)
        # 'Date'와 'Close' 컬럼이 반드시 있어야 함
        df = df[['Date', 'Close']].copy()
        df['Ticker'] = ticker
        # Date 컬럼을 datetime 형식으로 변환
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        # Close 값에 NaN이 있는 행 제거
        df.dropna(subset=["Close", "Date"], inplace=True)
        return df
    except Exception as e:
        st.error(f"{ticker} 데이터를 가져오는 중 오류 발생: {e}")
        return None

# 모든 티커 데이터를 하나의 DataFrame으로 결합
all_data = pd.DataFrame()
for tic in tickers:
    df_tic = load_data(tic, start_date, end_date)
    if df_tic is not None:
        all_data = pd.concat([all_data, df_tic], ignore_index=True)

# 데이터가 전혀 수집되지 않았다면 앱 실행 중단
if all_data.empty:
    st.error("모든 기업의 데이터를 불러올 수 없습니다. 네트워크 상태 또는 티커 목록을 확인하세요!")
    st.stop()

# 데이터프레임 확인: 컬럼, 데이터 타입, 미리보기 
st.write("데이터프레임 컬럼:", all_data.columns.tolist())
st.write("데이터프레임 정보:")
st.write(all_data.dtypes)
st.write("데이터 미리보기:")
st.write(all_data.head())

# Plotly로 인터랙티브 라인 차트 생성 (예외 처리 추가)
try:
    fig = px.line(
        all_data,
        x="Date",
        y="Close",
        color="Ticker",
        title="전세계 Top 10 기업 주가 변화 (지난 3년)",
        labels={"Close": "종가", "Date": "날짜"}
    )
    st.plotly_chart(fig, use_container_width=True)
except Exception as plot_err:
    st.error("Plotly 차트 생성 중 오류 발생: " + str(plot_err))
    raise plot_err
