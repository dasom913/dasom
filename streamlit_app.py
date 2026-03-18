import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="centered")

# 프로필 섹션
st.markdown("""
<style>
    .profile-header {
        text-align: center;
        padding: 20px 0;
    }
    .profile-name {
        font-size: 3em;
        font-weight: bold;
        margin: 10px 0;
    }
    .profile-title {
        font-size: 1.5em;
        color: #1f77b4;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class="profile-header">
        <div style="font-size: 80px; margin: 20px 0;">👤</div>
        <div class="profile-name">김다은</div>
        <div class="profile-title">인천대 수학교육과</div>
        <p style="color: gray; font-size: 1.1em;">📍 경기도 시흥시 거주</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 소개 섹션
st.header("🎯 소개")
st.write("""
안녕하세요 수학교육과 2학년 김다은입니다
""")

st.divider()

# 경력 섹션
st.header("💼 경력")
with st.expander("회사명 1 - 직책 (2020.01 ~ 2024.12)"):
    st.write("""
    **주요 업무:**
    - 업무 내용 1
    - 업무 내용 2
    - 업무 내용 3
    """)

with st.expander("회사명 2 - 직책 (2019.01 ~ 2019.12)"):
    st.write("""
    **주요 업무:**
    - 업무 내용 1
    - 업무 내용 2
    """)

st.divider()

# 기술/스킬 섹션
st.header("🛠️ 기술 & 스킬")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("프로그래밍 언어")
    st.write("• Python")
    st.write("• JavaScript")
    st.write("• SQL")

with col_b:
    st.subheader("주요 기술")
    st.write("• Streamlit")
    st.write("• Django")
    st.write("• REST API")

st.divider()

# 학력 섹션
st.header("🎓 학력")
st.write("""
**인천대학교** - 수학교육과  
*재학중*
""")

st.divider()

# 프로젝트 섹션
st.header("🚀 프로젝트")

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.subheader("프로젝트 1")
    st.write("""
    **설명:** 프로젝트에 대한 간단한 설명
    
    **기술:** Python, Streamlit
    """)

with col_p2:
    st.subheader("프로젝트 2")
    st.write("""
    **설명:** 프로젝트에 대한 간단한 설명
    
    **기술:** JavaScript, React
    """)

st.divider()

# 연락처 섹션
st.header("📞 연락처")

col_email, col_phone, col_link = st.columns(3)

with col_email:
    st.info("📧\nemail@example.com")

with col_phone:
    st.info("📱\n010-XXXX-XXXX")

with col_link:
    st.info("🔗\nlinkedin.com/in/yourprofile")

st.divider()

# 푸터
st.markdown("""
---
<div style="text-align: center; color: gray; padding: 20px 0;">
    © 2026 당신의 이름. All rights reserved.
</div>
""", unsafe_allow_html=True)
