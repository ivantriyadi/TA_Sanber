import streamlit as st
import pandas as pd

st.subheader("Proses pembersihan dataset")
st.write('Raw tweet dalam dataset pandas')
#st.image("assets/gambarnya.jpg")

data=pd.read_csv('assets/Raw_tweet.csv')
st.dataframe(data)

proses_names = ['Persiapkan Library','Data Understanding','Text Preprocessing','Tokenization']
proses = st.radio('Pilih Proses', proses_names)
st.write('-----------------------------------------------------------------------------------------------------')

if proses == 'Persiapkan Library':
    st.write('Proses mempersiapkan library')
    st.image("assets/1-library.jpg")

elif proses == 'Data Understanding':
    st.write('Proses data understanding')
    st.markdown(
        """
    Pada proses ini, tweets yang sudah dimasukkan ke dalam dataset pandas diolah menggunakan proses yaitu pengambilan fitur penting,
    normaliasi kata non-formal, penghilangan stopwords (angka, tanda baca, hyperlink, dan emoticon).
        """
    )
    st.image("assets/1-understanding.jpg")

elif proses == 'Text Preprocessing':
    st.write('Proses test preprocessing')
    st.image("assets/1-preprocessing.jpg")

elif proses == 'Tokenization':
    st.write('Proses tokenization')
    st.image("assets/1-tokenization.jpg")
    with open('assets/Clean_tweet.csv') as f:
        st.download_button(
            label="Download Clean Tweet",
            data=f,
            file_name="Clean_tweet.csv",
            mime="text/csv",
            icon=":material/download_for_offline:"
        )
else:
    st.write('proses lain')

