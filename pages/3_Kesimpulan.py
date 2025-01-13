import streamlit as st

st.subheader("Kesimpulan")

st.markdown(
    """
Dari hasil analisis sentimen dan visualisasi diperoleh diagram pie-chart sebagai berikut. Terlihat bahwa mayoritas (83%) sample
tweet bersentimen positif dalam menghadapi tahun 2025. Sebanyak 6% sample bersentimen negatif. Dan 11% sample bersentimen netral.
Sentimen netral ini hampir semuanya adalah tweet promosi yang memanfaatkan event tahun baru untuk menarik perhatian customer.
    """
)
st.image("assets/2-pie.jpg")

st.markdown(
    """
Dari hasil analisis sentimen dan visualisasi diperoleh wordcloud sentimen negatif sebagai berikut. Kata yang mendominasi berkisar
antara topik sehari-hari seperti tahun baru, finansial, kritik, rumah, dan umur. Beberapa topik viral juga muncul pada visualisasi
ini, misalnya pemecatan pelatih timnas Shin Tae Yong, konflik di Gaza, dan film Ipar adalah maut.
    """
)
st.image("assets/2-negatif.jpg")

st.markdown(
    """
Dari hasil analisis sentimen dan visualisasi diperoleh wordcloud sentimen positif sebagai berikut. Kata yang mendominasi berkisar
antara tahun baru, weekend, libur (cukup banyak tanggal merah di Januari). Perintah kemungkinan hasil stemming dari pemerintah yang
berarti ada sentimen positif terhadap pemerintah memasuki tahun 2025 ini, ditandai juga dengan banyaknya kata presiden "Prabowo".
Terdapat juga kata PLN, yang setelah dianalisis lebih lanjut merupakan tweet terafiliasi PLN.
    """
)
st.image("assets/2-positif.jpg")

st.markdown(
    """
Mari sambut tahun baru 2025 dengan optimisme tinggi! Salam.
    """
)
