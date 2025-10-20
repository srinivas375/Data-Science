import streamlit as st
import plotly.express as px

df = px.data.iris()

fig = px.scatter(
    df, x="sepal_width", y = "sepal_length",
    color = "species", size = "petal_length",
    title="Iris data scatter plot"
)
st.plotly_chart(fig, use_container_width=True)