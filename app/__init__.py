from flask import Flask 
from config import config 

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 注册规则，方便后续使用正则表达式表示动态路由
    from werkzeug.routing import BaseConverter
    class MyConverter(BaseConverter):
        def __init__(self,map,regex):
            super().__init__(map)
            self.regex=regex

    app.url_map.converters['rule']=MyConverter

    from app.HomePage import homepage 
    app.register_blueprint(homepage)
    
    return app

    