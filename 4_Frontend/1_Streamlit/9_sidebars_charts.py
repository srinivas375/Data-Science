# This file contains side bar and charts display code

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# sidebar
st.sidebar.write("This is my sidebar")
x = np.linspace(0, 100, 10000)
y = x**3
fig = plt.figure(figsize=(6,2))
plt.plot(x, np.sin(x))
st.write(fig)