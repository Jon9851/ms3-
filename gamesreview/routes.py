from flask import flask, render_template
from gamesreview import app, db
from gamesreview.models import Publisher, Title
from werkzeug.security import generate_password_hash, check_password_hash



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login ():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")