import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load training data
with open('chatbot_training_data.json', 'r') as file:
    data = json.load(file)

# Extract questions and labels
questions = [item['question'] for item in data]
labels = [item['label'] for item in data]

# Split data
X_train, X_test, y_train, y_test = train_test_split(questions, labels, test_size=0.2, random_state=42)

# Create and train model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

# Response dictionary with lists of responses
responses = {
    "greeting": [
        "Hi there! How can I help you today?",
        "Hello! What can I do for you?",
        "Hey! Ready to chat?",
        "I'm just code, but I'm doing great — how about you?",
        "Not much, just here to help. What’s up with you?"
    ],
    "identity": [
        "I’m real in your screen and code — not in the human way!",
        "I exist digitally, in the world of Python and logic.",
        "Nope, not a person — just a well-trained machine here to chat!",
        "Not human, but I try my best to be helpful and kind.",
        "Yes, a chatbot robot at your service 🤖!"
    ],
    "help": [
        "I can assist with answering questions, chatting, and offering guidance when needed.",
        "I'm here to support you with information, answers, and friendly conversation.",
        "I provide info, help with tasks, and chat with you — all in one!",
        "I work by matching your questions with the best answers I’ve been trained on.",
        "My purpose is to help, inform, and make your digital experience smoother!"
    ],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "food": ["How about trying something new like sushi or pasta?", "Pizza? Burgers? Or maybe some Indian street food?"],
    "travel": ["Visit Japan or the Swiss Alps. They're beautiful!", "You should check out Bali or Paris!"],
    "color": ["I love all colors, but blue is quite calming!", "Colors? I’d say sky blue, peaceful and cool."],
    "emotion": [
        "I don't have emotions, but I understand how important they are to you.",
        "Not really, but I can recognize emotional expressions and try to respond appropriately.",
        "I don't experience sadness, but I'm here if you need someone to talk to.",
        "I don't feel joy, but I'm always happy to help you!"
    ],
    "hobby": ["I enjoy learning and chatting!", "Talking to you is my hobby!"],
    "trivia": ["That's an interesting one! Want to know more?", "I’ve got tons of trivia! Ask away."],
    "movies": ["Try watching Inception or Interstellar!", "The Matrix and Spirited Away are classics!"],
    "python": ["Python is great for web, data, and AI!", "It’s my favorite language — clear, powerful, and fun!"],
    "study": ["Focus, make notes, and practice daily!", "Breaks + consistency = study success!"],
    "tech": ["AI, blockchain, and quantum computing are trending!", "Tech is evolving fast — exciting times ahead!"],
    "customer_care": ["Please call 1800-123-456 for support.", "Reach out to customer care at 1800-123-456."]
}

# Chat function
def chat():
    print("\n🤖 Chatbot is ready! Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break
        label = model.predict([query])[0]
        possible_responses = responses.get(label)
        if possible_responses:
            print("Bot:", random.choice(possible_responses))
        else:
            print("Bot: I'm not sure how to answer that.")

# Start chatting
chat()