from flask import render_template, request, url_for, redirect
from app.main import bp
from app.extensions import db
from app.models.book import Book
from app.main.forms import BookForm

@bp.route('/', methods=["GET", "POST"])
def index():  
    
    books = Book.query.all()
    form = BookForm()

    if request.method == 'POST':
      
        new_book = Book(title=request.form['title'], 
            author=request.form['author'], 
            description=request.form['description'], 
            number_of_pages=request.form['number_of_pages'],
            read=form.read.data,
            borrowed=form.borrowed.data
            )

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('main.index'))



    return render_template('books.html', form = form, books = books)


