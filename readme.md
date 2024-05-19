# A Discussion Forum (TBC) for CITS 5505 Group Project 
## Authors
### Wenjie Song 22470722@student.uwa.edu.au
### Zishan Luo 22448064@student.uwa.edu.au
### Jiehua Huang 24148088@student.uwa.edu.au
### Chuan Wang 23990575@studentt.uwa.edu.au

## Introduction

Welcome to our project, a discussion forum designed to facilitate vibrant and engaging community interactions. This platform will allow users to post content, join communities of interest, and communicate directly with other users. It's currently under development, and this README outlines the core features we plan to implement.

## Environment Setup

### Step 0 Python installed 
Make sure you already install the Python(Version 3.7 or higher version)

### Step 1 Cloning a repository
git clone https://github.com/kyra-luo/flaskProject.git<br>

### Step 2 Setting up the environment 
Create a virtual environment<br>
python3 -m venv venv <br>
source venv/bin/activate (For Linux and macOS)<br>
.\venv\Scripts\activate  (For Windows)<br>
Create a .env file, setting up the secret key to start the program
### Step 3 install the requirement 
pip install -r requirements.txt

### Step 4 Getting connection with the database
flask db upgrade

### Step 5 setting up the docker (requirement for the search function )
#### open a new terminal
docker run --name elasticsearch -d --rm -p 9200:9200 \
    --memory="2GB" \
    -e discovery.type=single-node -e xpack.security.enabled=false \
    -t docker.elastic.co/elasticsearch/elasticsearch:8.11.1
#### Enter to the flask shell
flask shell<br> 
Post.reindex()<br>
*press the control+ D to exit the flask shell<br>
**For more info please go to https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search

### Step 6 Starting the program 
flask run <br>
*Usually the program opened http://127.0.0.1:5000, but check which port are you using.


## Planned Features

### User Authentication

- **Login/Logout**: Secure authentication system allowing users to log in and out.
- **Registration**: New users can create an account to access the forum. When your 
registration successful, you will receive a welcome email from us.
- **Forget the password**: When you cannot remember your password, click the link, 'Can't remember your password?'
your will receive an email for us, submit the reset password form, the password will update. (Since you are working at 
on the local host, therefore you are not able to change the password through the email form, since the form cannot send 
back from the gmail to the localhost. Once you are working at the real server, you are able to change the password 
through the reset form  )

### Nav bar 
Navigation Bar before you login, you will only see the title of our website title, logo, login and regi button. 
But after you are login, you can use the search bar, link navigate you to community, Explore, Create, profile page.

### Posting System

- **Post Creation**: Only registered and logged-in users will be able to create posts.
- **Dynamic Ranking**: Posts will be displayed on the homepage, with the most recent posts at the top.

### Communities

- **Community Engagement**: Users can join communities that align with their interests, each hosting its own set of 
- discussions and posts.

### Comments

- **Comment to posts**: Users can comment on the posts posted by other users, share their thoughts about the post.

### Search Functionality

- **Efficient Searching**: A search feature to help users find specific posts or topics based on keywords.<br>

Search function is allow you to search the post body part, but require login.


### Replies (optional)

- **Discussions**: This is something really nice to have, as it futher promotes the discussion among the users, if 
- we do get time after implementing above essential functions, this should be considered first to be implemented.

### Messaging (optional)

- **Direct Messaging**: Users will have the ability to send private messages to others, facilitating direct and 
- personal communication.

### History (optional)

### Notifications (optional)

## Project Goals

This forum aims to create a welcoming and active environment where users can freely share and discuss their interests. 
Our goal is to implement a user-friendly interface with robust features that support community building and personal 
interaction.

## Contribution

While the project is still in the planning phase, we are open to ideas and suggestions. Feel free to reach out if you 
are interested in contributing or have any feedback on our proposed features.

## Contact

For more information or to get involved, please contact us at:

### Our student emails

- Email: 22470722@student.uwa.edu.au
- Project Link: [GitHub Repository](URL-to-your-repository)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

