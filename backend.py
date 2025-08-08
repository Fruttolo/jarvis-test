from flask import Flask, request, jsonify
from geminiBOT import geminiBOT

app = Flask(__name__)

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
