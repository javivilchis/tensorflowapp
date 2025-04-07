from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import openai  # ✅ Import openai for exception handling
import os
import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Set API Key for OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY is missing. Set it as an environment variable.")
    raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY before running the app.")

# Initialize OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

# Load LLaMA Model from Hugging Face (You may need a GPU for better performance)
llama_model = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        if not data or "message" not in data:
            logging.warning("No message provided in request.")
            return jsonify({"error": "No message provided"}), 400

        user_message = data["message"].strip()
        model_name = data.get("model", "gpt-4o")  # Default to GPT-4o

        logging.info(f"Received message: {user_message} | Model: {model_name}")

        # OpenAI GPT-4o
        if model_name == "gpt-4o":
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": user_message}]
            )
            reply = response.choices[0].message.content

        # Meta LLaMA 
        # This requires permission: model_name = "meta-llama/Llama-2-7b-chat-hf"
        elif model_name == "mistralai/Mistral-7B-Instruct-v0.1":
            #this model does not require authentication
            response = llama_model(user_message, max_length=200, do_sample=True)
            reply = response[0]["generated_text"]

        else:
            return jsonify({"error": "Invalid model name"}), 400

        logging.info(f"Response: {reply}")
        return jsonify({"response": reply})

    except openai.APIError as e:
        logging.error(f"OpenAI API Error: {str(e)}")
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500

    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
