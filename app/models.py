from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(20))
    about_me: so.Mapped[str] = so.mapped_column(sa.String(250))
    #community_id: db.Column(db.Integer, db.ForeignKey('community.id'))

    def __repr__(self):
        return f"<User {self.name}>"