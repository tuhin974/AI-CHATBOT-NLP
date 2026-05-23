# AI Chatbot using NLP

A Python-based AI chatbot built using Natural Language Processing (NLP) techniques such as tokenization, lemmatization, TF-IDF vectorization, and cosine similarity.

---

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TUHIN ROY

*INTERN ID*: CTIS05SQ

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# Features

- NLP-based chatbot
- Tokenization
- Lemmatization
- Intent recognition
- TF-IDF vectorization
- Cosine similarity matching
- Conversation logging
- Beginner-friendly code
- JSON-based intent dataset
- Command-line chatbot interface

---

# Technologies Used

- Python
- NLTK
- Scikit-learn
- TF-IDF
- Cosine Similarity

---

# Project Structure

```text
AI-CHATBOT-NLP/
│
├── chatbot.py
├── intents.json
├── requirements.txt
├── README.md
└── chat_log.txt
```

---

# Installation and Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/tuhin974/AI-CHATBOT-NLP.git
```

---

## Step 2: Open Project Folder

```bash
cd AI-CHATBOT-NLP
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Run the Chatbot

```bash
python chatbot.py
```

---

# Example Conversation

```text
AI Chatbot is running!
Type 'exit', 'quit', or 'bye' to stop.

You: hello
Bot: Hi there!

You: how are you
Bot: I am doing great!

You: what is your name
Bot: I am an NLP chatbot created using Python.

You: thanks
Bot: You're welcome!

You: bye
Bot: Goodbye!
```

---

# NLP Pipeline Explanation

## 1. Text Preprocessing

The chatbot preprocesses user input using:

- Lowercasing
- Removing punctuation
- Tokenization
- Lemmatization

Example:

```text
"Running!" → "running"
```

---

## 2. TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical vectors.

This helps the chatbot understand the importance of words in a sentence.

---

## 3. Cosine Similarity

Cosine similarity measures similarity between:

- User input
- Stored intent patterns

The chatbot selects the most similar intent and returns a relevant response.

---

# Logging System

All chatbot conversations are automatically stored in:

```text
chat_log.txt
```

This helps track interactions and debug chatbot behavior.

---

# Intents Dataset

The chatbot uses a JSON-based intents dataset:

```text
intents.json
```

Each intent contains:

- Tag
- Patterns
- Responses

Example:

```json
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello"],
  "responses": ["Hello!", "Hi there!"]
}
```

---

# Future Improvements

- GUI using Tkinter
- Voice assistant integration
- Flask web deployment
- Deep learning-based chatbot
- Database integration
- spaCy NLP support
- Speech recognition
- AI API integration

---

# Screenshots

(Add your chatbot screenshot here)

Example:

```markdown
![Chatbot Screenshot](screenshot.png)
```

---

# Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Required libraries:

- nltk
- scikit-learn

---

# Internship Project

This project was developed as part of an internship program at CodTech IT Solutions.

---

# Author

Developed by Tuhin Roy using Python and NLP.

---

# License

This project is licensed under the MIT License.
