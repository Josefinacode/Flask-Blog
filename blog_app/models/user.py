from blog_app import db, login_manager
from flask_login import UserMixin

login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)  # Indica si el usuario es especial

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
