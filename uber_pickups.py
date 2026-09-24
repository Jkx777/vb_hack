import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
#====================================================================

st.title('Uber pickups in NYC')
st.write('Hello world!')

#====================================================================
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
#====================================================================

n1= st.number_input("Insert a number")

n2 = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)

if st.button('minus'):
    st.write(n1-n2)

if st.button('plus'):
    st.write(n1 + n2)

if st.button('multiply'):
    st.write(n1*n2)

if st.button('divied'):
    st.write(n1/n2)