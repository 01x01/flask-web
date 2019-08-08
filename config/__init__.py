# coding: utf-8 
import os 
class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')




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