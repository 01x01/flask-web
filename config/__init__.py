# coding: utf-8 
import os 
class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    





from .dev import DevConfig
from .qa import QAConfig
from .cm import CMConfig
from .prod import ProdConfig
config = {
    "dev" : DevConfig,
    "qa" : QAConfig,
    "cm" : CMConfig,
    "prod": ProdConfig

}