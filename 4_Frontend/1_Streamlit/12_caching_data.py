# caching avoids the streamlit to rerun again, when same operation performed again and again on same data, therefore computation is also saved

# It has two types of decorators
#   @st.cache_data
#   @st.cache_resource

import streamlit as st
import pandas as pd
import numpy as np
import time

@st.cache_data
def load_data(n_rows: int):
    start = time.time()
    time.sleep(3)  
    df = pd.DataFrame(
        np.random.randn(n_rows, 3),
        columns=["A", "B", "C"]
    )
    end = time.time()
    elapsed = end - start
    return df, elapsed

st.title("Cache Demo with Timing")

rows = st.slider("Select number of rows:", 100, 1000, 500, step=100)

df, elapsed = load_data(rows)

st.write(f"Function execution time: **{elapsed:.2f} seconds**")
st.dataframe(df.head())
