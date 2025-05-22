import os
import time
import streamlit as st
from src.downloader import PATH_DOWNLOADS, baixar_com_ytdlp

# Limpa todos os arquivos .mp4 da pasta de downloads ao iniciar o app
if os.path.exists(PATH_DOWNLOADS):
    for arq in os.listdir(PATH_DOWNLOADS):
        os.remove(os.path.join(PATH_DOWNLOADS, arq))
        print(f'[INFO] - {time.strftime("%X")} - Removendo arquivo {arq} [INFO]')

st.set_page_config(initial_sidebar_state="collapsed")

st.title("Bem vindo ao Downloader, forneca a url do video!!!")
url_video = st.text_input(
    "insira a URL referente ao video", placeholder="https://www.youtube.com/watch"
)

if st.button("Buscar"):
    if url_video.strip() == "":
        st.error("URL não pode ser vazia")
    else:
        result = baixar_com_ytdlp(url_video)
        if result:
            st.success("Video baixado com sucesso!")
            arquivos = os.listdir(PATH_DOWNLOADS)
            for arq in arquivos:
                if arq.endswith(".mp4"):
                    video_path = f"{PATH_DOWNLOADS}/{arq}"
                    with open(video_path, "rb") as v:
                        video_bytes = v.read()
                        st.video(video_bytes)
                        # Inicializa download como False
                        download = False
                        # Botão de download
                        download = st.download_button(
                            "Baixar video", data=video_bytes, file_name="download.mp4"
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
                    # Agora, fora do bloco with, o arquivo está fechado e pode ser removido
            if not download:
                if os.path.exists(video_path):
                    try:
                        os.remove(video_path)
                        print(
                            f"[INFO] - {time.strftime('%X')} - Removendo arquivo {arq} [INFO]"
                        )
                    except Exception as e:
                        st.warning(
                            f"Não foi possível remover o arquivo {arq}, ele está em uso."
                        )
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
