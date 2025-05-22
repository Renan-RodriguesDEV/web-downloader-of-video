import os
from src.downloader import PATH_DOWNLOADS, converter_para_mp3
import streamlit as st

st.title("Converter MP4 (Video) para MP3 (Music/Audio)")
file = st.file_uploader("Insert MP4 file", type=[".mp4"])
if file:
    bytes_file = file.read()

if st.button("Converter"):
    result = False
    if os.path.exists(f"{PATH_DOWNLOADS}/converter.mp4"):
        os.remove(f"{PATH_DOWNLOADS}/converter.mp4")
    if os.path.exists(f"{PATH_DOWNLOADS}/converter.mp3"):
        os.remove(f"{PATH_DOWNLOADS}/converter.mp3")

    with open(f"{PATH_DOWNLOADS}/converter.mp4", "wb") as f:
        f.write(bytes_file)

    result = converter_para_mp3(f"converter.mp4")

    if result:
        st.success("Arquivo convertido com sucesso!")
        with open(f"{PATH_DOWNLOADS}/converter.mp3", "rb") as file_download:
            st.download_button(
                "Download", data=file_download.read(), file_name="converted.mp3"
            )
    else:
        st.error("Houve um erro ao converter o arquivo.")

footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    padding: 10px;
    text-align: center;
}
</style>
<div class="footer">
    <p>Segue no insta lá pae <a href="https://www.instagram.com/__little_renan__.py/">@__little_renan__.py</a> 📸<br>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
