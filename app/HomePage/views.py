from . import homepage 

@homepage.route('/')
def index():
    return "Hello flask"