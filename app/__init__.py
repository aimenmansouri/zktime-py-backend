from flask import Flask
from app.routes.main_routes import example_bp

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(example_bp)

    return app