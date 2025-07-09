import streamlit as st
import pandas as pd
import numpy as np

# 1. 버튼(Button)
st.subheader('버튼')
if st.button('눌러보세요'):
   st.write('버튼이 눌렸습니다!')

# 2. 셀렉트박스(Selectbox)
st.subheader('셀렉트박스')
option = st.selectbox(
'가장 좋아하는 동물은?',
   ('강아지', '고양이', '앵무새')
)
st.write(f'선택 : {option}')

# 3. 슬라이더(Slider)
st.subheader('슬라이더')
age= st.slider('나이를 선택하세요.', 0, 100, 25)
st.write(f'당신의 나이는 {age}세 입니다.')

# 4. 텍스트 입력(Text Input)
st.subheader('텍스트 입력')
name= st.text_input('이름을 입력하세요.', '홍길동')
st.write(f'안녕하세요, {name}님!')

# 사이드바에 위젯 추가하기
add_selectbox = st.sidebar.selectbox(
    "어떤것을보시겠습니까?",
    ("홈", "데이터", "차트")
 )

# 예제 데이터프레임 생성
data = {
    '연령대': ['10대', '20대', '30대', '40대', '50대', '60대 이상'],
    '이용건수': np.random.randint(1000, 5000, size=6)
}
df = pd.DataFrame(data)

col1, col2, col3 = st.columns(3)
with col1:
  st.header("첫번째컬럼")
  st.write("내용1")
with col2:
  st.header("두번째컬럼")
  st.line_chart(data)
with col3:
  st.header("세번째컬럼")
  st.metric("10대", "1,234건", "+5%")
  st.metric("20대", "2,345건", "-2%")
  st.metric("30대", "3,210건", "+8%")

# 'count'가session_state에없으면0으로초기화
if 'count' not in st.session_state:
    st.session_state.count= 0
# 버튼을누를때마다count 1 증가
if st.button('카운트'):
    st.session_state.count+= 1

st.write('버튼클릭횟수:', st.session_state.count)