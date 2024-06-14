from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, login_required
from blog_app.models.user import User, db

auth = Blueprint('auth', __name__, template_folder='../templates')

@auth.route('/')
def home(): 
    return render_template('auth/home.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()

        if existing_user: 
            print("El usuario ya existe")
            return jsonify({'error': 'El usuario ya existe'}), 400
        
        user = User(username=username, password=password)
        if User.query.count() == 0: 
            user.is_admin = True
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'success': True}), 200
    
    return render_template('auth/signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if not user or not user.password == password: 
            return jsonify({'error': 'Usuario o contraseña incorrectos'}), 400

        login_user(user)
        return jsonify({'success': True}), 200  # Devuelve una respuesta JSON de éxito
    
    return render_template('auth/login.html')

@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.home'))
