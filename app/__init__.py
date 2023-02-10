from flask import Flask
from app.extensions import db
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.book import bp as book_bp
    app.register_blueprint(book_bp, url_prefix='/books')

    from app.authors import bp as authors_bp
    app.register_blueprint(authors_bp, url_prefix='/authors')


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'


    return app