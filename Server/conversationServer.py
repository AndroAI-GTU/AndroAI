from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import logging
import os 

app = Flask(__name__)
CORS(app)  # We enable CORS support

# Logging settings
logging.basicConfig(level=logging.INFO)

@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json.get('message')
    user_id = request.json.get('userId')
    app.logger.info(f"Received message from user: {user_message}, User ID: {user_id}")

    if not user_id:
        app.logger.error("Missing userId in the request")
        return jsonify({"error": "userId is required"}), 400

    try:

        rasa_response = requests.post(
            'http://rasa:5005/webhooks/rest/webhook', 
            json={"message": user_message, "sender": user_id}
        )
        rasa_response.raise_for_status()
        app.logger.info(f"Received response from Rasa: {rasa_response.json()}")
        return jsonify(rasa_response.json())
    

    except requests.exceptions.RequestException as e:
        
        app.logger.error(f"Error occurred while sending message to Rasa: {e}")
        return jsonify({"error": "Failed to connect to Rasa server"}), 500


if __name__ == '__main__':
    app.logger.info("Starting Flask server...")
    port = int(os.environ.get('FLASK_PORT', 5001))
    app.run(host='0.0.0.0', port=port)
