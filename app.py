import streamlit as st
st.title('Hello Streamlit')
name = st.text_input('Enter username')
st.button('Greet')
if st.button:
  st.text_area('Hello, '+name+'! Welcome to Streamlit')
