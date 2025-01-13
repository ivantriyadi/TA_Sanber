import streamlit as st
import pandas as pd

st.markdown(
    """
    Judul:
Sentiment analysis optimisme terhadap Tahun Baru 2025

Ringkasan:
Saya akan membuat interface streamlit yang dapat menampilkan hasil sentiment analysis terhadap bagaimana kecenderungn optimisme netizen twitter menghadapi tahun 2025.
Data diambil berupa tweet bertagar #tahunbaru2025 menggunakan metode scraping manual dari web X, untuk menghindari penggunaan API yang berbayar.

Latar Belakang:
Tahun 2024 dengan segala pencapaian dan kegagalannya telah berlalu dan membuka lembaran baru 2025. Kondisi sosial politik di akhir tahun 2024 pun tampak naik turun.
Tugas akhir ini dibuat untuk mengetahui kecenderungn optimisme netizen twitter menghadapi tahun 2025.

Tujuan:
1.	Mengetahui sentimen netizen indonesia dalam menghadapi tahun 2025
2.	Mengaplikasikan ilmu yang dipelajari selama training menjadi sebuah produk data science.

Metodologi:
1.	Pengambilan dataset dilakukan manual melalui chrome.
2.	Melakukan pembersihan dataset menggunakan library Sastrawi, agar stemming lebih akurat -> pada file Dataset_cleaning.ipynb
3.	Melakukan terjemahan bahasa Indonesia ke Inggris dalam pengolahan sentimen analysis menggunakan library NLTK -> pada file Dataset_processing.ipynb
4.	Visualisasi presentase sentimen keberpihakan (positif, negative dan netral), akurasi model, dan cloud of words.
5.	Data, pengolahan dan visualisasi ditampilkan melalui interface Streamlit

Algoritma dan Model:
Bahasa: Python 3.13.1

Library :
Sastrawi untuk tahap pembersihan kata sampai stemming
NLTK untuk menghasilkan output sentimen analysis dengan akurasi tinggi.
Google translate untuk menterjemahkan kata
Regex untuk proses pembersihan string dari hyperlink, angka, tanda baca dan lainnya.
Pandas untuk pengolahan dataset
Matplotly untuk menampilkan visualisasi data dalam grafik
    """
)

#st.download_button('Download CSV', text_contents, 'text/csv')

with open('Raw_tweet.csv') as f:
   st.download_button('Download CSV', f)
