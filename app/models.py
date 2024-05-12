from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from random import randint

class Community(db.Model):
    communityid: so.Mapped[int] = so.mapped_column(primary_key=True)
    communityName: so.Mapped[str] = so.mapped_column(sa.String(15), index=True,
                                                unique=True)
    category: so.Mapped[str] = so.mapped_column(sa.String(10), index=True,
                                             unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(50),
                                             unique=True)
    #createddate: so.Mapped[Optional[datetime]] = so.mapped_column(
        #default=lambda: datetime.now(timezone.utc))
    #host: so.Mapped[int] = so.mapped_column(sa.ForeignKey(???),index=True) -- optional
    #posts: so.Mapped[Posts] = so.relationship(back_populates='???')
    #members: so,Mapped[Users]


    def __repr__(self):
        return '<Community {}>'.format(self.communityName)


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
