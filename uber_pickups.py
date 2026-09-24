import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
#====================================================================

st.title('Uber pickups in NYC')
st.write('Hello world!')

#====================================================================

n1= st.number_input("Insert a number")

n2 = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."

#selectionbox-----------------------------------
)
option = st.selectbox(
    "How would you like to be contacted?",
    ("Addition", "Subtraction", "Division", "Multiplication"),
)

st.write("You selected:", option)

#Buttons------------------------------------------
# if st.button('minus'):
#     st.write(n1-n2)

# if st.button('plus'):
#     st.write(n1 + n2)

# if st.button('multiply'):
#     st.write(n1*n2)

# if st.button('divied'):
#     st.write(n1/n2)