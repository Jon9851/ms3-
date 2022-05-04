from gamesreview import db 



class Publisher(db.model):
    #schema for Publisher model
    id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.string(30), unique=True, nullable=False)
    blizzard_activision = db.Column(db.string(0), unique=True, nullable=False)


    def __repr__(self):
        # used to represent itself as form of string

        return self.publisher_name 



class Id(db.model):
     #schema for id model
     id = db.Column(db.Integer, primary_key=True)
     id_number= db.Column(db.string(30), unique=True, nullable=False)
     blizzard_activision = db.Column(db.string(0), unique=True, nullable=False)



class Login(db.model):
     #schema for login model


class Admin(db.model):
      #schema for admin model