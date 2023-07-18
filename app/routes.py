from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm
from app.models import User

@app.route('/')
def home():
    matrix_posts = {
        'instructors': {
            'sean':['Flask week is huge, lets not forget wbs'],
            'dylan': ['Yay it is flask time']
        },
        'students':{ student:[f'This is post {num}'] for num, student in enumerate(['ben','christian','sima','david'])}
    }
    print(matrix_posts['students'])
    return render_template('index.jinja', instructors=matrix_posts['instructors'], students=matrix_posts['students'], title='Fakebook Homepage')

@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(login_form.password.data):
            flash(f'{login_form.email.data} logged in!', category='success')
            return redirect('/')
        else:
            flash(f'Invaled User Data, Try Again!', category='warning')
    return render_template('signin.jinja', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        try:
            user = User(first_name=first_name, last_name=last_name, username = username, email=email)
            user.hash_password(form.password.data)
            user.commit()
            flash(f'{first_name if first_name else username} registered', category='success')
            return redirect('/')
        except:
            flash(f'Username or Email already taken, Try Again', category='warning')
    return render_template('register.jinja', form=form)