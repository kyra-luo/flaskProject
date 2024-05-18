from flask import Flask
from config import Config, DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from elasticsearch import Elasticsearch

mail=Mail()

db = SQLAlchemy()
moment = Moment()
login=LoginManager()
login.login_view = 'main.login'

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from app.blueprint import main
    app.register_blueprint(main)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login.init_app(app)
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return app

from app import models


