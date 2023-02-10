from app.extensions import db

class Author(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    #title = db.Column(db.String(100), db.ForeignKey("book.title"))
    #books = db.relationship("Book", back_populates="author")

    def __str__(self):
       return f"<Author: {self.name}>"