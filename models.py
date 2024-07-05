from flask_sqlalchemy import SQLAlchemy

"""Models for Cupcake app."""

db = SQLAlchemy()

class Cupcake(db.Model):
    """Cupcake Api Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                     nullable=False)
    rating = db.Column(db.Float, 
                       nullable=False)
    image = db.Column(db.Text, 
                      nullable=False,
                      default="https://tinyurl.com/demo-cupcake")
    

    def __repr__(self):
        return f"< {self.id}, {self.flavor}, {self.size}, rating, {self.rating} >"
    
    def serialize(self):
        return {
            'id' : self.id,
            'flavor' : self.flavor, 
            'rating' : self.rating, 
            'size' : self.size, 
            'image' : self.image
        }


def connectdb(app):
    """Connect the database to our Flask app."""
    db.app = app
    db.init_app(app)