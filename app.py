import streamlit as st
st.title('Hello Streamlit')
name = st.text_input('Enter username')
button = st.button('Greet')
if button:
  st.write('Hello, '+name+'! Welcome to Streamlit')
