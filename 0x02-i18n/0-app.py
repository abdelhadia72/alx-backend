#!/usr/bin/env python3
from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def hello():
    return send_file("templates/0-index.html")


if __name__ == "__main__":
    app.run(port=5000)
