import streamlit as st
import pandas as pd

st.title("BIODATA DAN PENDIDIKAN")
st.header("IVAN TRIYADI")

st.image("assets/cv_header.jpg")

col_1, col_2 = st.columns([1,2])

with col_1:
    st.subheader("Biodata")
    st.text("Nama:Ivan Triyadi")
    st.text("Tempat lahir: Bandung")
    st.text("Tanggal lahir: 15 Februari 1989")
    st.text("Jenis kelamin: Laki-laki")

    st.subheader("Alamat")
    st.text("Jalan Serua Residence, Depok")

with col_2:
    st.subheader("Kegiatan")
    st.text("Fulltime: bekerja di General Electric")
    st.text("Course Data Science di Sanbercode")

    st.subheader("Kontak")
    st.text("Phone: +628111588698")
    st.text("Instagram: ivantriyadi")

st.header("PENDIDIKAN FORMAL")
st.text("Sekolah Menengah Pertama Negeri 2 Bandung, 2001-2004")
st.text("Sekolah Menengah Atas Negeri 3 Bandung, 2004-2007")
st.text("Institut Teknologi Bandung, Jurusan Elektro, 2007-2011")
