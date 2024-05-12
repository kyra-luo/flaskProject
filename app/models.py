from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
# Create a new database callled user, for user register, which content id(UI&PK), id after format, Firstname,
# lastname,username and the email and password_hash to

    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    def __repr__(self):