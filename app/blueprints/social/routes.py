from flask import render_template, redirect, flash, url_for, g
from flask_login import current_user
from app import app
from app.forms import PostForm, UserSearchForm
from app.models import Post, User
from . import bp

@app.before_request
def before_request():
    g.search_form = UserSearchForm()

@bp.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, user_id = current_user.user_id)
        post.commit()
        flash('Posted',category = 'success')
        return redirect(url_for('social.profile', username = current_user.username))
    return render_template('post.jinja', form = form, search_form = g.search_form)

@bp.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()
    if user:
        # posts = Post.query.filter_by(user_id=user.user_id).all()
        posts = user.posts
        print(user.posts)
        return render_template('profile.jinja', search_form = g.search_form, username = username, posts = posts)
    else:
        flash(f'User: {username} isn\'t valid',category='alert')
        return redirect(url_for('main.home'))
    
@bp.post('/user-search')
def user_search():
    return redirect(url_for('social.profile', username = g.search_form.username.data))
    