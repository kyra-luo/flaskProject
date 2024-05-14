from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from flask_login import UserMixin


# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to

commembers = sa.Table(
    'commembers',
    db.metadata,
    sa.Column('member_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True),
    sa.Column('community_id', sa.Integer, sa.ForeignKey('community.id'),
              primary_key=True)
)

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    User_id: so.Mapped[str] = so.mapped_column(sa.String(6), unique=True, nullable=False)
    fname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    lname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')
    
    communities: so.WriteOnlyMapped['Community'] = so.relationship(
        secondary=commembers, primaryjoin=(commembers.c.member_id == id),
        secondaryjoin=(commembers.c.community_id == 'community.id'),
        back_populates='members')
    # write_comments: so.WriteOnlyMapped['Comment'] = so.relationship(back_populates='commentor')

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
    # community_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("community.id"),
    #                                           index=True)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=True)
    community: so.Mapped['Community'] = so.relationship(back_populates='community_posts')
    author: so.Mapped[User] = so.relationship(back_populates='posts')
#     comments: so.WriteOnlyMapped['Comment'] = so.relationship(back_populates='UnderPost')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
# class Comment(db.Model):
#     id: so.Mapped[int] = so.mapped_column(primary_key=True)
#     comment: so.Mapped[str] = so.mapped_column(sa.String(140))
#     timestamp: so.Mapped[datetime] = so.mapped_column(
#         index=True, default=lambda: datetime.now(timezone.utc))
#     user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
#                                                index=True)
#     post_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Post.id),
#                                                index=True)
#     UnderPost: so.Mapped[Post] = so.relationship(back_populates='comments')
#     Commentor: so.Mapped[User] = so.relationship(back_populates='write_comments')

# class User(db.Model):
#     id: so.Mapped[int] = so.mapped_column(primary_key=True)
#     User_id: so.Mapped[str] = so.mapped_column(sa.String(6), unique=True, nullable=False)
#     fname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
#     lname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
#     username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
#     email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
#     password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

#     def __repr__(self):
#         return f"<User {self.username}>"

class Community(db.Model):
    __tablename__ = "community"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    communityName: so.Mapped[str] = so.mapped_column(sa.String(15), index=True,
                                                unique=True)
    category: so.Mapped[str] = so.mapped_column(sa.String(10), index=True,
                                             unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(50))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))  
    
    community_posts: so.WriteOnlyMapped[Post] = so.relationship(back_populates='community')

    members:  so.WriteOnlyMapped[User] = so.relationship(
        secondary=commembers, primaryjoin=(commembers.c.community_id == id),
        secondaryjoin=(commembers.c.member_id == User.id),
        back_populates='communities')
    

    def __repr__(self):
        return '<Community {}>'.format(self.communityName)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
