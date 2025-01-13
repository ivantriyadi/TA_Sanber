import streamlit as st
import pandas as pd

st.subheader("Proses pembersihan dataset")

#st.image("assets/gambarnya.jpg")

st.markdown(
    """
Tulis di sini
    """
)

with open('assets/Clean_tweet.csv') as f:
    st.download_button(
        label="Download Raw Tweet",
        data=f,
        file_name="Clean_tweet.csv",
        mime="text/csv",
        icon=":material/download_for_offline:"
    )
