from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to
class User(db.Model):
    # __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    User_id: so.Mapped[str] = so.mapped_column(sa.String(6), unique=True, nullable=False)
    fname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    lname: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.User_id = '{:06d}'.format(self.id)  # 在初始化时自动生成六位数的id字符串

    def __repr__(self):
        return f"<User {self.username}>"

    def encrypted_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Display id at inner HTML
    @property
    def display_id(self):
        return self.User_id



