from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session

app = Flask(__name__)

##########################################
#              Main Routes               #
##########################################

@app.route('/')
def index():
    '''Display homepage'''
    return render_template('index.html')

@app.route('/chat')
def chat():
    '''Display chatpage'''
    return render_template('chat.html')

if __name__ == "__main__":
    app.run(debug=True)
