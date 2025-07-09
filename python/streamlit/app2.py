import streamlit as st

st.title('제목(Title)')
st.header('헤더(Header)')
st.subheader('서브헤더(SubHeader)')
st.text('일반텍스트(Text)')
st.markdown('"Markdown" **지원** - markdown')

st.markdown("`Markdown`도 **지원**합니다.") # 마크다운문법지원
# cc=```import numpy as np
# n1=np.array([0,1,2])
# ```

st.code('import pandas as pd')
st.code('df1=pd.Dataframe([0,1,2])')
st.code('print("hello, streamlit")')
print("hello, streamlit")
