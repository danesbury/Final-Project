from flask import Flask, redirect, render_template, request, url_for, jsonify
from cs50 import SQL
import urllib.request, json
from flask_jsglue import JSGlue

#configure application

app = Flask(__name__)
JSGlue(app)

db = SQL("sqlite:///finalproject.db")

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/lookup")
def lookup():
    team = request.args.get("team")
    row = db.execute("SELECT * FROM PREMTABLE WHERE team_name = :team", team=team)
    
    return jsonify(row)
    
def renderTable(team):
    with urllib.request.urlopen("http://www.football-data.org/v1/competitions/426/leagueTable") as url:
        data = json.loads(url.read().decode())
        for item in data:
            if item["teamName"]==team:
                data = team
                break
            else:
                data = {}
    