import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

a= {"name":[1,2,5,2,6],"address":[3,5,7,3,1]}
b=pd.DataFrame(a)
b.plot("name","address")
st.write(b)
