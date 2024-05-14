from flask import Flask
from config import Config, DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# csrf = CSRFProtect(app)
#inital the login
login = LoginManager(app)
login.login_view = 'login'
# print(app.config['SQLALCHEMY_DATABASE_URI'])

from app import routes, models
#
# with app.app_context():
#     db.create_all()


