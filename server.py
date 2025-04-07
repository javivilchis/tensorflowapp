from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
import openai
import os
import logging

UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Setup
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

file_context = {"content": ""}  # global context to hold uploaded file content

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_context["content"] = f.read()
        return jsonify({"message": "File uploaded successfully."})
    except Exception as e:
        logging.exception("Failed to read file")
        return jsonify({"error": str(e)}), 500

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        messages = [{"role": "user", "content": user_message}]
        if file_context["content"]:
            messages.insert(0, {
                "role": "system",
                "content": f"The user uploaded the following file content. Use it for context:\n{file_context['content'][:2000]}"
            })

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})

    except Exception as e:
        logging.exception("Chat error")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)