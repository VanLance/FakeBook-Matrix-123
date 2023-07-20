from flask import request, jsonify
from . import bp as api
from app.models import User

@api.post('/register')
def register():
    content, response = request.json, {}
    print(content)
    if User.query.filter_by(email=content['email']).first():
      response['email error']=f'{content["email"]} is already taken/ Try again'
    if User.query.filter_by(username=content['username']).first():
      response['username error']=f'{content["username"]} is already taken/ Try again'
    if 'password' not in content:
       response['message'] = "Please include password"
    u = User()
    u.from_dict(content)
    try:
      u.hash_password(u.password)
      u.commit()
      return jsonify({'message': f'{u.username} is registered'}, 200)
    except:
      return jsonify(response),400