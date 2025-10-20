# This file contains framents code of streamlit

"""
- st.fragment
    A decorator to turn a function into a fragment to rerun independently of the full app.
"""

import streamlit as st

if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

@st.fragment
def my_fragement():
    st.session_state.fragment_runs += 1
    st.button("Rerun fragement")
    st.write(f"Fragment part says, it ran {st.session_state.fragment_runs} times")

st.session_state.app_runs += 1
my_fragement()
st.button("Rerun full app")
st.write(f"Full app says, it ran {st.session_state.app_runs} times")
st.write(f"Full app says, fragment ran {st.session_state.fragment_runs} times")