import socketio
import base64
from datetime import datetime
from time import sleep
from logger import log

# create Socket.IO server and wrap into a WSGI application
sio = socketio.Server()
sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)


print(f"{log('[STATUS]', 'blue')} Server Started")

# enocde image to Base64 to send to client
def send_image(sid):
    with open("./botw.jpg", "rb") as img:
        encode = base64.b64encode(img.read())
        sio.emit("image", {"data": encode.decode("utf-8")}, to=sid)


@sio.event
def connect(sid, environ):
    print(f"{log('[CONNECTION_STATUS]', 'green')} {sid} connected")

    sio.start_background_task(send_image, sid)


@sio.event
def disconnect(sid):
    print(f"{log('[CONNECTION_STATUS]', 'red')} {sid} disconnected")


# send datetime to client
@sio.event
def get_datetime(sid, data):
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    return now
