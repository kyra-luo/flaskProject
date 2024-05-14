from app import db
from app.models import User, Post, Community

# Create fake users
user = db.session.get(User, 1)



post1 = Post(
    topic="topic1",
    body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
    author=user
)

community1 = Community(
   communityName = "Community 1",
    category = "IT",
    description = "CITS",
    community_posts=post1
)


user.communities.append(community1)
community1.members.append(user)

#commembers = [
#    {'member_id': user.id, 'community_id': community1.id},
#]

# Add users to the database session
db.session.add_all([user, post1, community1])

# Commit the session to the database
db.session.commit()
