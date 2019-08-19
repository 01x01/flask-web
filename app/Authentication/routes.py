from . import auth
from .views import RegisterView, LoginView 


auth.add_url_rule('/register', view_func=RegisterView.as_view('register'))
auth.add_url_rule('/login', view_func=LoginView.as_view('login'))