from flask import render_template, request, url_for, redirect
from app.main import bp
from app.extensions import db
from app.models.book import Book
from app.models.author import Author
from app.main.forms import BookForm

@bp.route('/', methods=["GET", "POST"])
def index():  
    
    authors = Author.query.all()
    books = Book.query.all()
    form = BookForm()

    if request.method == 'POST':
      
        new_book = Book(title=request.form['title'],  
            description=request.form['description'], 
            number_of_pages=request.form['number_of_pages'],
            read=form.read.data,
            borrowed=form.borrowed.data
            )
        
        for author in authors:
            if author.name == request.form['author']:
                author_object = author    
            else:
                author_object = Author(name=request.form['author'])    
        
        db.session.add(new_book)
        new_book.authors.append(author_object)
        db.session.commit()
        return redirect(url_for('main.index'))



    return render_template('books.html', form = form, books = books)


