from flask import flash, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from gamesreview import app, db, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, Flask
from gamesreview.models import Publisher, Game
from flask_pymongo import PyMongo
import os

if os.path.exists('env.py'):
    import env

mongoapp = Flask(__name__)

mongoapp.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
mongoapp.config["MONGO_URI"] = os.getenv('MONGO_URI')

# Redefining from line 3 during testing



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/titles")
def titles():
    game = list(Game.query.order_by(Game.id).all())
    publisher = list(Game.query.order_by(Game.id).all())
    return render_template("titles.html", game=game, publisher=publisher)


@app.route("/publisher")
def publisher():
    publisher = list(Publisher.query.order_by(Publisher.publisher_name).all())
    return render_template("publisher.html", publisher=publisher)

@app.route("/add_publisher", methods=["GET", "POST"])
def add_publisher():
    if request.method == "POST":
        publisher = Publisher(publisher_name=request.form.get("publisher_name"))
        db.session.add(publisher)
        db.session.commit()
        return redirect(url_for("publisher"))
    return render_template("add_publisher.html")


@app.route("/edit_publisher/<int:publisher_id>", methods=["GET", "POST"])
def edit_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    if request.method == "POST":
         publisher.publisher_name = request.form.get("publisher_name")
         db.session.commit()
         return redirect(url_for("publisher"))
    return render_template("edit_publisher.html", publisher=publisher)

@app.route("/delete_publisher/<int:publisher_id>")
def delete_publisher(publisher_id):
     publisher = Publisher.query.get_or_404(publisher_id)
     db.session.delete(publisher)
     db.session.commit()
     return redirect(url_for("publisher"))

@app.route("/")
def game():
    game = list(Game.query.order_by(Game.id).all())
    return render_template("titles.html", game=game)

@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    publisher = list(Publisher.query.order_by(
    Publisher.publisher_name).all())
    if request.method == "POST":
        game = Game(

            game_name=request.form.get("game_name"),
            publisher_id=request.form.get("publisher_id")
        )
        db.session.add(game)
        db.session.commit()
        return redirect(url_for("titles"))
    return render_template("add_game.html", publisher=publisher)

@app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    game = Game.query.get_or_404(game_id)
    if request.method == "POST":
        game.game_name = request.form.get("game_name"),
        publisher_id=request.form.get("publisher_id")
        db.session.commit()
        return redirect(url_for("titles"))
    return render_template("edit_game.html", game=game, publisher=publisher)

@app.route("/delete_game/<int:game_id>")
def delete_game(game_id):
     game = Game.query.get_or_404(game_id)
     db.session.delete(game)
     db.session.commit()
     return redirect(url_for("titles"))
    

@app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(
        Review.game_review).all())
    return render_template("reviews.html", reviews=reviews)

@app.route("/add_reviews", methods=["GET", "POST"])
def add_reviews():
    reviews = list(Review.query.order_by(
        Review.game_review).all())
    if request.method == "POST":
        reviews = Reviews(
            game_review.form.get("game_review"),
            game_rating.form.get("game_rating"),
            game_genre.form.get("game_genre"),
            game_id=request.form.get("game_id")

        )
        db.session.add(reviews)
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("add_reviews.html", reviews=reviews, game=game)






    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)