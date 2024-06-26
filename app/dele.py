from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import db
from app.models import User, Post, Comment, Community

# Assuming your database URL
engine = create_engine('sqlite:////Users/wenjiesong/Desktop/flaskProject/app.db')

# Specifying the IDs to delete
ids_to_delete = [1]

# Deleting users with the specified IDs
db.session.query(Community).filter(Community.id.in_(ids_to_delete)).delete(synchronize_session=False)

# Committing the changes to the database
db.session.commit()
