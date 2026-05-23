# AI Chatbot using NLP

## Overview

This project is a simple AI chatbot built using Python and NLP techniques.
The chatbot can understand user queries and respond intelligently using TF-IDF and cosine similarity.

---

## Features

- NLP-based chatbot
- Tokenization
- Lemmatization
- Intent recognition
- TF-IDF vectorization
- Cosine similarity matching
- Conversation logging
- Beginner-friendly code

---

## Technologies Used

- Python
- NLTK
- Scikit-learn

---

## Project Structure

```text
AI_Chatbot/
│
├── chatbot.py
├── intents.json
├── requirements.txt
└── README.md
```

---

## Installation

### Step 1: Clone or Download the Project

Download the project files.

---

### Step 2: Install Dependencies

Open terminal and run:

```bash
pip install -r requirements.txt
```

---

### Step 3: Run the Chatbot

```bash
python chatbot.py
```

---

## Example Conversation

```text
AI Chatbot is running!

You: Hi
Bot: Hello! How can I help you?

You: What is your name?
Bot: I am an NLP chatbot created using Python.

You: Thanks
Bot: You're welcome!

You: bye
Bot: Goodbye!
```

---

## NLP Pipeline Explanation

### 1. Text Preprocessing

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

### 2. TF-IDF Vectorization

TF-IDF converts text into numerical vectors.

It helps the chatbot understand important words in sentences.

---

### 3. Cosine Similarity

Cosine similarity measures similarity between:

- User input
- Stored intent patterns

The chatbot selects the most similar response.

---

## Logging

All conversations are saved in:

```text
chat_log.txt
```

---

## Future Improvements

- GUI using Tkinter
- Voice assistant support
- Deep learning model
- Database integration
- Web deployment using Flask

---

## Author

Created using Python and NLP.