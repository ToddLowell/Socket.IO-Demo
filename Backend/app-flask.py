from flask import Flask, make_response, request
from flask_socketio import SocketIO
import base64
from datetime import datetime
from logger import log

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def hello():
    response = make_response(f"Hello World! Running on {request.host}.", 200)
    response.mimetype = "text/plain"
    return response


@app.route("/image", methods=["POST"])
def image():
    if request.method == "POST":
        socketio.emit("image", {"data": request.json["key"]})
        return "", 201


# enocde image to Base64 to send to client
def send_image(file_name="./botw.jpg"):
    with open(file_name, "rb") as img:
        encode = base64.b64encode(img.read())
        socketio.emit("image", {"data": encode.decode("utf-8")})


@socketio.event
def connect():
    print(f"{log('[CONNECTION_STATUS]', 'green')} {request.sid} connected")

    socketio.start_background_task(send_image)


@socketio.event
def disconnect():
    print(f"{log('[CONNECTION_STATUS]', 'red')} {request.sid} disconnected")


# send datetime to client
@socketio.event
def get_datetime(data):
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    return now


if __name__ == "__main__":
    socketio.run(app, port=8000)