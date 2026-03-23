import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
import os
from pathlib import Path

# 폰트 파일 경로 설정
font_path = Path(__file__).parent.parent / 'fonts' / 'NanumGothic-Bold.ttf'

# 한글 폰트 설정
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    plt.rcParams['font.family'] = 'NanumGothic'
else:
    print(f"폰트 파일을 찾을 수 없습니다: {font_path}")

plt.rcParams['axes.unicode_minus'] = False

# 페이지 설정
st.set_page_config(page_title="데이터 시각화", layout="wide")

st.title("📊 데이터 시각화 예제")
st.write("matplotlib을 사용한 다양한 그래프 예제입니다.")

st.divider()

# 1. 막대 그래프
st.header("1️⃣ 막대 그래프 (Bar Chart)")

col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    categories = ['서울', '부산', '대구', '인천', '광주', '대전']
    values = [9776, 3569, 2419, 2874, 1500, 1402]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
    
    bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)
    
    # 막대 위에 값 표시
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:,}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('도시', fontsize=12, fontweight='bold')
    ax.set_ylabel('인구 (만 명)', fontsize=12, fontweight='bold')
    ax.set_title('2024년 주요 도시별 인구', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.info("""
    **막대 그래프**
    
    - 카테고리별 비교에 적합
    - 값의 크기 비교 용이
    - 도시별 인구 비교 예제
    """)

st.divider()

# 2. 선 그래프
st.header("2️⃣ 선 그래프 (Line Chart)")

col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
    temperature = [5, 6, 12, 18, 23, 28, 31, 30, 24, 15, 8, 3]
    humidity = [45, 48, 55, 60, 65, 70, 75, 72, 68, 58, 50, 46]
    
    ax.plot(months, temperature, marker='o', linewidth=2.5, markersize=8, 
            label='온도 (℃)', color='#FF6B6B', markerfacecolor='white', markeredgewidth=2)
    ax.plot(months, humidity, marker='s', linewidth=2.5, markersize=8, 
            label='습도 (%)', color='#4ECDC4', markerfacecolor='white', markeredgewidth=2)
    
    ax.set_xlabel('월', fontsize=12, fontweight='bold')
    ax.set_ylabel('값', fontsize=12, fontweight='bold')
    ax.set_title('2024년 월별 기후 데이터', fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.info("""
    **선 그래프**
    
    - 시간 경과에 따른 추이 표현
    - 여러 계열 비교 가능
    - 월별 기후 변화 예제
    """)

st.divider()

# 3. 산점도
st.header("3️⃣ 산점도 (Scatter Plot)")

col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    study_hours = np.random.uniform(1, 10, 50)
    test_scores = study_hours * 10 + np.random.normal(0, 10, 50)
    test_scores = np.clip(test_scores, 0, 100)
    
    scatter = ax.scatter(study_hours, test_scores, s=100, alpha=0.6, 
                        c=test_scores, cmap='viridis', edgecolors='black', linewidth=1)
    
    # 추세선 추가
    z = np.polyfit(study_hours, test_scores, 1)
    p = np.poly1d(z)
    ax.plot(study_hours, p(study_hours), "r--", linewidth=2, label='추세선')
    
    ax.set_xlabel('학습 시간 (시간)', fontsize=12, fontweight='bold')
    ax.set_ylabel('시험 점수', fontsize=12, fontweight='bold')
    ax.set_title('학습 시간과 시험 점수 관계', fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('시험 점수', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.info("""
    **산점도**
    
    - 두 변수 간의 관계 표현
    - 패턴 및 상관관계 파악
    - 학습 시간과 성적의 관계 예제
    """)

st.divider()

# 4. 히스토그램
st.header("4️⃣ 히스토그램 (Histogram)")

col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)
    
    n, bins, patches = ax.hist(data, bins=30, color='#45B7D1', edgecolor='black', 
                               alpha=0.7, linewidth=1.5)
    
    # 컬러 그래디언트 적용
    cm = plt.cm.Blues
    for i, patch in enumerate(patches):
        patch.set_facecolor(cm(0.4 + 0.5 * i / len(patches)))
    
    ax.set_xlabel('값', fontsize=12, fontweight='bold')
    ax.set_ylabel('빈도', fontsize=12, fontweight='bold')
    ax.set_title('1000개 샘플의 분포', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.info("""
    **히스토그램**
    
    - 데이터의 분포 시각화
    - 도수 분포 표표현
    - 정규분포 예제
    """)

st.divider()

# 5. 원형 그래프
st.header("5️⃣ 원형 그래프 (Pie Chart)")

col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(8, 8))
    
    labels = ['한국어', '수학', '영어', '과학', '사회']
    sizes = [25, 20, 25, 15, 15]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    explode = (0.05, 0, 0.05, 0, 0)
    
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                        colors=colors, explode=explode,
                                        startangle=90, textprops={'fontsize': 11})
    
    # 특정 텍스트 굵게
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    for text in texts:
        text.set_fontweight('bold')
        text.set_fontsize(11)
    
    ax.set_title('과목별 수강 비율', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.info("""
    **원형 그래프**
    
    - 전체에서 각 부분의 비율 표현
    - 구성비 시각화
    - 과목별 수강 비율 예제
    """)

st.divider()

# 6. 박스 플롯
st.header("6️⃣ 박스 플롯 (Box Plot)")

col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    data_a = np.random.normal(75, 10, 100)
    data_b = np.random.normal(80, 12, 100)
    data_c = np.random.normal(78, 8, 100)
    
    bp = ax.boxplot([data_a, data_b, data_c],
                     labels=['1학기', '2학기', '3학기'],
                     patch_artist=True,
                     notch=True,
                     showmeans=True)
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_ylabel('시험 점수', fontsize=12, fontweight='bold')
    ax.set_title('학기별 시험 점수 분포', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.info("""
    **박스 플롯**
    
    - 데이터의 사분위수 범위 표현
    - 이상치 탐지
    - 학기별 점수 분포 예제
    """)

st.divider()

# 데이터 테이블 예제
st.header("📋 샘플 데이터")

sample_data = pd.DataFrame({
    '도시': ['서울', '부산', '대구', '인천', '광주', '대전'],
    '인구 (만 명)': [9776, 3569, 2419, 2874, 1500, 1402],
    '면적 (㎢)': [605, 770, 885, 1032, 502, 540],
    '성장률 (%)': [1.2, 0.5, 0.8, 1.5, 0.3, 0.9]
})

st.dataframe(sample_data, use_container_width=True)

st.divider()

# 푸터
st.markdown("""
---
<div style="text-align: center; color: gray; padding: 20px 0;">
    💡 Tip: Streamlit + Matplotlib으로 만든 다양한 데이터 시각화 예제입니다.
</div>
""", unsafe_allow_html=True)
