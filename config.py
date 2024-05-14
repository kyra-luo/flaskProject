import os
# get the path for this file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'
    SQLALCHEMY_TRACK_MODIFICATIONS = False