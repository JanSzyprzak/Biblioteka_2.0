from app.extensions import db
from app.models.tables import book_author 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    description = db.Column(db.String(250), index=True)
    number_of_pages = db.Column(db.Integer, index=True) 
    read = db.Column(db.Boolean)
    borrowed = db.Column(db.Boolean) 
    authors = db.relationship('Author', secondary=book_author, backref='books')
    

    def __str__(self):
       return f"<Title: {self.title}, Author: {self.author}>"