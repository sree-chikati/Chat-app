# Chat-App
A simple, realtime chat application that allows users to create rooms and communicate with one another.


 ## Table of Contents
 * [Functions to Highlight](#functions-to-highlight)
 * [Challanges Faced](#challanges-faced)
 * [Deployment](#deployment)
 * [Demo](#demo)
 
## Functions to highlight
* Connecting server and client sides
* Implementation of Socket.io with Flask
* Authetication
* Client and Server side data showing up

## Challanges Faced
* Before even creating a chat app, I had to make sure the data is being received on both the server side and client side. I also needed to have a place where this data is being stored and displayed. This was a challange as I was not familiar with how to connect two servers togehter. However, I was able to overcome this by learning basics of Websockets and PHP.
* After data was sucessfully being sent and received, I worked on creating an authetication system that would link user accounts.
In order to create rooms, it is important to add existing users first. To solve this, I utlized MongoDB and Socket.io to connect the user accounts so they are able to chat with one another.
* Finally, one the authetication was working I needed to display the messages being sent by users in specific chat rooms. With a little JavaScript and tying in Socket.io, I was able to showcase messages being sent my users. This is still a work in progress and I hope to improve it's functionalities more.

## Deployment
In a terminal window, navigate to your newly created folder and clone:
```bash
git clone git@github.com:sree-chikati/chat-app.git
```

Deploy virtual environment.
```
python3 -m venv env
source env/bin/activate
```

Run the following commands from your virtual environment to install the needed packages
```bash 
pip3 install -r requirements.txt
```

On a development server
```bash 
# run
python3 app.py
```

## Demo
![alt text](preview.gif "Preview Gif")
