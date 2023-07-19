from flask import render_template
from app import app

from app.forms import LoginForm

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

@app.route('/signin')
def sign_in():
    login_form = LoginForm()
    return render_template('signin.jinja', form=login_form)

@app.route('/register')
def register():
    return render_template('register.jinja')
