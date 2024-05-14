from app import db
from app.models import User, Post, Community

# Create fake users
user1 = User(
    User_id="123456", 
    fname="Alice", 
    lname="Johnson", 
    username="alicej", 
    email="alice.johnson@example.com", 
    password_hash="cat",
    communities="community1"
)



post1 = Post(
    topic="topic1",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user1
)

post2 = Post(
    topic="topic2",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user1
)

community1 = Community(
    communityName = "Community 1",
    category = "IT",
    description = "CITS",
    community_posts=post1,
    members=user1
)
commembers = [
    {'member_id': user1.id, 'community_id': community1.id},
]
# Add users to the database session
db.session.add_all([user1])

# Commit the session to the database
db.session.commit()
