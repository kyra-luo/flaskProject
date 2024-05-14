import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, create_app
from flask_migrate import Migrate
from app.models import User, Post
from config import DevelopmentConfig as D

app = create_app(D)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}