from app import db
from app.models import User, Post, Community

# Create fake users
user1 = User(
    User_id="123456", 
    fname="Alice", 
    lname="Johnson", 
    username="alicej", 
    email="alice.johnson@example.com", 
    password_hash="cat"
)

user2 = User(
    User_id="234567", 
    fname="Bob", 
    lname="Smith", 
    username="bobsmith", 
    email="bob.smith@example.com", 
    password_hash="cat"
)

user3 = User(
    User_id="345678", 
    fname="Charlie", 
    lname="Brown", 
    username="charlieb", 
    email="charlie.brown@example.com", 
    password_hash="cat"
)

user4 = User(
    User_id="456789", 
    fname="Diana", 
    lname="Prince", 
    username="dianap", 
    email="diana.prince@example.com", 
    password_hash="cat"
)

user5 = User(
    User_id="567890", 
    fname="Eve", 
    lname="White", 
    username="evew", 
    email="eve.white@example.com", 
    password_hash="cat"
)

post1 = Post(
    topic="topic1",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user5
)

post2 = Post(
    topic="topic2",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user2
)

community1 = Community(
    Community_id = "111",
    communityName = "Community 1",
    category = "IT",
    description = "CITS",
    members=user3,
    community_posts=post1

)

# Add users to the database session
db.session.add_all([user1, user2, user3, user4, user5])

# Commit the session to the database
db.session.commit()
