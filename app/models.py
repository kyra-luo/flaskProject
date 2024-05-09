from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Community(db.Model):
    communityid: so.Mapped[int] = so.mapped_column(primary_key=True)
    communityName: so.Mapped[str] = so.mapped_column(sa.String(15), index=True,
                                                unique=True)
    category: so.Mapped[str] = so.mapped_column(sa.String(10), index=True,
                                             unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(50),
                                             unique=True)
    #timestamp:
    #host: so.Mapped[int] = so.mapped_column(sa.ForeignKey(???),index=True) -- optional
    #posts: so.Mapped[Posts] = so.relationship(back_populates='???')
    #members: so,Mapped[Users]


    def __repr__(self):
        return '<Community {}>'.format(self.communityName)