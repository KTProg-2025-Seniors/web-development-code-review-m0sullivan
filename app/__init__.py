from flask import Flask

from flask_svelte import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="Flask Svelte")

@app.route("/newsletter")
def newsletter():
    return render_template("newsletter.html", name="Flask Svelte")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)