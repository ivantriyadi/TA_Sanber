import streamlit as st

st.subheader("Kesimpulan")

st.markdown(
    """
Dari hasil analisis sentimen dan visualisasi diperolah diagram pie-chart sebagai berikut. Terlihat bahwa mayoritas (83%) sample
tweet bersentimen positif dalam menghadapi tahun 2025. Sebanyak 11% sample bersentimen negatif. Dan 6% sample bersentimen netral.
Sentimen netral ini hampir semuanya adalah tweet promosi yang memanfaatkan event tahun baru untuk menarik perhatian customer.
    """
)
st.image("assets/2-pie.jpg")

st.markdown(
    """
Dari hasil analisis sentimen dan visualisasi diperolah wordcloud sentimen negatif sebagai berikut.
    """
)
st.image("assets/2-negatif.jpg")

st.markdown(
    """
Dari hasil analisis sentimen dan visualisasi diperolah wordcloud sentimen positif sebagai berikut.
    """
)
st.image("assets/2-positif.jpg")
