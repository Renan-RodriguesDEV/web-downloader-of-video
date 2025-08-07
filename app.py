from flask import Flask, render_template
from flask_cors import CORS

from routes.downloads import route as downloads_route

app = Flask(__name__)
CORS(app)
app.register_blueprint(downloads_route)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
