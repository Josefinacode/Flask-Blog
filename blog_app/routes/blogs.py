from flask import Blueprint, redirect, url_for, request, render_template
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from blog_app import db
from blog_app.models.blog import Blog
import base64

blogs = Blueprint('blogs', __name__, template_folder='../templates')

@login_required
@blogs.route('/blogs', methods=['GET', 'POST'])
def blogs_list(): 
    return render_template('blogs/blogs.html', blogs=Blog.query.all())

@login_required
@blogs.route('/create_blog', methods=['GET', 'POST'])
def create_blog(): 
    if request.method == 'POST':
        if not current_user.is_admin: 
            return redirect(url_for('auth.home'))
        
        name = request.form.get('name')
        description = request.form.get('description')
        text = request.form.get('text')
        pic = request.files['pic']

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        img_data = pic.read()

        blog = Blog(name=name, description=description, text=text, img=img_data, mimetype=mimetype, img_name=filename, user_id=current_user.id)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('blogs.blogs'))
    
    return render_template('blogs/create_blog.html')

@login_required
@blogs.route('/tools/update_blog/<int:blog_id>', methods=['POST', 'GET'])
def update_blog(blog_id): 
    blog = Blog.query.get_or_404(blog_id)
    if request.method == 'POST':
        if not current_user.is_admin: 
            return redirect(url_for('blogs.blogs_list'))
        
        blog.name = request.form.get('title')
        blog.description = request.form.get('description')
        blog.text = request.form.get('text')

        pic = request.files['pic']
        blog.img = pic.read()
        blog.mimetype = pic.mimetype
        blog.img_name = secure_filename(pic.filename)
        blog.user_id = current_user.id

        db.session.commit()
        return redirect(url_for('blogs.blogs_list'))
    return render_template('blogs/update_blog.html', blog=blog)

@login_required
@blogs.route('/tools/delete_blog/<int:blog_id>', methods=['GET', 'POST'])
def delete_blog(blog_id):  # Cambia el nombre de la función aquí
    blog = Blog.query.get_or_404(blog_id)

    if not current_user.is_admin: 
        return redirect(url_for('blogs.blogs_lists'))
    
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blogs.blogs_lists'))

