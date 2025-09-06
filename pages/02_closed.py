import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# 샘플 데이터 생성 (실제 데이터로 대체 가능)
@st.cache_data
def load_data():
    dates = pd.date_range(end=datetime.datetime.today(), periods=36, freq='M')
    companies = ['Apple', 'Microsoft', 'Saudi Aramco', 'Alphabet', 'Amazon',
                 'Nvidia', 'Berkshire Hathaway', 'Meta', 'TSMC', 'Tesla']
    
    data = []
    for company in companies:
        base = 500 + hash(company) % 1000  # 기업마다 기본값 다르게
        for i, date in enumerate(dates):
            fluctuation = base + i * (hash(company + str(i)) % 50 - 25)
            data.append({'Date': date, 'Company': company, 'MarketCap': abs(fluctuation * 1e9)})

    df = pd.DataFrame(data)
    return df

df = load_data()

# 사이드바에서 기업 선택
st.sidebar.title("📈 기업 선택")
selected_companies = st.sidebar.multiselect(
    "시가총액 변화를 보고 싶은 기업을 선택하세요",
    options=df['Company'].unique(),
    default=['Apple', 'Microsoft']
)

# 필터링된 데이터
filtered_df = df[df['Company'].isin(selected_companies)]

# Plotly 그래프
fig = px.line(filtered_df, x='Date', y='MarketCap', color='Company',
              title='전 세계 시가총액 TOP10 기업의 지난 3년간 변화',
              labels={'MarketCap': 'Market Cap (USD)', 'Date': '날짜'})

st.plotly_chart(fig, use_container_width=True)
