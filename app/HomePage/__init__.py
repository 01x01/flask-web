from flask import Blueprint  
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Blueprint
homepage =  Blueprint('homepage',__name__,url_prefix='/')
import views,forms,models.routes