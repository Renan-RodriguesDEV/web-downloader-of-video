# Método 1: usando yt-dlp (Recomendado)
import os
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip

PATH_DOWNLOADS = os.path.join(os.getcwd(), "downloads")


if not os.path.exists(PATH_DOWNLOADS):
    print("[INFO] Downloads not exists, creating folder... [INFO]")
    os.makedirs(PATH_DOWNLOADS)


def baixar_com_ytdlp(url, pasta_destino=PATH_DOWNLOADS):
    """
    Baixa vídeo usando yt-dlp - mais robusto e frequentemente atualizado
    """
    opcoes = {
        "format": "bestvideo+bestaudio/best",  # Melhor qualidade disponível
        "outtmpl": f"{pasta_destino}/%(title)s.%(ext)s",
        "ignoreerrors": True,
        "nocheckcertificate": True,  # Ignorar erros de certificado
    }

    with YoutubeDL(opcoes) as ydl:
        try:
            ydl.download([url])
            return True
        except Exception as e:
            print(f"Erro: {str(e)}")
            return False


def converter_para_mp3(filename_video, base_folder=PATH_DOWNLOADS):
    try:
        audio = VideoFileClip(os.path.join(base_folder, filename_video)).audio
        audio.write_audiofile(f"{base_folder}/{filename_video.replace('.mp4','')}.mp3")
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == "__main__":
    # link = "https://youtu.be/23HFxAPyJ9U?si=Qsb9rxXOFIVaydxl"
    # baixar_com_ytdlp(link)
    for video in os.listdir("downloads"):
        if video.endswith(".mp4"):
            converter_para_mp3(video)
