# Skincare Assistant Chatbot

This is a simple skincare assistant chatbot built with Flask, integrating Gemini 2.0 AI for natural language responses. The chatbot uses a user-friendly interface to answer skincare-related queries.

## Features

- **Flask Backend**: A simple Flask app handles user input and interacts with Gemini 2.0 for AI-generated responses.
- **Gemini AI Integration**: Uses Google's Gemini 2.0 Flash API for generating natural language responses based on user input.
- **Frontend UI**: The chatbot interface is built with HTML, CSS, and JavaScript, designed to be user-friendly and responsive.

## Requirements

Before running this application, you need to have the following installed on your system:

- Python 3.8+
- Flask
- Requests
- Python-dotenv

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/skincare-assistant-chatbot.git
cd skincare-assistant-chatbot



### 2. Install Dependencies
Create a virtual environment and install the required dependencies:


python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
If requirements.txt doesn't exist yet, you can manually install the necessary packages:

pip install Flask requests python-dotenv

### 3. Set Up API Key
Create a .env file in the root directory of the project and add your Gemini API key:


GEMINI_API_KEY=your-api-key-here
Replace your-api-key-here with your actual Gemini API key.

### 4. Run the Application
Run the Flask app:

python app.py
The app will start on http://127.0.0.1:5000/ by default.

### 5. Access the Chatbot
Open a browser and navigate to http://127.0.0.1:5000/. You'll be able to interact with the chatbot and get skincare advice powered by Gemini AI.

Folder Structure
skincare-assistant-chatbot/
├── app.py                # Main Flask app file
├── .env                  # Environment variables (Gemini API key)
├── templates/
│   └── index.html        # Frontend chatbot HTML
├── static/
│   └── style.css         # CSS file for chatbot styling
├── requirements.txt      # Python dependencies
└── README.md             # This file
Troubleshooting
"Something went wrong" error: Ensure that your Gemini API key is correctly set in the .env file.

Flask issues: If you encounter issues with Flask, ensure you're running the app in the correct virtual environment with all dependencies installed.