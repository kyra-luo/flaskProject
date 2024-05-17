from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from hashlib import md5

# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to





class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    User_id: so.Mapped[str] = so.mapped_column(sa.String(6), unique=True, nullable=False)
    fname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    lname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    about_me: so.Mapped[str] = so.mapped_column(sa.String(250), nullable=True)
    #Communities: so.Mapped[str] = so.mapped_column(sa.String(250),nullable=True)



    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')

    # write_comments: so.WriteOnlyMapped['Comment'] = so.relationship(back_populates='commentor')
    write_comments: so.WriteOnlyMapped['Comment'] = so.relationship(back_populates='commentor')

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    topic: so.Mapped[str] = so.mapped_column(sa.String(250))
    body: so.Mapped[str] = so.mapped_column(sa.String(50000))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)
    # community_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('community.id'),
    #                                               index=True)
    author: so.Mapped[User] = so.relationship(back_populates='posts')
    comments: so.WriteOnlyMapped['Comment'] = so.relationship(back_populates='underPost')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
class Comment(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    comment: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)
    post_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Post.id),
                                               index=True)
    underPost: so.Mapped[Post] = so.relationship(back_populates='comments')
    commentor: so.Mapped[User] = so.relationship(back_populates='write_comments')


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))