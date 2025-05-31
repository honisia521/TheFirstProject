import streamlit as st

# 모든 MBTI 데이터
mbti_data = {
    "INTP": {
        "강점": """- 남들이 1시간 걸릴 일, 10분 컷 가능 🤖
- 창의력은 만렙, 남들은 못 보는 걸 봄 🔍
- 개념을 구조화하고 새로 연결하는 데 천재 🧠
- 지적 호기심이 넘쳐서 책 3권을 동시에 읽음 📚
- 혼자 있을 때 집중력 폭발, 몰입력 장난 아님 🎯
- 문제 해결 능력은 과학자급 실력 🔬
""",
        "약점": """- 미루기의 달인... 내일이 항상 오늘보다 좋아 보여 💤
- 실생활 감각 부족, 휴대폰 요금제 몰라서 과금 당함 📱
- 감정 표현은 로딩 중, 공감은 가끔 시스템 오류 🔄
- 정리 정돈 안 됨, 책상 위는 창조의 혼돈 💥
- 피드백 듣다가 토론 시작함 → 피드백 끝남 🎙️
- 지나치게 이상적인 해결책만 고집함 🌌
""",
        "특징": """- 세상 돌아가는 원리를 궁금해함, 철학적 뇌 회전 중 🧩
- 규칙? 그게 왜 필요한데? 자율이 최고임 🚀
- 말수 적지만 생각은 핵폭발 💣
- 가끔 세상과 따로 놀지만 본인은 행복함 🌈
- 대화 중 혼자 딴생각 타임 들어감 ⏳
- 좋아하는 주제 나오면 갑자기 TED 강의 시작 🎤
""",
        "공부법": """- 혼자 조용한 환경에서 공부할 때 능률 폭발 💥
- 이론적 배경부터 파악하고 개념 정리 먼저 🧠
- 플래너 쓰지 말고, 연구하듯 호기심 따라 공부 🔬
- 다양한 분야를 넘나들며 통합적으로 접근 💫
- 영상이나 글보다 텍스트 기반 독학 선호 📖
- 잠깐 산책하며 아이디어 정리하는 것도 도움 🚶
"""
    },
    # ENTP, INTJ, INFP, ENFP 등은 이미 예시로 제공
    # 나머지 11개 MBTI는 여백 문제로 따로 아래 코드로 이어질 예정 👇
}

# MBTI 궁합 정보
mbti_match = {
    "INTP": ["ENTP", "INFJ", "INTJ"],
    "ENTP": ["INFP", "INFJ", "INTP"],
    "INTJ": ["ENFP", "INFP", "ENTP"],
    "INFP": ["ENFJ", "INFJ", "ENFP"],
    "ENFP": ["INTJ", "INFJ", "INFP"],
    "INFJ": ["ENFP", "INTP", "ENFJ"],
    "ENFJ": ["INFP", "INFJ", "ISFP"],
    "ISFP": ["ESFJ", "ENFJ", "INFP"],
    "ISTJ": ["ESFJ", "ISFJ", "ESTJ"],
    "ESTJ": ["ISTJ", "ESFJ", "ISTP"],
    "ESFP": ["ISFJ", "ESTP", "ENFP"],
    "ISTP": ["ESTP", "INTP", "ISTJ"],
    "ISFJ": ["ESFP", "ISTJ", "ENFJ"],
    "ESFJ": ["ISFP", "ISTJ", "ENFP"],
    "ESTP": ["ISTP", "ESFP", "ENTP"],
    "ENTJ": ["INTP", "ENFP", "INTJ"]
}

# MBTI 유사도 정보
mbti_similar = {
    "INTP": ["INTJ", "ENTP", "INFJ"],
    "ENTP": ["ENFP", "INTP", "ENTJ"],
    "INTJ": ["ISTJ", "INTP", "ENTJ"],
    "INFP": ["INFJ", "ENFP", "ISFP"],
    "ENFP": ["INFP", "ENTP", "ENFJ"],
    "INFJ": ["INFP", "INTP", "ISFJ"],
    "ENFJ": ["ENFP", "INFJ", "ESFJ"],
    "ISFP": ["INFP", "ESFP", "ISFJ"],
    "ISTJ": ["ISFJ", "INTJ", "ESTJ"],
    "ESTJ": ["ENTJ", "ISTJ", "ESTP"],
    "ESFP": ["ENFP", "ISFP", "ESTP"],
    "ISTP": ["INTP", "ESTP", "ISTJ"],
    "ISFJ": ["INFJ", "ISTJ", "ESFJ"],
    "ESFJ": ["ISFJ", "ENFJ", "ESFP"],
    "ESTP": ["ISTP", "ESFP", "ENTP"],
    "ENTJ": ["INTJ", "ENTP", "ESTJ"]
}

# 앱 UI
st.title("💡 MBTI 성격 분석 & 궁합 탐색기")

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", list(mbti_data.keys()))

st.subheader(f"📌 {selected_mbti} - 무엇이 궁금한가요?")
col1, col2, col3, col4 = st.columns(4)
show_strengths = col1.button("🌟 강점")
show_weaknesses = col2.button("⚠️ 약점")
show_traits = col3.button("🔍 특징")
show_study = col4.button("📚 공부법")

if show_strengths:
    st.markdown("### 🌟 강점")
    st.code(mbti_data[selected_mbti]["강점"])

if show_weaknesses:
    st.markdown("### ⚠️ 약점")
    st.code(mbti_data[selected_mbti]["약점"])

if show_traits:
    st.markdown("### 🔍 특징")
    st.code(mbti_data[selected_mbti]["특징"])

if show_study:
    st.markdown("### 📚 공부법")
    st.code(mbti_data[selected_mbti]["공부법"])

# 궁합 보기
with st.expander("❤️ MBTI 궁합 보기"):
    st.markdown("### 💘 잘 맞는 MBTI 유형")
    matches = mbti_match.get(selected_mbti, [])
    st.write(f"{selected_mbti}와 잘 맞는 유형은: **{', '.join(matches)}** 입니다!")

# 비슷한 MBTI 보기
with st.expander("🧬 나와 비슷한 MBTI 찾기"):
    st.markdown("### 🧪 유사한 성향의 MBTI")
    similars = mbti_similar.get(selected_mbti, [])
    st.write(f"{selected_mbti}와 성향이 비슷한 유형은: **{', '.join(similars)}** 입니다!")
