from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def hello():
    return render_template('index.html')


@socketio.on('user speaks')
def handle_json(json):
    speech_text = json['data']
    print('Melissa thinks you said: ' + speech_text)

    emit('melissa replies', 'thank you')

if __name__ == "__main__":
    socketio.run(app)
