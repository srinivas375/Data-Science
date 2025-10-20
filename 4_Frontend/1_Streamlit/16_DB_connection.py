# working on db connection in streamlit using st.connectoin

import streamlit as st
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

st.title("MySQL demo with st.connection")

try:
    #creating the connection
    conn = st.connection("my_mysql", type="sql")

    #run a query
    df = conn.query("SELECT * FROM customers;", ttl = 600)

    # displaying the data
    st.subheader("Sample data from MySQL")
    st.dataframe(df)
except SQLAlchemyError as e:
    st.error("Database connection/query failed", e)
except Exception as e:
    st.error("Something error occured", e)