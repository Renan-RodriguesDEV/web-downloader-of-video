from flask import Flask, render_template

from routes.downloads import route as downloads_route

app = Flask(__name__)
app.register_blueprint(downloads_route)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
