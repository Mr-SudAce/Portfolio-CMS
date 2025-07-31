import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import db
from app.routes.api_routes import api
from app.routes.temp_routes import main

migrate = Migrate()

# --- Import models to register with SQLAlchemy ---
from .models import *

def create_app():
    app = Flask(__name__)

    # Build absolute path to instance/portfoliocms.db (cross-platform)
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '../instance/portfoliocms.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')
    
    
      # ✅ Add route to serve uploaded files
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        from flask import send_from_directory
        uploads_dir = os.path.abspath(os.path.join(basedir, '../uploads'))
        return send_from_directory(uploads_dir, filename)


    return app
