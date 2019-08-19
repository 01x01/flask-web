from flask.views import MethodView 
from flask import request,jsonify,g
from .models import User 
from app import db
from .token import tokenAuth


USERNAME_OR_PASSWORD_IS_NONE_ERROR = {"id":401,"message":"please specify the username/password"}
NO_USER_ERROR = {"id":402, "message":"No such user"}
PASSWORD_ERROR = {"id":403, "message":"password error"}
LOGIN_SUCCESS = {"id":200, "message":"Login Successful"}
REGISTER_SUCCESS = {"id":200, "message":"Register Successful"}
USER_EXSIST = {"id":300, "message": "User exists!"}


class RegisterView(MethodView):
    
    def post(self):
        args = request.get_json()
        username = args.get('username')
        password = args.get('password')
        user  = User.query.filter_by(username=username).first()
        if user:
            return jsonify(USER_EXSIST)
        
        else:
            user = User(username=username)
            user.password = password
            db.session.add(user)
            db.session.commit()
            return jsonify(REGISTER_SUCCESS)



class LoginView(MethodView):
    def get(self):
        return "login page"
    
    def post(self):
        args = request.get_json()
        username = args.get('username')
        password = args.get('password')
        if username is None or password is None:
            return jsonify(USERNAME_OR_PASSWORD_IS_NONE_ERROR)
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify(NO_USER_ERROR)
        
        if user.verify_password(password):
            token = user.generate_auth_token()
            # db.session.commit()
            LOGIN_SUCCESS.update({"token":token.decode('utf-8')})
            return jsonify(LOGIN_SUCCESS)
        else:
            return jsonify(PASSWORD_ERROR)
            

        
class UserProfile(MethodView):
    decorators = [tokenAuth.login_required]
    def get(self):
        return jsonify({"user":g.current_user.username})


