from flask import flash, render_template, request, redirect, session, url_for
from gamesreview import app, db
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