# TensorFlow Chatbot with OpenAI Integration

## ⚠️ Use at Your Own Risk

Hey! Just a heads-up — this app is shared for learning and experimenting. If you want to use it for something serious, it’s best to **fork the repo** and make your own copy.

Feel free to dive in, play around, and make it your own — but keep in mind:

- There's **no guarantee** everything will work perfectly.
- Make sure to **check the code and dependencies** yourself.
- Test things out before using it in anything important.

Basically: use it, tweak it, break it, fix it — just know it's all **at your own risk**. 😉

[![Creative Commons License](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)  
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## Overview
This project implements a **chatbot** application built using **TensorFlow** and integrated with **OpenAI's GPT-3** (or GPT-4) API. The application allows users to interact with the chatbot in real-time, leveraging the power of OpenAI’s language model to provide human-like responses. Additionally, the chatbot can interpret code snippets and run JavaScript directly in the browser.

The project demonstrates how TensorFlow, OpenAI, and a custom-built Flask server can be used together to provide intelligent conversational experiences.

## Features

- **Real-Time Chat:** Users can send text-based messages to the AI chatbot, and receive immediate responses.
- **Code Interpretation:** If the AI response contains code, users can click a button to run JavaScript directly in the browser.
- **File Upload:** Users can upload text files, which the AI can read and analyze.
- **Copy to Clipboard:** Each response from the chatbot has a button to copy the content for easy sharing.

## Technologies Used

- **TensorFlow:** Used for integrating machine learning models, though the primary language model is provided by OpenAI.
- **Flask:** Backend server that handles API requests and serves the front-end assets.
- **OpenAI GPT-3 (or GPT-4):** Used for natural language processing to generate human-like chatbot responses.
- **JavaScript (for code execution):** Embedded JavaScript that allows users to execute code provided by the AI directly in the browser.
- **Bootstrap 5:** Front-end CSS framework used to create a responsive and clean user interface.
- **Python:** Backend code that processes chat requests and communicates with the OpenAI API.

## Installation

### Prerequisites
- Python 3.x
- Node.js (for any frontend-related tasks)
- OpenAI API key (You will need to create an account at [OpenAI](https://www.openai.com/) and get your API key)

### Steps to Set Up Locally

1. **Clone the repository:**
    ```bash
   git clone https://github.com/yourusername/tensorflow-openai-chatbot.git
   cd tensorflow-openai-chatbot
    ```
    then, navigate to the project directory:

    ```bash
    cd your-repository-name
    ```

2. **Create and activate a virtual environment**
    It’s recommended to use a virtual environment to manage the dependencies for this project.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install dependencies**

    Once the virtual environment is activated, install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all necessary libraries, including Flask, OpenAI, TensorFlow, and other dependencies.

4. **Set up environment variables**

    The application requires the OpenAI API key to function. You can obtain the API key by signing up at OpenAI.

    For macOS/Linux, set the OpenAI API key by running:
    ```bash
    export OPENAI_API_KEY="your-api-key"
    ```
    Be sure to replace "your-api-key" with your actual OpenAI API key.

5. **Run the Flask app**

    Start the Flask development server by running the following command:

    ```bash
    python app.py
    ```
    The Flask app will start and be accessible at http://127.0.0.1:5000.

6. **Access the app**

    Open your web browser and go to `http://127.0.0.1:5000`. You should see the chatbot interface, where you can start interacting with the AI.

**How to Use**

Once the app is running, you can interact with the AI chatbot through the following features:
    <li>Chat: Type your message in the input field and click “Send” to interact with the AI.
    <li>File Upload: Click the 📎 icon next to the input field to upload a file (e.g., .txt file) for the AI to analyze. The AI will respond with insights based on the file’s content.
    <li>Code Responses: If the AI provides code, it will be formatted for easy reading and can be copied for use.

Example Interaction
    <ol><li>Type a message, such as “What’s the weather like today?” and press “Send.”
    <li>The AI will respond with weather information.
    <li>Upload a .txt file, and the AI will analyze it and answer questions based on the contents.</li></ol>

***Deployment***

To deploy the app in a production environment, use a WSGI server like Gunicorn or deploy it to a cloud platform such as Heroku, AWS, or DigitalOcean.

## To run the app with Gunicorn:

1.	**Install Gunicorn:**
```bash
pip install gunicorn
```

2.	**Start the app with Gunicorn:**
```bash
gunicorn app:app
```

This will run the app using Gunicorn as the WSGI server.

License

This project is licensed under the MIT License - see the LICENSE file for details.