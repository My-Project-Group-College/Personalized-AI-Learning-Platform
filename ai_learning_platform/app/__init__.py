from flask import Flask
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
    return app