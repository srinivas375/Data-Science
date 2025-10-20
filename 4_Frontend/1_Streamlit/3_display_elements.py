import streamlit as st
import pandas as pd


table = pd.DataFrame({"name":["srinu", "nani", "abhai"], "marks": [23, 45, 12]})

#write function - we can display json, code, markdowns,... using 'write' function

# normal text
st.write("This is normal text")

# markdown text
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")
st.write("---")

#json
json_file = {"name":"nani", "mobile": "8097739812"}
st.write(json_file)

#metric
st.metric(label = "wind speed", value="120ms", delta="1.4ms")
st.metric(label = "New wind speed", value="111ms", delta="-1.2ms")

# table
st.table(table)

# dataframe
st.dataframe(table)