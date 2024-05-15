from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('team_input.html')

@app.route('/live')
def live_page():
    return render_template('live_page.html')

@socketio.on('new_team')
def handle_new_team(data):
    team_name = data['teamName']
    team_number = data['teamNumber']
    emit('team_submission', {'teamName': team_name, 'teamNumber': team_number}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
