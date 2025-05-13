from flask import Flask
from app.routes.main_routes import example_bp
from app.routes.attendance.attendance_route import attendance_bp
from app.routes.attendance.users_route import users_bp

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(example_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(users_bp)

    return app