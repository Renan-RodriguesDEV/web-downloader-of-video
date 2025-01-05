import os
from src.downloader import PATH_DOWNLOADS, converter_para_mp3
import streamlit as st

st.title("Convert MP4 (Video) to MP3 (Music/Audio)")
file = st.file_uploader("Insert MP4 file", type=[".mp4"])
if file:
    bytes_file = file.read()

if st.button("Convert"):
    result = False
    if os.path.exists(f"{PATH_DOWNLOADS}/converter.mp4"):
        os.remove(f"{PATH_DOWNLOADS}/converter.mp4")
    if os.path.exists(f"{PATH_DOWNLOADS}/converter.mp3"):
        os.remove(f"{PATH_DOWNLOADS}/converter.mp3")

    with open(f"{PATH_DOWNLOADS}/converter.mp4", "wb") as f:
        f.write(bytes_file)

    result = converter_para_mp3(f"converter.mp4")

    if result:
        st.success("File converted successfully!")
        with open(f"{PATH_DOWNLOADS}/converter.mp3", "rb") as file_download:
            st.download_button(
                "Download", data=file_download.read(), file_name="converted.mp3"
            )
    else:
        st.error("An error occurred while converting the file.")
