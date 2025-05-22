import os
import time
import streamlit as st
from src.downloader import PATH_DOWNLOADS, baixar_com_ytdlp

st.set_page_config(initial_sidebar_state="collapsed")

st.title("Bem vindo ao Downloader, forneca a url do video!!!")
url_video = st.text_input(
    "insira a URL referente ao video", placeholder="https://www.youtube.com/watch"
)
if st.button("Buscar"):
    result = baixar_com_ytdlp(url_video)
    if result:
        st.success("Video baixado com sucesso!")
        arquivos = os.listdir(PATH_DOWNLOADS)
        for arq in arquivos:
            with open(f"{PATH_DOWNLOADS}/{arq}", "rb") as v:
                if arq.endswith(".mp4"):
                    st.video(v.read())
                    download = st.download_button(
                        "Baixar video", data=v.read(), file_name="download.mp4"
                    )
                cont = 0
                placeholder = st.empty()
                while cont <= 300:
                    if download:
                        break
                    placeholder.warning(
                        f"Tempo de download disponível: {300-cont} segundos"
                    )
                    cont += 1
                    time.sleep(1)
            # limpando a pasta de downloads do servidor
            print(f"[INFO] - {time.strftime('%X')} - Removendo arquivo {arq} [INFO]")
            os.remove(f"{PATH_DOWNLOADS}/{arq}")
            st.subheader("Tempo esgotado, forneca a url novamente")
            time.sleep(5)
            st.rerun()
    else:
        st.error("Ocorreu um erro ao baixar o video.")
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
