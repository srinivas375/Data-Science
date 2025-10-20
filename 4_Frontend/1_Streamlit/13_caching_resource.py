import streamlit as st
import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
import time

@st.cache_resource
def load_model():
    # Training time (only first run matters)
    X, y = datasets.load_iris(return_X_y=True)
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model

button = st.button("Load the model")
if button:
    start = time.time()
    model = load_model()
    end = time.time()

    st.success("Model is cached and reused!")
    st.write(f"Time spent on this call: **{end - start:.4f} s**")
