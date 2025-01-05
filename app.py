import os
import time
import streamlit as st
from src.downloader import PATH_DOWNLOADS, baixar_com_ytdlp

st.set_page_config(initial_sidebar_state="collapsed")
for f in os.listdir(PATH_DOWNLOADS):
    os.remove(f"{PATH_DOWNLOADS}/{f}")
    print("[INFO] pasta de downloas limpa!! [INFO]")
st.title("Pagina para dowloads de videos via link(s)!!!")
url_video = st.text_input(
    "insira a URL referente ao video", placeholder="http://www.youtube.com/watch"
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
                while cont <= 120:
                    if download:
                        break
                    placeholder.warning(
                        f"Tempo de download disponível: {120-cont} segundos"
                    )
                    cont += 1
                    time.sleep(1)
            # os.remove(f"{PATH_DOWNLOADS}/{arq}")
            st.subheader("Tempo esgotado, forneca a url novamente")
            time.sleep(5)
            st.rerun()
    else:
        st.error("Ocorreu um erro ao baixar o video.")
