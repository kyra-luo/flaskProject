from app import db
from app.models import User, Post, Comment, Community

# Create fake users
user = db.session.get(User, 1)
user2 = db.session.get(User, 2)
community = db.session.get(Community, 1)

sample_posts = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa."

# community1 =Community(
#     communityName = "Community 1",
#     category = "IT",
#     description = "data science"
# )

# post1 = Post(
#     topic="topic1",
#     body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa.",
#     author=user,
#     community=community

# )

# comment1_post1 = Comment(
#     comment="post1_1 " + sample_posts,
#     commentor=user,
#     underPost=post1
# )

# comment2_post1 = Comment(
#     comment="post1_2 " + sample_posts,
#     commentor=user,
#     underPost=post1
# )

# comment3_post1 = Comment(
#     comment="post1_3 " + sample_posts,
#     commentor=user,
#     underPost=post1
# )

db.session.rollback()
# Add users to the database session
# db.session.add_all([ community, post1])

# # Commit the session to the database
# db.session.commit()

db.session.rollback()

user.communities.add(community)
community.members.add(user)
user2.communities.add(community)
community.members.add(user2)
db.session.commit()