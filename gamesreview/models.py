from gamesreview import db 



class Publisher(db.model):
    #schema for Publisher model
    publisher = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.string(30), unique=True, nullable=False)


    def __repr__(self):
        # used to represent itself as form of string

        return self.publisher_name 



class Register(db.model):
     #schema for  publisher model 
     id = db.Column(db.Integer, primary_key=True)
     user_name= db.Column(db.string(30), unique=True, nullable=False)
     


    



class (db.model):
     #schema for login model

