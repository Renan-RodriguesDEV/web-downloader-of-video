from io import BytesIO

from flask import Blueprint, render_template, request, send_file, make_response

from src.downloader import download

route = Blueprint("downloads", __name__)


@route.route("/downloads", methods=["POST"])
def downloads():
    url = request.form.get("url")
    filename = request.form.get("filename")
    try:
        music_data = download(url)
        if not music_data or len(music_data) == 0:
            raise Exception("No data received from download")
        # converte o áudio para o formato desejado
        music_file = BytesIO(music_data)
        music_file.seek(0)
        content_length = music_file.getbuffer().nbytes
        print(f"File converted to BytesIO: {content_length} bytes")
        print(f"Downloading audio from {url} as {filename}.mp3")
        response = make_response(send_file(
            music_file,
            as_attachment=True,
            download_name=f"{filename}.mp3",
            mimetype="audio/mpeg",
        ))
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}.mp3"'
        response.headers['Content-Length'] = str(content_length)
        return response
    except Exception as e:
        return render_template("error.html", error_message=str(e))
