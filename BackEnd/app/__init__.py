import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Build absolute path to instance/portfolio.db (cross-platform)
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '../instance/portfolio.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Enable CORS and initialize extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    # Import models so Flask-Migrate can detect them
    from app import models

    return app
