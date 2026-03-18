import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="Streamlit 요소 데모", layout="wide")

# 제목
st.title("🎈 Streamlit 기본 요소 데모")
st.write("이 페이지는 Streamlit이 제공하는 다양한 UI 요소들을 보여줍니다.")

# ==================== 텍스트 요소 ====================
st.header("📝 텍스트 요소")

st.subheader("제목과 텍스트")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**Bold** 텍스트와 _Italic_ 텍스트를 지원합니다.")
st.code("print('코드 블록도 표시할 수 있습니다')", language="python")

# ==================== 입력 요소 ====================
st.header("🎮 입력 요소 (Input Widgets)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("텍스트 입력")
    name = st.text_input("이름을 입력하세요:", value="홍길동")
    st.write(f"입력하신 이름: {name}")
    
    email = st.text_area("메시지를 입력하세요:", height=100)
    if email:
        st.success(f"메시지 입력됨: {len(email)}자")

with col2:
    st.subheader("선택 요소")
    option = st.selectbox("옵션 선택:", ["옵션 1", "옵션 2", "옵션 3", "옵션 4"])
    st.write(f"선택된 옵션: {option}")
    
    multi = st.multiselect("여러 개 선택:", ["사과", "바나나", "딸기", "포도"], default=["사과"])
    st.write(f"선택된 항목: {', '.join(multi)}")

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("숫자 입력")
    age = st.slider("나이를 선택하세요:", 0, 100, 25)
    st.write(f"선택된 나이: {age}세")
    
    number = st.number_input("숫자를 입력하세요:", value=10, step=1)
    st.write(f"입력된 숫자: {number}")

with col4:
    st.subheader("선택 요소")
    agree = st.checkbox("약관에 동의합니다")
    st.write(f"동의 여부: {'✅ 동의' if agree else '❌ 미동의'}")
    
    choice = st.radio("좋아하는 색상:", ["🔴 빨강", "🟢 초록", "🔵 파랑"])
    st.write(f"선택: {choice}")

# ==================== 버튼 ====================
st.header("🔘 버튼")

col5, col6, col7 = st.columns(3)

with col5:
    if st.button("일반 버튼"):
        st.balloons()
        st.success("버튼이 클릭되었습니다!")

with col6:
    if st.button("⭐ 특별한 버튼", key="special"):
        st.info("특별한 버튼이 클릭되었습니다!")

with col7:
    if st.download_button("📥 파일 다운로드", data="안녕하세요!", file_name="example.txt"):
        st.success("다운로드되었습니다!")

# ==================== 데이터 표시 ====================
st.header("📊 데이터 표시")

st.subheader("데이터프레임")
df = pd.DataFrame({
    "이름": ["Alice", "Bob", "Charlie", "Diana"],
    "나이": [25, 30, 35, 28],
    "도시": ["서울", "부산", "대구", "인천"]
})
st.dataframe(df, use_container_width=True)

st.subheader("테이블 (수정 불가)")
st.table(df)

st.subheader("JSON 데이터")
st.json({"이름": "홍길동", "나이": 30, "취미": ["독서", "영화", "게임"]})

# ==================== 차트 ====================
st.header("📈 차트")

chart_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 120, 200, 180, 250]
})

col8, col9 = st.columns(2)

with col8:
    st.subheader("라인 차트")
    st.line_chart(chart_data.set_index("Month")["Sales"])

with col9:
    st.subheader("바 차트")
    st.bar_chart(chart_data.set_index("Month")["Sales"])

st.subheader("에어리어 차트")
st.area_chart(chart_data.set_index("Month"))

# ==================== 메시지와 알림 ====================
st.header("💬 메시지와 알림")

col10, col11, col12, col13 = st.columns(4)

with col10:
    st.success("✅ 성공 메시지")

with col11:
    st.info("ℹ️ 정보 메시지")

with col12:
    st.warning("⚠️ 경고 메시지")

with col13:
    st.error("❌ 에러 메시지")

# ==================== 진행 표시 ====================
st.header("⏳ 진행 표시")

progress = st.slider("진행 상황:", 0, 100, 50)
st.progress(progress / 100)

# ==================== 확장/축소 영역 ====================
st.header("📂 확장/축소 영역 (Expander)")

with st.expander("클릭해서 더보기"):
    st.write("숨겨진 내용입니다!")
    st.image("https://via.placeholder.com/300", caption="샘플 이미지")

# ==================== 사이드바 ====================
st.sidebar.header("⚙️ 설정")
theme = st.sidebar.radio("테마 선택:", ["일반", "어두운 모드", "밝은 모드"])
st.sidebar.write(f"선택된 테마: {theme}")

sidebar_text = st.sidebar.text_input("사이드바 입력:")
if sidebar_text:
    st.sidebar.write(f"입력하신 텍스트: {sidebar_text}")

# ==================== 세션 상태 ====================
st.header("💾 세션 상태 (Session State)")

if "count" not in st.session_state:
    st.session_state.count = 0

col14, col15 = st.columns(2)

with col14:
    if st.button("+1 증가"):
        st.session_state.count += 1

with col15:
    if st.button("-1 감소"):
        st.session_state.count -= 1

st.write(f"현재 카운트: {st.session_state.count}")
