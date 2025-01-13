import streamlit as st
import pandas as pd

st.subheader("Proses pembersihan dataset")

#st.image("assets/gambarnya.jpg")

st.markdown(
    """
Tulis di sini
    """
)

proses_names = ['Memasukkan Library','Data Understanding','Text Preprocessing','Tokenization']
proses = st.radio('Pilih Proses', proses_names)

if proses = 'Memasukkan Library':
    st.write('proses library')
else:
    st.write('proses lain')

with open('assets/Clean_tweet.csv') as f:
    st.download_button(
        label="Download Clean Tweet",
        data=f,
        file_name="Clean_tweet.csv",
        mime="text/csv",
        icon=":material/download_for_offline:"
    )
