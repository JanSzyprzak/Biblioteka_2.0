from flask import render_template, request, url_for, redirect
from flask import render_template
from sqlalchemy import update
from app.book import bp
from app.models.book import Book
from app.main.forms import BookForm
from app.extensions import db


@bp.route('<int:book_id>/', methods=["GET", "POST"])
def book_details(book_id):
    book_to_update = Book.query.get(book_id+1)
    form = BookForm()
    if request.method == 'POST':
        title=request.form['title'] 
        author=request.form['author'] 
        description=request.form['description']
        number_of_pages=request.form['number_of_pages']
        read=form.read.data
        borrowed=form.borrowed.data

        book_to_update.title = title
        book_to_update.author = author
        book_to_update.description = description
        book_to_update.number_of_pages = number_of_pages
        book_to_update.read = read
        book_to_update.borrowed = borrowed

        db.session.add(book_to_update)
        db.session.commit()




        return redirect(url_for('main.index'))



    return render_template('book/book.html', form=form, book_id=book_id)






"""
Book(
            title=request.form['title'], 
            author=request.form['author'], 
            description=request.form['description'], 
            number_of_pages=request.form['number_of_pages'],
            read=form.read.data,
            borrowed=form.borrowed.data
            )
        db.session.delete(book_to_update)
        db.session.add(book_to_update)
        db.session.commit()
        return redirect(url_for('main.index'))
"""






"""
@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)
###"""


"""
for i in books:
        if i.id == 'book_id':
            book = i
"""