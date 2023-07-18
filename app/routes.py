from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm

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
        flash(f'{login_form.email.data} logged in!', category='success')
        return redirect('/')
    return render_template('signin.jinja', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        user_name = form.username.data
        flash(f'{first_name if first_name else user_name} registerd', category='success')
        return redirect('/')
    return render_template('register.jinja', form=form)