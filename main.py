import streamlit as st
import pandas as pd
import altair as alt
import os

# 제목
st.title("🌍 MBTI 유형별 비율이 가장 높은 국가 TOP10")

# 기본 파일 경로
file_path = "countriesMBTI_16types.csv"

# CSV 파일 로드 함수
def load_data():
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
        if uploaded_file is not None:
            return pd.read_csv(uploaded_file)
        else:
            return None

# 데이터 불러오기
df = load_data()

if df is not None:
    # MBTI 유형 선택
    mbti_types = df.columns[1:].tolist()  # Country 제외
    selected_type = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

    # 선택한 MBTI 유형별 Top10 추출
    top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

    # Altair 그래프
    chart = (
        alt.Chart(top10)
        .mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8)
        .encode(
            x=alt.X(selected_type, title=f"{selected_type} 비율"),
            y=alt.Y("Country", sort="-x"),
            tooltip=["Country", selected_type]
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터 표시
    st.dataframe(top10.reset_index(drop=True))
else:
    st.info("기본 CSV 파일이 없으니 업로드해주세요.")
