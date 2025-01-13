import streamlit as st
import pandas as pd

st.subheader("Proses pembersihan dataset")
st.markdown(
    """
Raw tweet dalam dataset pandas
    """
)
#st.image("assets/gambarnya.jpg")

data=pd.read_csv('assets/Raw_tweet.csv')
st.dataframe(data)

proses_names = ['Memasukkan Library','Data Understanding','Text Preprocessing','Tokenization']
proses = st.radio('Pilih Proses', proses_names)

if proses == 'Memasukkan Library':
    st.write('proses library')
    st.image("assets/1-library.jpg")

elif proses == 'Data Understanding':
    st.write('proses data understanding')
    st.image("assets/1-understanding.jpg")

elif proses == 'Text Preprocessing':
    st.write('proses test preprocessing')
    st.image("assets/1-preprocessing.jpg")

elif proses == 'Tokenization':
    st.write('proses tokenization')
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

