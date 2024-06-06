from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    return render_template("index3.html")


@app.route("/person/")
def person():
    return render_template("index4.html")


if __name__ == "__main__":
    app.run()