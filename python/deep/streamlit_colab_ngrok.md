# localtunnel 사용

https://discuss.streamlit.io/t/how-to-launch-streamlit-app-from-google-colab-notebook/42399


# ngrok 사용

**기본 원리:**

Google Colab은 가상 머신 환경을 제공하며, 이 가상 머신은 외부에서 직접 접속하기 어렵습니다. 따라서 Streamlit 앱을 외부에서 접속 가능하게 하려면 "터널링"이라는 기술을 사용해야 합니다. 가장 흔하게 사용되는 방법은 `ngrok`을 이용하는 것입니다. `localtunnel`도 가능하지만, `ngrok`이 더 널리 사용되고 안정적입니다.

**단계별 설명:**

1.  **Streamlit 앱 설치 및 작성:**
    먼저 Colab 노트북에서 Streamlit을 설치하고 앱을 작성해야 합니다.

    ```python
    !pip install streamlit
    ```

    예시 `app.py` 파일 생성:

    ```python
    %%writefile app.py
    import streamlit as st

    st.title("My Streamlit App on Colab")
    st.write("Hello from Google Colab!")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")
    ```

2.  **`ngrok` 설치 및 인증:**
    `ngrok`을 설치하고, `ngrok` 웹사이트에서 발급받은 인증 토큰을 연결해야 합니다.

    ```python
    !pip install pyngrok
    ```

    `ngrok` 토큰 설정 (회원가입 후 [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) 에서 토큰을 얻을 수 있습니다):

    ```python
    from pyngrok import ngrok
    ngrok_auth_token = "YOUR_NGROK_AUTH_TOKEN" # 여기에 실제 ngrok 토큰을 입력하세요
    ngrok.set_auth_token(ngrok_auth_token)
    ```

3.  **Streamlit 앱 실행 및 `ngrok` 터널링:**
    이제 Streamlit 앱을 백그라운드에서 실행하고, `ngrok`을 사용하여 터널을 생성합니다. Streamlit은 기본적으로 8501 포트를 사용합니다.

    ```python
    # Streamlit 앱을 백그라운드에서 실행
    !streamlit run app.py &

    # ngrok 터널 시작
    public_url = ngrok.connect(port=8501)
    print(f"Streamlit App Public URL: {public_url}")
    ```

    `- &`는 백그라운드에서 명령을 실행하도록 합니다. 이렇게 해야 Streamlit 앱이 실행되는 동안 다음 셀에서 `ngrok`을 실행할 수 있습니다.

4.  **외부 접속:**
    위 코드를 실행하면 `Streamlit App Public URL:` 뒤에 `https://RANDOM_STRING.ngrok-free.app`와 같은 형태의 URL이 출력됩니다. 이 URL을 웹 브라우저에 입력하면 외부에서 Colab에서 실행 중인 Streamlit 앱에 접속할 수 있습니다.

**주의사항:**

  * **Colab 런타임 종료:** Colab 런타임이 종료되면 Streamlit 앱도 종료되고 `ngrok` 터널도 끊어집니다. 따라서 세션을 유지해야 합니다.
  * **무료 `ngrok` 제한:** 무료 `ngrok` 계정은 세션 시간이 제한될 수 있으며, 터널 URL이 세션마다 변경됩니다. 장기적인 사용이나 고정된 URL이 필요하다면 `ngrok` 유료 플랜을 고려해야 합니다.
  * **보안:** `ngrok`을 통해 외부에 노출되는 앱이므로, 중요한 정보나 민감한 데이터를 다루는 앱이라면 보안에 각별히 유의해야 합니다.
  * **Streamlit 포트:** Streamlit은 기본적으로 8501 포트를 사용하지만, 다른 포트를 사용하도록 설정할 수도 있습니다. 이 경우 `ngrok.connect()` 함수의 `port` 인자도 해당 포트 번호로 변경해야 합니다.

이 단계를 따르면 Google Colab 터미널을 통해 Streamlit 앱을 시작하고 외부에서 성공적으로 접속할 수 있습니다.