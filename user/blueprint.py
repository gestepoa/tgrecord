# coding: utf8
from flask import Blueprint
from utils.blueprint_util import add_resource
from . import views


# user
user_blueprint = Blueprint('user', __name__, url_prefix='/user')
config = [
    (views.UserView, '/')
]

add_resource(user_blueprint, config)


# basic_info
basic_info_blueprint = Blueprint('basic_info', __name__, url_prefix='/basic_info')
basic_info_config = [
    (views.BasicInfoViewQuery, '/query'),
    (views.BasicInfoViewAdd, '/add'),
    (views.BasicInfoViewUpdate, '/update'),
    (views.BasicInfoViewDelete, '/delete'),
    (views.Upload, '/upload')
]

add_resource(basic_info_blueprint, basic_info_config)
