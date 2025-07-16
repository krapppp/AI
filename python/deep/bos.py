import streamlit as st
import numpy as np
import joblib

# 모델 불러오기
model_filename = 'boston_lg_clf.joblib'
model = joblib.load(model_filename)

st.title('보스턴 집값 예측기')
st.write('13개 특성 값을 조정해서 예측해보세요.')

# 13개 feature 이름
features = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
    'RM', 'AGE', 'DIS', 'RAD', 'TAX',
    'PTRATIO', 'B', 'LSTAT'
]

# 슬라이더 UI로 13개 feature 값 받기
user_inputs = []

user_inputs.append(st.slider('CRIM: 범죄율', 0.0, 100.0, 0.1))
user_inputs.append(st.slider('ZN: 25,000 평방피트 이상 거주지역 비율', 0.0, 100.0, 0.0))
user_inputs.append(st.slider('INDUS: 비상업지역 비율', 0.0, 30.0, 5.0))
user_inputs.append(st.slider('CHAS: 찰스강 주변 여부 (0:아님, 1:맞음)', 0, 1, 0))
user_inputs.append(st.slider('NOX: 산화질소 농도', 0.3, 1.0, 0.5))
user_inputs.append(st.slider('RM: 평균 방 개수', 3.0, 9.0, 6.0))
user_inputs.append(st.slider('AGE: 1940년 이전 비율', 0.0, 100.0, 50.0))
user_inputs.append(st.slider('DIS: 중심지 거리', 1.0, 12.0, 4.0))
user_inputs.append(st.slider('RAD: 고속도로 접근성', 1, 24, 1))
user_inputs.append(st.slider('TAX: 재산세', 100, 750, 300))
user_inputs.append(st.slider('PTRATIO: 학생-교사 비율', 10.0, 25.0, 15.0))
user_inputs.append(st.slider('B: 흑인 비율 지수', 0.0, 400.0, 300.0))
user_inputs.append(st.slider('LSTAT: 하위 계층 비율', 0.0, 40.0, 10.0))

# 예측 버튼
if st.button('집값 예측하기'):
    input_data = np.array(user_inputs).reshape(1, -1)
    prediction = model.predict(input_data)
    st.write(f'예상 집값: **${round(prediction[0]*1000)}**')
