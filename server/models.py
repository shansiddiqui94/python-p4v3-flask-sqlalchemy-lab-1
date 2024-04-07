from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
# model: a blueprint of a class that represents the structure of the data you want to store and organize your data

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

#repr helps to return a string representation of the object.

def __repr__(self):
    return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

