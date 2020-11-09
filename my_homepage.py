from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/projects/fakebook")
def fakebook():
    return render_template("index_fakebook.html")


@app.route("/projects/stran22")
def stran22():
    return render_template("index_stran22.html")


if __name__ == "__main__":
    app.run(debug=True)
