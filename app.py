# gemini ai integration
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# Gemini 2.0 Flash endpoint
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_msg = request.args.get("msg", "")
    if not user_msg.strip():
        return "Please ask something."

    payload = {
        "contents": [
            {
                "parts": [{"text": user_msg}]
            }
        ]
    }

    try:
        response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        return reply
    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)


# local dataset 
# from flask import Flask, render_template, request, jsonify
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# import json
# import re
# import difflib

# app = Flask(__name__)

# # Load the Q&A data
# with open("skincare_data.json", "r", encoding="utf-8") as file:
#     qa_data = json.load(file)

# def normalize(text):
#     # Lowercase and remove punctuation
#     return re.sub(r'[^\w\s]', '', text.lower().strip())

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/get", methods=["GET"])
# def get_response():
#     user_msg = normalize(request.args.get("msg", ""))

#     # Try exact match or close match for any question in the dataset
#     for pair in qa_data:
#         for q in pair["questions"]:
#             normalized_q = normalize(q)

#             if normalized_q in user_msg or user_msg in normalized_q:
#                 return pair["answer"]
            
#             # Fuzzy match using difflib
#             if difflib.SequenceMatcher(None, normalized_q, user_msg).ratio() > 0.8:
#                 return pair["answer"]

#     return "I'm sorry, I don't have an answer for that yet. Could you try rephrasing?"


# if __name__ == "__main__":
#     app.run(debug=True)




# use of OpenAI API
# from flask import Flask, request, render_template
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# # Set OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/get", methods=["GET"])
# def get_response():
#     user_msg = request.args.get("msg", "")

#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",  # Or "gpt-4"
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "You are a helpful skincare assistant. Answer user questions clearly and in friendly, concise language."
#                 },
#                 {
#                     "role": "user",
#                     "content": user_msg
#                 }
#             ],
#             temperature=0.6,
#             max_tokens=300
#         )

#         reply = response.choices[0].message.content.strip()
#         return reply

#     except Exception as e:
#         return f"Oops! Something went wrong: {str(e)}"
        

# if __name__ == "__main__":
#     app.run(debug=True)
