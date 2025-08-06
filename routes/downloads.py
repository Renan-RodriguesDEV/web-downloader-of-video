from io import BytesIO

from flask import Blueprint, render_template, request, send_file

from src.downloader import download

route = Blueprint("downloads", __name__)


@route.route("/downloads", methods=["POST"])
def downloads():
    url = request.form.get("url")
    filename = request.form.get("filename")
    try:
        music_data = download(url)
        # converte o áudio para o formato desejado
        music_file = BytesIO(music_data)
        print(f"File converted to BytesIO: {music_file}")
        print(f"Downloading audio from {url} as {filename}.mp3")
        return send_file(
            music_file,
            as_attachment=True,
            download_name=f"{filename}.mp3",
            mimetype="audio/mpeg",
        )
    except Exception as e:
        return render_template("error.html", error_message=str(e))
