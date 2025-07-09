import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

csv = pd.read_csv('../csv/서울특별시_공공자전거_이용정보(월별)_22.12.csv', encoding='utf-8')
st.write(csv)
chart=alt.Chart(csv).mark_bar().encode( x='대여구분코드', y='연령대코드', size='이용건수', tooltip=['대여구분코드','연령대코드','이용건수'] )
st.write(chart)

chart = alt.Chart(csv).mark_bar().encode(
    x=alt.X('대여구분코드:N', title='대여구분'),
    y='이용건수:Q',
    color='연령대코드:N',
    xOffset='연령대코드:N',  # Altair 4.2 이상만 가능
    tooltip=['대여구분코드', '이용건수', '연령대코드']
)
st.altair_chart(chart, use_container_width=True)

import numpy as np

# 예시: 연령대별 전체 이용건수 집계 후 비율 시각화
pie_data = csv.groupby('연령대코드')['이용건수'].sum().reset_index()
pie_chart = alt.Chart(pie_data).mark_arc().encode(
    theta='이용건수:Q',
    color='연령대코드:N',
    tooltip=['연령대코드', '이용건수']
)
st.altair_chart(pie_chart, use_container_width=True)

# csv 경로 설정
# 1. raw 문자열 -> csv = pd.read_csv(r'C:\Users\ksa\Desktop\vs\pn\streamlit\서울특별시_공공자전거_이용정보(월별)_22.12.csv', encoding='utf-8')
# 2. 슬래시 -> csv = pd.read_csv('C:/Users/ksa/Desktop/vs/pn/streamlit/서울특별시_공공자전거_이용정보(월별)_22.12.csv', encoding='utf-8')
# 3. 백슬래시 두 번 사용 -> csv = pd.read_csv('C:\\Users\\ksa\\Desktop\\vs\\pn\\streamlit\\서울특별시_공공자전거_이용정보(월별)_22.12.csv', encoding='utf-8')