from flask import render_template, request, url_for, redirect
from flask import render_template
from sqlalchemy import update
from app.book import bp
from app.models.book import Book
from app.models.author import Author
from app.main.forms import BookForm
from app.extensions import db




@bp.route('<int:book_id>/', methods=["GET", "POST"])
def book_details(book_id):
    #authors = Author.query.all()

    book_to_update = Book.query.get(book_id)
    
    
    form = BookForm()
    form.title.data = book_to_update.title
    form.author.data = [author.name for author in book_to_update.authors] 
    form.description.data = book_to_update.description
    form.number_of_pages.data = book_to_update.number_of_pages
    form.read.data = book_to_update.read
    form.borrowed.data = book_to_update.borrowed

    if request.method == 'POST':
        title=request.form['title']     
        author=request.form['author'] 
        description=request.form['description']
        number_of_pages=request.form['number_of_pages']
        read=form.read.data
        borrowed=form.borrowed.data

        book_to_update.title = title
        book_to_update.description = description
        book_to_update.number_of_pages = number_of_pages
        book_to_update.read = read
        book_to_update.borrowed = borrowed
                
        author_object = Author(name=author) 
     
        
        db.session.add(book_to_update)
        for author in book_to_update.authors:
            book_to_update.authors.remove(author)
        book_to_update.authors.append(author_object)
        db.session.commit()



        return redirect(url_for('main.index'))



    return render_template('book/book.html', form=form, book_id=book_id)




