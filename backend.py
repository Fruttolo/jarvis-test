
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
from flask import Flask, request, jsonify, send_from_directory
from geminiBOT import geminiBOT, reset_chat

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    reset_chat()
    return send_from_directory('.', 'frontend.html')


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    req = data.get('req', '')
    try:
        response = geminiBOT(req)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27000)
