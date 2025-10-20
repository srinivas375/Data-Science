import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


opt = st.sidebar.radio("Select any Graph", options=("Line chart", "Bar chart", "Pie chart", "map"))

if opt == "Line chart":
    x = np.linspace(0, 50, 10000)
    fig = plt.figure(figsize=(8,2))
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.grid()
    st.pyplot(fig)

elif opt == "Bar chart":
    categories = ["A", "B", "C", "D", "E"]
    values = np.random.randint(1, 10, size=5)
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(categories, values, color="skyblue")
    ax.set_title("Random Bar Chart")
    st.pyplot(fig)

elif opt == "Pie chart":
    labels = ["Apples", "Bananas", "Cherries", "Dates"]
    sizes = [15, 30, 45, 10]
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Fruit Distribution")
    st.pyplot(fig)

elif opt == "map":
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        np.random.randn(100, 2)/[50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )
    st.map(df)