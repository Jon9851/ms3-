from flask import render_template, request, redirect, url_for
from gamesreview import app, db
from flask import session
from gamesreview.models import Publisher, Title, User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/titles")
def titles():
    return render_template("titles.html")

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


@app.route("/add_titles", methods=["GET", "POST"])
def add_titles():
    publisher = list(Publisher.query.order_by(Publisher.publisher_name).all())
    if request.method == "POST":
        titles = Titles(
            titles_name=request.form.get("titles_name"),
            publisher_id=request.form.get("publisher_id")
        )
        db.session.add(titles)
        db.session.commit()
        return redirect(url_for("publisher"))
    return render_template("add_titles.html", publisher=publisher)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    if "User" in session:
        # user logged in 
    

        login = User.query.filter_by(username=username)
        if login is not None:
            return redirect(url_for("register"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        register = User(username=username, password=password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


    if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)