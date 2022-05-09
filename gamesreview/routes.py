from flask import render_template
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
    def register():
     if request.method == "POST":
        # check if username already exists in db
        existing_user = gamesreview.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        gamesreview.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
     return render_template("register.html")

                     
 
    return render_template("register.html")