import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("zoK2V-udkUpT_NLhKn.kVko8B")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URl")

db= SQLAlchemy(app)

from gamesreview import routes #noqa
