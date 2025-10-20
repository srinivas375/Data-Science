"""
- streamlit is a python framework for developing web applications especially for Data Science, Machine Learning & Artificial Intellegence in short time.
- Advantages:
    - compatable with scikit-learn, keras, numpy, pandas, pytorch, tensorflow, ..
    - maximizes the development speed
    - safe and secure web app development
    - no html, css, javascript needed
    - easy to deploy

To run any streamlit file, Use:
    streamlit run file_name.py
"""

# Basic text elements in streamlit


import streamlit as st

# title
st.title("Welcome to streamlit Web App")

# header
st.header("This is a header")

# sub-heading
st.subheader("This is a sub header")

# text 
st.text("This is simple text, writter by using streamlit 'text' function")

# markdown (used to apply markdown properties)
st.markdown("**Hello**, welcome to streamlit")
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")
st.markdown("#### Heading 4")
st.markdown("> block queote text")
st.markdown("`sample code`")
st.markdown("---") # horiznatal line
st.markdown("[Google](www.google.com)") # creating the link
st.markdown("![baby deol](2a27c0bda2.jpg)")


