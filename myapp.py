import streamlit as st
import pandas as pd

a= {"serie 1":[1,2,5,2,6],"fora de serie":[3,5,7,3,1]}
b=pd.DataFrame(a)
st.checkbox('aa')
st.write(b)
st.line_chart(b)
