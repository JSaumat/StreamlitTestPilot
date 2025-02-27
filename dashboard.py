import streamlit as st
import pandas as pd
import numpy as np

# st.title("This is the title")
#
# st.header("This is the header")
#
# st.subheader("This is the subheader")
# st.write("This is regular text")
#
# """
# # header
# ## subheader
# """
#
# some_dictionary = {
#     "key": "value",
#     "key2": "value2"
# }
#
# some_list = [1, 2 , 3]
# st.write(some_dictionary)
# st.write(some_list)
#
# st.sidebar.title("Options")
#
# df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
#
# st.dataframe(df)
#
# st.image("https://www.nasdaq.com/sites/acquia.prod/files/image/4b6c84393df1ef26f81356305cf5fba0007f8c2b_f9bcaea802f3a0a5afed32f5702d48e7.png")

option = st.sidebar.selectbox(
    "Which dashboard?", ("Twitter", "wallstreetbets", "stocktwits", "chart", "pattern"),
)

st.header(option)

if option == "twitter":
    st.subheader("twitter dashboard logic")

if option == "chart":
    st.subheader("this is the chart dashboard")