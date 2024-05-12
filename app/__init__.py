

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # 正确从Config类加载配置

db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # 确保在函数内部导入 User
    return User.query.get(int(user_id))

# 导入放在最后以避免循环导入
from app import routes, models
