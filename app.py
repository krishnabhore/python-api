from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home PAge</h1>"

import controller.controller_route