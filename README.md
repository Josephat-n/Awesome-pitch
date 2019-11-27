
# AWESOME-PITCH

# Name of author
Josphat Njoroge. <br>
Email: josphatnjoroge254@gmail.com

# Project Description
The project displays various pitch messages from various people and in different categories. A person who visits this site is able to view the pitch messages by category. <br>

One can click on a certain message so as to view more details such as the cretor of the pitch, when it was created and such. The user can also vote on any pitch, giving it an upvote or a downvote. <br>

To comment on any pitch, a user will have to be signed in. This implies that they have to be registered in first. The process of registration is followed by an email from the site informing you that you have been registered in the site.<br>

When a person is registered and signed in, they have the privilege of creating a pitch message in any category. They can view all the pitches that they have created in their profile page.<br>

# Development Methodology
Both BDD and TDD were used, with Bdd determining what test cases were designed and implemented. In a summary, this is the bdd: <br>

Given a user wants to view pitch messages by the use of our app, when they interract with the app, they will see various pitch messages grouped per category. They can click on a particular pitch to comment on it and maybe give it a vote. <br>

Given a user is already viewing a pitch, when they want to give it a vote (upvote or downvote), they can easily do so via buttons that are adjacent to the pitch. For this they will have to sign in first, if and only if they are registered in the system, else they will have to register first.

# Live-link 
The project is live at: https://jn-pitch.herokuapp.com

# Technology used
1. Python flask.<br>
2. Some third party modules such as Jinja2 and gunicorn, flask-uploads etc. The whole list of depencies is available at: https://github.com/Josephat-n/Awesome-pitch/blob/master/requirements.txt

# Setup Instructions
A user may interact with the app that is hosted in the live-link as indicated above, and in that case no setup is required but a functioning web-browser and internet connection.<br>

To run the application in a local machine, the basic requirement is to have python installed on the local machine that you are working with. If not, install python by running the following commands consequtively via terminal: "$ sudo add-apt-repository ppa:jonathonf/python-3.6", "$ sudo apt-get update" and finally "$ sudo apt-get install python3.6". Confirm that the intallation was successful by typing the following command  $ python3.6 <br>

If python is up and runnning, next you need to install some third party modules. All the other required modules are as indicated in the requirements.txt file available in this repo, and given in the link above.

### License
MIT &copy; Josephat Njoroge <br>
Anyone is free to fork, reuse, upgrade or do whatever partains this program without a prior request for permission.