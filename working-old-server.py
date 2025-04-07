from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
import openai
import os
import logging

print("Current Working Directory:", os.getcwd())
print("Expected template path:", os.path.exists("templates/index.html"))
# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Set API Key for OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY is missing. Set it as an environment variable.")
    raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY before running the app.")

# Initialize OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        if not data or "message" not in data:
            logging.warning("No message provided in request.")
            return jsonify({"error": "No message provided"}), 400

        user_message = data["message"].strip()
        logging.info(f"Received message: {user_message}")

        # GPT-4o Chat Completion
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
        logging.info(f"Response: {reply}")

        return jsonify({"response": reply})

    except openai.APIError as e:
        if "insufficient_quota" in str(e):
            logging.error("Quota exceeded.")
            return jsonify({"error": "You have exceeded your OpenAI API quota. Check your billing or usage limits."}), 429
        else:
            logging.error(f"OpenAI API Error: {str(e)}")
            return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500

    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)