from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import base64

# Inicialización de SQLAlchemy y LoginManager fuera de la función create_app()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        db.create_all()

    # Define el filtro de plantilla aquí
    @app.template_filter('b64encode')
    def b64encode(b):
        return base64.b64encode(b).decode('utf-8')
    
    from blog_app.routes.auth import auth
    from blog_app.routes.blogs import blogs
    app.register_blueprint(auth)
    app.register_blueprint(blogs)
    return app

