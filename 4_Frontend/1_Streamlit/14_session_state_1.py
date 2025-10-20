import streamlit as st

# without session state
# counter = 0

# counter += 1

# st.header(f"This page has run {counter} times")
# st.button("Run it again")


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times")
st.button("Run page again")