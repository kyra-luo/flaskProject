
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from random import randint

# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    User_id: so.Mapped[str] = so.mapped_column(sa.String(6), unique=True, nullable=False)
    fname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    lname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return f"<User {self.username}>"
