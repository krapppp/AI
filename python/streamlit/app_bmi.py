# import streamlit as st

# # 페이지 제목
# st.title("🧮 BMI 계산기")

# st.markdown("**키(cm)**와 **몸무게(kg)**를 입력하고, 아래 버튼을 눌러 BMI를 확인해보세요.")

# # 슬라이더로 키와 몸무게 입력 받기
# height = st.slider("📏 키 (cm)", min_value=100, max_value=220, value=170, step=1)
# weight = st.slider("⚖️ 몸무게 (kg)", min_value=30, max_value=150, value=60, step=1)

# # BMI 계산 함수
# def calculate_bmi(height_cm, weight_kg):
#     height_m = height_cm / 100
#     bmi = weight_kg / (height_m ** 2)
#     return round(bmi, 2)

# # BMI 범주 판단 함수
# def bmi_category(bmi):
#     if bmi < 18.5:
#         return "🔵 저체중"
#     elif 18.5 <= bmi < 23:
#         return "🟢 정상"
#     elif 23 <= bmi < 25:
#         return "🟡 과체중"
#     else:
#         return "🔴 비만"

# # 버튼 누르면 결과 출력
# if st.button("BMI 예측하기"):
#     bmi = calculate_bmi(height, weight)
#     category = bmi_category(bmi)

#     st.subheader(f"당신의 BMI는 **{bmi}** 입니다.")
#     st.success(f"체형 분류: {category}")

import streamlit as st
import pickle
filename_pickle = '../deep/bmi20000_svm.pkl'
#pickle을 사용하여 모델 불러오기
loaded_model_pickle = None
with open(filename_pickle, 'rb') as file:
    loaded_model_pickle = pickle.load(file)
print(f'모델이 "{filename_pickle}" 파일에서 성공적으로 불러와졌습니다 (pickle).')

# streamlit

st.header('BMI data')

st_height = st.slider('키(cm)', 100, 220, 160)
st_weight = st.slider('몸무게(kg)', 40, 120, 60)

# 예측 버튼
if st.button('BMI 예측하기'):
    bmi_dict = {'thin': 1, 'normal': 2, 'fat': 3}
    reverse_mapping_dict = {value: key for key, value in bmi_dict.items()}
    features = [[st_height, st_weight]]
    prediction = loaded_model_pickle.predict(features)
    st.success(f'{st_height}, {st_weight} : {reverse_mapping_dict.get(prediction[0])} 입니다.')