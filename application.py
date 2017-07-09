from flask import Flask, redirect, render_template, request, url_for

#configure application

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")