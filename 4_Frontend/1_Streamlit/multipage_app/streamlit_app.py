# run this page -> This is the starting point of execution for multipage app

import streamlit as st

main_page = st.Page("main_page.py", title="Main Page")
page_2 = st.Page("page_2.py", title="Page 2")
page_3 = st.Page("page_3.py", title="Page 3")

pg = st.navigation([main_page, page_2, page_3])

pg.run()
