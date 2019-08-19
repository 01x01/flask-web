from . import homepage 
from flask.views import MethodView 
from flask import current_app

class HomePage(MethodView):
    def get(self):
        return current_app.config['SECRET_KEY']


class User(MethodView):
    def get(self,username):
        return "Hello {username}".format(username=username)