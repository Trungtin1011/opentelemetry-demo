from flask import Flask, request, jsonify, render_template, send_from_directory, cli
import os
import requests
import logging

# Disable  * Serving Flask app 'server' AND * Debug mode: off
#cli.show_server_banner = lambda *x: None

logging.getLogger('werkzeug').disabled = True
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__, template_folder='.')

# Define the server endpoint
SERVER_ENDPOINT = os.environ.get('SERVER_ENDPOINT', 'http://localhost:5555/server_request')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call', methods=['POST'])
def send_request():
    param = request.json.get("param")
    logger.info(f"Python Single Client: Sending request {param}")

    # Send requests
    try:
        response = requests.get(SERVER_ENDPOINT, params={"param": param}, headers={})
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        python_failed = "Python Single Caller Failed:" in response.text
        res = ""

        if python_failed:
            logger.error("Cannot reach Python Single Server")
            res += "Cannot reach Python Single Server"
        else:
            logger.info(f"{response.text}")
            res += response.text

        return jsonify({"message": f"Python Single Client: {res}"})

    except requests.exceptions.RequestException as e:
        logger.error(f"Python Single Client Error: {e}")
        return jsonify({"message": f"Python Single Client Error: {e}"})

if __name__ == '__main__':
    app.run(debug=False, port=8082, host='0.0.0.0')
