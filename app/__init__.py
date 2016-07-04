#-*-coding:utf-8-*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown


from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
mail = Mail()
moment = Moment()
pagedown = PageDown()


def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(config[configname])
    app.debug = True
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from main import main as mian_blueprint
    app.register_blueprint(mian_blueprint, url_prefix='/main')

    from api_1_0 import api as api_blueprint
    app.register_blueprint(api_blueprint,url_prefix='/api_1_0')


    return app
