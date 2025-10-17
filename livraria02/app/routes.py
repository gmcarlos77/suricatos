from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = 'gabrieltyson157'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livraria.db'  # Exemplo com SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db.init_app(app)

    from .destaque import destaque_bp
    app.register_blueprint(destaque_bp)

    return app