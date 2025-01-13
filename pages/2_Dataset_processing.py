import streamlit as st
import pandas as pd

st.subheader("Proses Sentiment Analysis Dataset")
st.write('Clean tweet dalam dataset pandas')

data=pd.read_csv('assets/Clean_tweet.csv')
st.dataframe(data)

proses_names = ['Memasukkan Library','Penerjemahan','Sentiment Analysis NLTK','Data Visualisasi']
proses = st.radio('Pilih Proses', proses_names)

if proses == 'Memasukkan Library':
    st.markdown(
        """
        proses library
        """)
    
elif proses == 'Penerjemahan':
    st.markdown(
        """
        proses penerjemahan
        """)
    
elif proses == 'Sentiment Analysis NLTK':
    st.markdown(
        """
        proses analysis
        """)
    
elif proses == 'Data Visualisasi':
    st.markdown(
        """
        proses visualisasi data
        """)
    
else:
    st.write('proses lain')
