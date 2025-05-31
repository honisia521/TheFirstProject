import streamlit as st
import folium
from streamlit.components.v1 import html

# 여행지 데이터 (이름, 위도, 경도, 간단한 설명)
travel_spots = [
    {"name": "도쿄", "lat": 35.682839, "lon": 139.759455, "desc": "쇼핑과 음식의 천국, 일본의 수도."},
    {"name": "오사카", "lat": 34.6937, "lon": 135.5023, "desc": "문화를 맛보고 타코야끼를 즐기자."},
    {"name": "방콕", "lat": 13.7563, "lon": 100.5018, "desc": "저렴한 물가와 활기찬 시장, 태국의 수도."},
    {"name": "다낭", "lat": 16.0544, "lon": 108.2022, "desc": "한적하고 아름다운 해변 도시."},
    {"name": "하와이", "lat": 21.3069, "lon": -157.8583, "desc": "평생 한 번쯤은 꿈꾸는 로맨틱 휴양지."},
    {"name": "파리", "lat": 48.8566, "lon": 2.3522, "desc": "에펠탑과 예술의 도시."},
    {"name": "바르셀로나", "lat": 41.3851, "lon": 2.1734, "desc": "가우디의 도시, 축구 팬들의 성지."},
    {"name": "세부", "lat": 10.3157, "lon": 123.8854, "desc": "저렴하고 아름다운 휴양지."},
    {"name": "푸켓", "lat": 7.8804, "lon": 98.3923, "desc": "힐링과 액티비티가 가득한 섬."},
    {"name": "로마", "lat": 41.9028, "lon": 12.4964, "desc": "역사와 예술의 본고장."},
]

st.set_page_config(page_title="한국인이 사랑하는 여행지", layout="wide")
st.title("💖 한국인이 사랑하는 TOP 10 해외 여행지")

# 지도 중심은 중간 좌표
center_lat = sum([spot["lat"] for spot in travel_spots]) / len(travel_spots)
center_lon = sum([spot["lon"] for spot in travel_spots]) / len(travel_spots)

# 지도 생성
m = folium.Map(location=[center_lat, center_lon], zoom_start=2)

# 마커 추가
for spot in travel_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"<b>{spot['name']}</b><br>{spot['desc']}",
        icon=folium.Icon(color="green", icon="heart"),
    ).add_to(m)

# 지도 삽입
html(m._repr_html_(), height=600, width=1000)
