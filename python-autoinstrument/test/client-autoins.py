from flask import Flask, request, jsonify, render_template_string
import os
import requests
from time import sleep

app = Flask(__name__)

# Define the server endpoint
SERVER_ENDPOINT = "http://18.142.79.116:5000/server_request"

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask Client</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }
                #myButton {
                    padding: 20px 40px;
                    font-size: 24px;
                    cursor: pointer;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                #myButton:hover {
                    background-color: #0056b3;
                }
                #response {
                    margin-top: 20px;
                    font-size: 18px;
                    color: #333;
                }
                .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    text-align: center;
                }
                .text {
                    margin-bottom: 20px;
                    font-size: 24px;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="text">Click to send request</h1>
                <button id="myButton">Click Me!</button>
                <p id="response"></p>
            </div>
            <script>
                $(document).ready(function(){
                    $("#myButton").click(function(){
                        $.ajax({
                            url: "/send_request",
                            type: "POST",
                            data: JSON.stringify({param: "client-post"}),
                            contentType: "application/json",
                            success: function(response) {
                                $("#response").text("Response: " + response.message);
                            }
                        });
                    });
                });
            </script>
        </body>
        </html>
    ''')

@app.route('/send_request', methods=['POST'])
def send_request():
    data = request.json
    param = data.get("param")

    # Send requests in a loop with sleep intervals
    for i in range(0, 5):
        response = requests.get(SERVER_ENDPOINT, params={"param": param}, headers={})
        sleep(5)
        if response.status_code != 200:
            return jsonify({"message": f"Request failed with status code {response.status_code}"}), response.status_code

    return jsonify({"message": "Button was clicked and requests were sent!"})

if __name__ == '__main__':
    app.run(debug=False, port=8082, host='0.0.0.0')