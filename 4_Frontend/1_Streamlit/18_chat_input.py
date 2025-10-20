import streamlit as st

prompt = st.chat_input(
    "Enter some text, can also add image",
    accept_file=True,
    file_type=["jpg", 'png', 'jpeg'],
)

if prompt and prompt.text:
    st.markdown(f"User says: {prompt.text}")
if prompt and prompt.files:
    st.image(prompt.files[0])