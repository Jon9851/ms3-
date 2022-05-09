from gamesreview import db 



class Publisher(db.Model):
    #schema for Publisher model
     id = db.Column(db.Integer, primary_key=True)
     publisher_name = db.Column(db.String(30), unique=True, nullable=False)
     games = db.relationship("Title", backref="Publisher", cascade="all, delete", lazy=True)  

     def __repr__(self):
     

        return self .publisher_name 



class Title(db.Model):
     #schema for  publisher model 
     id = db.Column(db.Integer, primary_key=True)
     title_name = db.Column(db.String(30), unique=True, nullable=False)
     publisher_id = db.Column(db.Integer, db.ForeignKey("publisher.id", ondelete="CASCADE"), nullable=False)
     

class User(db.Model):
     #  Schema for user model
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(30), unique=True, nullable=False)
     password = db.Column(db.Text(), nullable=False)

     def __repr__(self):
        
        return "#{0} - Title Name: {1}".format(
             self.id, self.tile_name
        ) 
