from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import db
from app.models import User, Post

# Assuming your database URL
engine = create_engine('sqlite:////Users/wenjiesong/Desktop/flaskProject/app.db')

# Specifying the IDs to delete
ids_to_delete = [3, 4, 5, 6, 7]

# Deleting users with the specified IDs
db.session.query(User).filter(User.id.in_(ids_to_delete)).delete(synchronize_session=False)

# Committing the changes to the database
db.session.commit()
