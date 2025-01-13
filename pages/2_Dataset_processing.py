import streamlit as st
import pandas as pd

st.subheader("Proses Sentiment Analysis Dataset")

#st.image("assets/gambarnya.jpg")

st.markdown(
    """
Tulis di sini
    """
)

proses_names = ['Memasukkan Library','Penerjemahan','Sentiment Analysis NLTK','Data Visualisasi']
proses = st.radio('Pilih Proses', proses_names)

if proses == 'Memasukkan Library':
    st.write('proses library')
elif proses == 'Penerjemahan':
    st.write('proses Penerjemahan')
elif proses == 'Sentiment Analysis NLTK':
    st.write('proses Sentiment Analysis NLTK')
elif proses == 'Data Visualisasi':
    st.write('proses Data Visualisasi')
else:
    st.write('proses lain')
