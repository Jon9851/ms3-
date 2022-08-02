from flask import flash, render_template, request, session, redirect, url_for
from functools import wraps
from bson.objectid import ObjectId
from gamesreviewc import app, db, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, Flask
from werkzeug.exceptions import HTTPException
from gamesreviewc.models import Publisher, Game, Reviews
from flask_pymongo import PyMongo
import os

if os.path.exists("env.py"):
    import env

mongoapp = Flask(__name__)

mongoapp.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
mongoapp.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Redefining from line 3 during testing


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# User name routes
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if username already exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Succesfull")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


def login_required(f):
    # ensures page is only viewable to logged in users
    # https://flask.palletsprojects.com/ helped me achieve this
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to be logged in to view this page")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/titles")
@login_required
def titles():
    game = list(Game.query.order_by(Game.id).all())
    publisher = list(Publisher.query.order_by(Publisher.id).all())
    return render_template("titles.html", game=game, publisher=publisher)


@app.route("/publisher")
@login_required
def publisher():
    publisher = list(Publisher.query.order_by(Publisher.publisher_name).all())
    return render_template("publisher.html", publisher=publisher)


@app.route("/add_publisher", methods=["GET", "POST"])
@login_required
def add_publisher():
    if request.method == "POST":
        publisher = Publisher(
            publisher_name=request.form.get("publisher_name"))
        db.session.add(publisher)
        db.session.commit()
        return redirect(url_for("publisher"))
    return render_template("add_publisher.html")


@app.route("/edit_publisher/<int:publisher_id>", methods=["GET", "POST"])
@login_required
def edit_publisher(publisher_id):

    publisher = Publisher.query.get_or_404(publisher_id)
    if request.method == "POST":
        publisher.publisher_name = request.form.get("publisher_name")
        db.session.commit()
        return redirect(url_for("publisher"))
    return render_template("edit_publisher.html", publisher=publisher)


@app.route("/delete_publisher/<int:publisher_id>")
@login_required
def delete_publisher(publisher_id):

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to delete publishers!")
        return redirect(url_for("publisher"))

    publisher = Publisher.query.get_or_404(publisher_id)
    db.session.delete(publisher)
    db.session.commit()
    return redirect(url_for("publisher"))


@app.route("/add_game", methods=["GET", "POST"])
@login_required
def add_game():
    publisher = list(Publisher.query.order_by(Publisher.publisher_name).all())
    if request.method == "POST":
        game = Game(
            game_name=request.form.get("game_name"),
            publisher_id=request.form.get("publisher_id"),
        )
        db.session.add(game)
        db.session.commit()
        return redirect(url_for("titles"))
    return render_template("add_game.html", publisher=publisher)


@app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
@login_required
def edit_game(game_id):
    game = Game.query.get_or_404(game_id)
    if request.method == "POST":
        game.game_name = (request.form.get("game_name"),)
        publisher_id = request.form.get("publisher_id")
        db.session.commit()
        return redirect(url_for("titles"))
    return render_template("edit_game.html", game=game, publisher=publisher)


@app.route("/delete_game/<int:game_id>")
@login_required
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for("titles"))


@app.route("/reviews")
@login_required
def reviews():
    reviews = list(Reviews.query.order_by(Reviews.id).all())
    print("reviews:", reviews)
    game = list(Game.query.order_by(Game.id).all())
    return render_template("reviews.html", reviews=reviews, game=game)


@app.route("/add_reviews", methods=["GET", "POST"])
@login_required
def add_reviews():
    game = list(Game.query.order_by(Game.game_name).all())
    if request.method == "POST":
        reviews = Reviews(
            game_review=request.form.get("game_review"),
            game_rating=request.form.get("game_rating"),
            game_genre=request.form.get("game_genre"),
            game_id=request.form.get("game_id"),
        )
        db.session.add(reviews)
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("add_reviews.html", game=game)


@app.route("/edit_reviews/<int:reviews_id>", methods=["GET", "POST"])
@login_required
def edit_reviews(reviews_id):
    reviews = Reviews.query.get_or_404(reviews_id)
    game = list(Game.query.order_by(Game.game_name).all())
    if request.method == "POST":
        reviews.game_review = (request.form.get("game_review"),)
        reviews.game_rating = (request.form.get("game_rating"),)
        reviews.game_genre = (request.form.get("game_genre"),)
        game_id = request.form.get("game_id")
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("edit_reviews.html", reviews=reviews, game=game)


@app.route("/delete_reviews/<int:reviews_id>")
@login_required
def delete_reviews(reviews_id):
    reviews = Reviews.query.get_or_404(reviews_id)
    db.session.delete(reviews)
    db.session.commit()
    return redirect(url_for("reviews"))


"""
    All error handlers were implemented with help from
    https://flask.palletsprojects.com/
"""


@app.errorhandler(500)
def internal_server_error(e):
    """
        handles a 400 Bad Request error
        and returns an error message to the user
    """
    return render_template('error.html'), 500


@app.errorhandler(400)
def handle_bad_request(e):
    """
        handles a 400 Bad Request error
        and returns an error message to the user
    """
    return render_template("error.html", error_status=e), 400


@app.errorhandler(404)
def page_not_found(e):
    """
        handles a 404 Not Found error
        and returns an error message to the user
    """
    return render_template("error.html", error_status=e), 404