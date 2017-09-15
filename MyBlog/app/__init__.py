# -*- coding: utf-8 -*-
from os import path

from flask import Flask
# from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import * #nav导航栏地址找不到
from flask_sqlalchemy import SQLAlchemy
from werkzeug.routing import BaseConverter

from flask_login import LoginManager

basedir = path.abspath(path.dirname('__file__'))
nav = Nav()
bootstrap = Bootstrap()
db = SQLAlchemy()
loginmanager = LoginManager()
loginmanager.session_protection = 'strong'
loginmanager.login_view = 'auth.login'


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex=items[0]#regex的属性名不能改动

def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    nav.register_element('top', Navbar(u'导航栏',
                                       View(u'主页', 'auth.index'),
                                       View(u'登录', 'auth.login'),
                                       View(u'注册', 'auth.register')
                                       ))
    nav.init_app(app)

    nav.init_app(app)
    db.init_app(app)

    bootstrap.init_app(app)

    from .auth import auth
    # from .main import main

    app.register_blueprint(auth)
    # app.register_blueprint(main, static_folder='static')

    loginmanager.init_app(app)
    return app

