import streamlit as st
from Ai import find_keywords  
st.title('Resume tweaker')

if st.file_uploader('gimme a Resume'):
    st.text('hello world')
else:
    pass
