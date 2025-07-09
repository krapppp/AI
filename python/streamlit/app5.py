import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.write('hello, *world!* :sunglasses:')
st.write(':sunglasses: :bike: :balloon: :up: :muscle: ✅')
st.write(1234)

df1= pd.DataFrame({
'첫번째컬럼': [1,2,3,4],
'두번째컬럼': [10,20,30,40]
})
st.write(df1)
df2 = pd.DataFrame( np.random.randn(200,3), columns=['a','b','c'])
st.write( df2, '위는 DF1 입니다. 아래는 DF2 입니다.')
c = alt.Chart(df2).mark_circle().encode( x='a', y='b', size='c', tooltip=['a','b','c'] )
st.write(c)