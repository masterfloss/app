import streamlit as st
import pandas as pd

a= {"name":[1,2,5,2,6],"address":[3,5,7,3,1]}
b=pd.DataFrame(a)

st.write(b)
st.line_chart(b)
