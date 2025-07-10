import streamlit as st

# 세션 초기화
if 'key' not in st.session_state:
    st.session_state['key'] = 'hgd'

# 읽기
st.write('현재 key 값:', st.session_state['key'])

# 값 변경
st.session_state.key = 'value2'
st.write('변경된 key 값:', st.session_state.key)

# 전체 출력
st.write('전체 session_state:', st.session_state)

# 존재하지 않는 키 접근 시 예외 처리
if 'value' in st.session_state:
    st.write(st.session_state['value'])
else:
    st.write('⚠️ "value" 키는 존재하지 않습니다.')

# 안전한 삭제
if 'key' in st.session_state:
    del st.session_state['key']

# 전체 삭제 안전하게
for k in list(st.session_state.keys()):
    del st.session_state[k]

# 입력 필드
st.text_input("Your name", key="name")

# 값 확인
st.write('입력된 이름:', st.session_state.get("name", ""))

# 폼
def form_callback():
    st.write("슬라이더 값:", st.session_state.my_slider)
    st.write("체크박스 상태:", st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
