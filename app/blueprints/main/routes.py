from flask import render_template, g
from . import bp as main

@main.route('/')
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

