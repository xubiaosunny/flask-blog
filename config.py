#-*coding:utf-8-*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or ' le day ga ga'
    #SQL
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #email
    MAIL_SERVER = 'smtp.mxhichina.com'
    MAIL_PORT = 25
    #MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'admin@xubiaosunny.net'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Xu1234567890'

    POSTS_PER_PAGE = 20
    FOLLOWERS_PER_PAGE = 20
    COMMENTS_PER_PAGE = 20
    @staticmethod
    def init_app(app):
        pass
'''
开发配置
'''
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or  'mysql://root:771743@localhost/test'


'''
测试配置
'''
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or  'mysql://root:771743@localhost/test'


'''
生产配置
'''
class ProductionCOnfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or  'mysql://root:771743@localhost/blog'

#
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionCOnfig,
    'default':DevelopmentConfig
}