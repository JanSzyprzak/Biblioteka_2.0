from flask import render_template
from app.authors import bp
from app.models.author import Author

@bp.route('/')
def get_authors():
    authors = Author.query.all()

    return render_template('authors/authors.html', authors=authors)
