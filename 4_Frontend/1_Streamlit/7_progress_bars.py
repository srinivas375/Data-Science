# this file contains streamlit code for prgoress bar

import streamlit as st
import time as ts


st.write("### Progress bar")
bar = st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    ts.sleep(1)

