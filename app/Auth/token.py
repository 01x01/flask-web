from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired,BadSignature
from flask import g,current_app
from app.Auth.models import User
from flask_httpauth import HTTPTokenAuth

tokenAuth = HTTPTokenAuth(scheme="Bearer")

@tokenAuth.verify_token
def verify_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        print("SignatureExpired")
        return False
    except BadSignature:
        return False
    
    user = User.query.get(data['id'])
    g.current_user = user
    return g.current_user is not None
