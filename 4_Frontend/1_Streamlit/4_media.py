# embedding image, audio, video in streamlit

import streamlit as st

#image
st.image('deol.jpg', caption="Baby Deol image")

st.image('deol.jpg', caption="Baby Deol image 2", width=300)

#audio
st.audio("audio.mp3")

#video
st.video("video.mp4")

st.video("video.mp4", width=300)