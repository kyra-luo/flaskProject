from flask import Flask
from config import Config, DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)
# csrf = CSRFProtect(app)
#inital the login
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
print(app.config['SQLALCHEMY_DATABASE_URI'])
print("ADMINS config:", app.config['ADMINS'])

db = SQLAlchemy()
moment = Moment()
login=LoginManager()
login.login_view = 'main.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    from app.blueprint import main
    app.register_blueprint(main)
    db.init_app(app)
    # migrate = Migrate(app, db)
    moment.init_app(app)
    # csrf = CSRFProtect(app)
    login.init_app(app)

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return app

from app import routes, models
#
# with app.app_context():
#     db.create_all()



from app import routes, models