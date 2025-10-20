# this file contains interactive elements of streamlit

import streamlit as st

#checkbox
st.write("##checkbox")
st.write("#### Exampl - 1")
state = st.checkbox("Are you agree to the terms and conditions")
if state:
    st.write("Yay!, you agreed")
else:
    st.write("Please agree to the terms, to continue")

# example-2
st.write("#### Example - 2")
apple = st.checkbox("apple")
banana = st.checkbox("banana")
mango = st.checkbox("mango")
st.write("The fruits you selected:")
if apple: st.write("apple")
if banana: st.write("banana")
if mango: st.write("mango")

#exampl3 - 3
st.write("#### Example - 3")
def hello():
    st.write("You, toggled the fucntion")
    st.write(st.session_state.checker)
st.checkbox("Toggle", on_change=hello, key='checker')

# slidebar
st.write("## slidebar")
age = st.slider("choose your age:", 0, 100, 25)
st.write("Your age is :", age)

# select slidebar
rating = st.select_slider(
    "Rate your experience",
    options=["Bad", "Okay", "Good", "Excellent"]
)

st.write("Your rating:", rating)

# button
st.write("## button")
submit = st.button("Submit the form")
if submit:
    st.write("You submitted the form")


# radio button
st.write("## radio button")
radio_btn = st.radio("Which Branch are you studying", options=("CSE", "ECE", "Mech", "Civil"))
if radio_btn:
    st.write(f"You are {radio_btn} student")

# select boxes
st.write("## select box")
select = st.selectbox("Favoriate car", options=("audi", 'bmw', 'ferrari', 'bugatti'))
st.write(f"Your favorite car is {select}")

# multi select box
st.write("## Multi select")
multi_select = st.multiselect("Your Favoriate laptop", options=("Dell", "Apple", "HP", "Asus"))

st.write(f"Your favorite laptops are : {multi_select}")

# text input
st.write("## Text input")
value = st.text_input("enter you name", max_chars=60)
if value:
    st.write(f"Hello {value}, welcome to streamlit")

# text area
text = st.text_area("Describe about ML")
if text:
    st.write("You done very well")

# date input
st.write("## Date input")
birth = st.date_input("Enter your birthdate")
if birth:
    st.write(f"Your bithday is on : {birth}")

# time input
time = st.time_input("Enter your sleeping time")
if time:
    st.write(f"Happy sleep at {time}")

# audio input
st.write("### Audio input")
audio_val = st.audio_input("Record your audio here")
if audio_val:
    st.audio(audio_val)

# camera input
st.write("### Camera input")
enable = st.checkbox("Enable camera input")
picture = st.camera_input("Take a picture", disabled= not enable)

if picture:
    st.image(picture)
