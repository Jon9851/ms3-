from gamesreviewbeta import db


class Publisher(db.Model):
    # schema for Publisher model
    id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.String(30), unique=True, nullable=False)
    game = db.relationship(
        "Game", backref="Publisher", cascade="all, delete", lazy=True
    )

    def __repr__(self):

        return self.publisher_name


class Game(db.Model):
    # schema for  games model
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(30), unique=True, nullable=True)
    publisher_id = db.Column(
        db.Integer, db.ForeignKey("publisher.id", ondelete="CASCADE"), nullable=False
    )

class Reviews(db.Model):
    # schema for  games model
    id = db.Column(db.Integer, primary_key=True)
    game_review = db.Column(db.String(300), unique=True, nullable=True)
    game_rating = db.Column(db.String(30), unique=True, nullable=True)
    game_genre = db.Column(db.String(30), unique=True, nullable=True)
    game_id = db.Column(
        db.Integer, db.ForeignKey("publisher.id", ondelete="CASCADE"), nullable=False)
    
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string]
        return "#{0} - Games Name: {1} | Game Review: {2}".format(
            self.id, self.game_name, self.game_review
        )