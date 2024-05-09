from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from random import randint

# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to
def generate_user_id():
    return '{:06d}'.format(randint(0, 999999))
class User(db.Model):
    __tablename__ = 'users'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    User_id: so.Mapped[str] = so.mapped_column(sa.String(6), unique=True, nullable=False)
    fname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    lname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    def __init__(self, User_id, fname, lname, username, email, password_hash):
        self.User_id = User_id
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"<User {self.username}>"
