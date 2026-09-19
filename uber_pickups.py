import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
st.write('Hello world!')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')


import streamlit as st

n1, n2 = st.number_input("Insert a number"), st.number_input("Insert a number")
if st.button('minus'):
    st.write(n1-n2)

if st.button('plus'):
    st.write(n1 + n2)

if st.button('multiply'):
    st.write(n1*n2)
    
if st.button('divie'):
    st.write(n1/n2)