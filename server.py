import socketio
import eventlet
import eventlet.wsgi
from sympy import *
import numpy as np
import random
from json import JSONEncoder
import json
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)


# @sio.on('clientQ', namespace='/')
# def connect(sid, environ):
#     print(sid)
#     print(environ)
    # sio.emit('reply', generateDerivativeQuestion())

@sio.on('questions', namespace='/')
def connect(sid, environ):
    # print('here')
    # temp = generateDerivativeQuestion()
    # print(temp)
    sio.emit('reply', temp)

@sio.on('questions2', namespace='/')
def connect(sid, environ):
    # print('here')
    # temp1 = generateIntegralQuestion()
    # print(temp1)
    sio.emit('reply2', temp1)
#
@sio.on('questions3', namespace='/')
def connect(sid, environ):
    # print('here')
    # temp2 = generateAlgebraQuestion()
    # print(temp2)
    sio.emit('reply3', temp2)

    # print("connect ", sid)
    # print("environ ", environ);
    # print environ[0]

# @sio.on('chat message', namespace='/chat')
# def message(sid, data):
#     print("message ", data)
#     sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
