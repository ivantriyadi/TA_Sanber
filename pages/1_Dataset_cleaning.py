import streamlit as st
import pandas as pd

st.subheader("Proses Pembersihan Dataset")
st.write('Raw tweet dalam dataset pandas')
#st.image("assets/gambarnya.jpg")

data=pd.read_csv('assets/Raw_tweet.csv')
st.dataframe(data)

proses_names = ['Persiapkan Library','Data Understanding','Text Preprocessing','Tokenization']
proses = st.radio('Pilih Proses', proses_names)
st.write('-----------------------------------------------------------------------------------------------------')

if proses == 'Persiapkan Library':
    st.subheader('Proses mempersiapkan library')
    st.markdown(
        """
    Pada proses ini, dilakukan instalasi library yang dibutuhkan, diantaranya Pandas untuk memproses dataset,
        """
    )
    st.image("assets/1-library.jpg")

elif proses == 'Data Understanding':
    st.subheader('Proses data understanding')
    st.markdown(
        """
    Pada proses ini, tweets yang sudah dimasukkan ke dalam dataset pandas diperiksa tipe dan jumlah datanya, periksa apakah
    ada baris kosong dan duplikat. Diketahui terdapat 100 tweets, tidak terdapat baris kosong pada kolom Tweet dan tidak terdapat tweet duplikat.
        """
    )
    st.image("assets/1-understanding.jpg")

elif proses == 'Text Preprocessing':
    st.subheader('Proses text preprocessing')
    st.markdown(
        """
    Pada proses ini, tweets yang sudah dimasukkan ke dalam dataset pandas diolah menggunakan proses yaitu pengambilan fitur penting,
    normaliasi kata non-formal, penghilangan stopwords (angka, tanda baca, hyperlink, dan emoticon).
        """
    )
    st.image("assets/1-preprocessing.jpg")

elif proses == 'Tokenization':
    st.subheader('Proses tokenization dan stemming')
    st.markdown(
        """
    Pada proses ini, string pada tiap tweet dipecah menjadi token, lalu dicari akar katanya (stemming) menggunakan library Sastrawi agar lebih
    akurat terhadap tweet yang berbahasa indonesia. Script akan menghasilkan file csv berupa Tweet yang sudah siap untuk dilakukan analisis sentimen.
        """
    )
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

