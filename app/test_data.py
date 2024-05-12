from app import db
from app.models import User, Post, Comment

# Create fake users
user = db.session.get(User, 1)
sample_posts = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa."


post1 = Post(
    topic="topic1",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user
)

comment1_post1 = Comment(
    comment="post1_1 " + sample_posts,
    commentor=user,
    underPost=post1
)

comment2_post1 = Comment(
    comment="post1_2 " + sample_posts,
    commentor=user,
    underPost=post1
)

comment3_post1 = Comment(
    comment="post1_3 " + sample_posts,
    commentor=user,
    underPost=post1
)

post2 = Post(
    topic="topic2",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user
)
comment1_post2 = Comment(
    comment="post2_1 " + sample_posts,
    commentor=user,
    underPost=post2
)

db.session.rollback()
# Add users to the database session
db.session.add_all([comment1_post2])

# Commit the session to the database
db.session.commit()
