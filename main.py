import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 공부법 추천", page_icon="📚", layout="centered")

# 헤더
st.title("✨ MBTI별 맞춤 공부법 추천 ✨")
st.markdown("공부할 때도 성격이 중요하다구요! 😎 아래에서 MBTI 유형을 선택해 보세요.")

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 유형별 추천 공부법
study_tips = {
    "INTJ": "📖 계획을 세우고 꾸준히! 장기적 목표를 달성하는 로드맵을 만들면 🔥 집중력이 배가돼요!",
    "INTP": "🤯 흥미 위주 탐구! 문제를 깊게 파고드는 탐구형 공부법이 잘 맞아요 🕵️‍♂️",
    "ENTJ": "🚀 목표지향! 마감일과 구체적인 성취 목표를 두면 성취욕구가 활활!",
    "ENTP": "🎤 토론 & 발표! 다른 사람과 아이디어를 주고받으며 배우면 ✨창의력 뿜뿜✨",
    "INFJ": "🧘‍♀️ 조용한 공간에서 몰입! 글쓰기와 정리 노트가 큰 도움이 돼요 ✍️",
    "INFP": "🎶 감성 자극! 좋아하는 음악, 색깔펜을 활용해 즐겁게 공부해 보세요 💖",
    "ENFJ": "👫 스터디 그룹! 함께 공부하면서 가르쳐주는 과정에서 실력이 쑥쑥 🌱",
    "ENFP": "🌈 다양하게! 게임화, 창의적인 방법으로 즐겁게 공부하는 게 포인트 🎮",
    "ISTJ": "📊 체크리스트! 꼼꼼하게 계획표를 세우고 체크하며 성취감을 느끼세요 ✅",
    "ISFJ": "🤝 누군가를 돕듯이! 교재 정리, 설명하면서 배우면 이해가 깊어져요 🪴",
    "ESTJ": "📅 규칙적인 루틴! 시간 관리 철저히 해서 꾸준히 밀고 나가세요 ⏰",
    "ESFJ": "💬 함께 공부! 친구와 서로 문제 내주기, 설명해주기 효과 만점 👏",
    "ISTP": "🔧 실습 위주! 직접 손으로 풀고, 실험하며 배울 때 몰입도가 올라가요 ⚡",
    "ISFP": "🎨 예쁘게 정리! 다이어그램, 색깔펜, 마인드맵으로 감각적으로 공부해 보세요 🌸",
    "ESTP": "🏃‍♂️ 액션 학습! 몸을 움직이며 암기하거나 퀴즈식 학습이 효과적 🎯",
    "ESFP": "🎉 즐겁게! 친구랑 문제풀이 게임, 노래처럼 암송하는 방식이 찰떡 🤩",
}

# 선택 박스
choice = st.selectbox("당신의 MBTI는 무엇인가요?", ["선택하세요"] + mbti_list)

# 추천 결과
if choice != "선택하세요":
    st.subheader(f"{choice} 유형의 추천 공부법 ✨")
    st.success(study_tips[choice])

    # 재미 요소 효과 랜덤 출력
    effects = [st.balloons, st.snow]
    random.choice(effects)()

    st.markdown("---")
    st.markdown("🌟 오늘도 당신의 공부를 응원합니다! 화이팅 💪")
