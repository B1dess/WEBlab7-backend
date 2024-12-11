from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

server_events = []


@app.route('/log_event', methods=['POST'])
def log_event():
    data = request.json
    event = {
        'event_number': data['event_number'],
        'time': datetime.now().strftime("%H:%M:%S"),
        'message': data['message']
    }
    server_events.append(event)
    return jsonify({"status": "success", "event": event}), 200


@app.route('/get_events', methods=['GET'])
def get_events():
    ret = server_events.copy()
    server_events.clear()
    return jsonify(ret), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
