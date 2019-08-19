from . import auth
from .views import RegisterView, \
                    LoginView, \
                    UserProfile \



auth.add_url_rule('/register', view_func=RegisterView.as_view('register'))
auth.add_url_rule('/login', view_func=LoginView.as_view('login'))
auth.add_url_rule('/userinfo', view_func=UserProfile.as_view('userinfo'))