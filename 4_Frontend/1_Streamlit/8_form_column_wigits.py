import streamlit as st

# form wigit in streamlit
st.markdown("<h1 style = 'text-alighn: center;'>User Registration</h1>", unsafe_allow_html=True)
st.write("### Form - 1")
form = st.form("Form_1")
form.text_input("Enter First name")
form.form_submit_button("Submit")


st.write("### Form - 2")
with st.form("form_2"):
    st.text_input("First Name")
    st.text_input("Last Name")
    st.form_submit_button("Submit")

st.write("### Form - 3")
with st.form("form_3", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    st.text_input("Email address")
    st.text_input("Password")
    st.text_input("conform passroed")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state = st.form_submit_button("Submit")

    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill above fields")
        else:
            st.success("Submitted Successfully")
