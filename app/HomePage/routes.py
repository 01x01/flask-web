from . import homepage
from .views import HomePage,User


homepage.add_url_rule("/",view_func=HomePage.as_view('homepage'))
homepage.add_url_rule('/user/<rule("\w{4}"):username>',view_func=User.as_view('user'))