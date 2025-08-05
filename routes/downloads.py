from io import BytesIO

from flask import Blueprint, request, send_file

from src.downloader import download

route = Blueprint("downloads", __name__)


@route.route("/downloads", methods=["POST"])
def downloads():
    url = request.form.get("url")
    try:
        music_data = download(url)
        # converte o áudio para o formato desejado
        music_file = BytesIO(music_data)
        return send_file(
            music_file,
            as_attachment=True,
            download_name="audio.mp3",
            mimetype="audio/mpeg",
        )
    except Exception as e:
        return {"error": str(e)}, 400
