import streamlit as st

st.title("Chatbot helper")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter something"):
    st.session_state.messages.append({"role":"user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = f"I received : {prompt}"
    st.session_state.messages.append({"role":"ai", "content":response})
    with st.chat_message("ai"):
        st.markdown(response)