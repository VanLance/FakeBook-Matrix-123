from flask import render_template, redirect, flash
from flask_login import current_user
from app.forms import PostForm
from app.models import Post
from . import bp

@bp.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, user_id=current_user.user_id)
        post.commit()
        flash('Posted',category='success')
        redirect('/')
    return render_template('post.jinja', form=form)