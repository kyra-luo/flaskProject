from app import db
from app.models import User, Post, Community

# Create fake users
user = db.session.get(User, 1)
community = db.session.get(Community, 1)



community2 = Community(
   communityName = "Community 2",
    category = "It",
    description = "CS",
)

post2 = Post(
    topic="topic2",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user,
    community=community2
)





db.session.rollback()
# Add users to the database session
db.session.add_all([community2, post2])

# Commit the session to the database
db.session.commit()

db.session.rollback()

user.communities.add(community)
community.members.add(user)

db.session.commit()