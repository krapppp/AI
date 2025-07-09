import streamlit as st
import pandas as pd

df= pd.DataFrame({
 'col1': [1, 2, 3, 4],
 'col2': [10, 20, 30, 40]
 })
st.dataframe(df) # 인터랙티브테이블
st.table(df)      # 정적테이블
st.metric(label="온도", value="25°C", delta="1.5°C") # KPI 지표