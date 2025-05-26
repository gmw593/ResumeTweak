import streamlit as st
from Ai import find_keywords  
st.title('Resume tweaker')

##add session state
if "desc" not in st.session_state:
    st.session_state.desc = ''
    
if st.file_uploader('gimme a Resume'):
    with st.form('job descricription'):
        desc = st.text_area('enter the job description')
        submitted = st.form_submit_button('Submit')

        if submitted:
            st.session_state.desc = desc

    st.write(st.session_state.desc)
else:
    pass

