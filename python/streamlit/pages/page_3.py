import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="얼굴 인식 비교", layout="centered")
st.markdown("# 얼굴 인식 비교")
st.sidebar.markdown("# Page 3 🎉")

# ✅ 사이드바에서 입력 방식 선택
mode = st.sidebar.radio("얼굴 인식 방식 선택", ["이미지 업로드", "웹캠 캡처 (내장 카메라)"])

# ✅ 공통: 얼굴 인식 함수 (Haar 적용)
def detect_faces(image_bgr):
    image_gs = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    cascade_file = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    face_list = cascade.detectMultiScale(
        image_gs,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in face_list:
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (255, 0, 0), 3)

    return image_bgr, len(face_list)

# ✅ 이미지 업로드 방식
if mode == "이미지 업로드":
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        result_bgr, count = detect_faces(image_bgr)
        result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)

        st.success(f"✅ 얼굴 {count}개 감지됨" if count > 0 else "⚠️ 얼굴을 감지하지 못했습니다.")

        col1, col2 = st.columns(2)
        with col1:
            st.image(image_np, caption="원본", use_container_width=True)
        with col2:
            st.image(result_rgb, caption="얼굴 인식 결과", use_container_width=True)

# ✅ 웹캠 캡처 방식 (내장 카메라 사용)
elif mode == "웹캠 캡처 (내장 카메라)":
    st.info("📡 웹캠으로 실시간 얼굴 인식을 수행합니다. '정지' 버튼을 누르면 종료됩니다.")

    run = st.checkbox("▶️ 실시간 인식 시작")

    # 얼굴 감지를 위한 이미지 자리 만들기
    FRAME_WINDOW = st.image([])

    cap = None
    if run:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("❌ 카메라를 열 수 없습니다.")
        else:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.warning("⚠️ 프레임을 가져오지 못했습니다.")
                    break

                # 얼굴 감지
                result_bgr, count = detect_faces(frame)
                result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)

                # 업데이트
                FRAME_WINDOW.image(result_rgb, channels="RGB")

                # run 상태 업데이트 체크 (checkbox 상태를 갱신)
                run = st.session_state.get('checkbox_value', run)

            cap.release()
            cv2.destroyAllWindows()
