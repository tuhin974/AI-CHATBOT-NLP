import json
import random
import string
import logging

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK data
import nltk

resources = ['punkt', 'punkt_tab', 'wordnet']

for resource in resources:
    nltk.download(resource)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Configure logging
logging.basicConfig(
    filename='chat_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Load intents
with open('intents.json', 'r') as file:
    data = json.load(file)

patterns = []
tags = []
responses = {}

# Extract patterns and responses
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

    responses[intent['tag']] = intent['responses']


# Text preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    # Tokenization
    tokens = word_tokenize(text)

    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)


# Preprocess all patterns
processed_patterns = [preprocess_text(pattern) for pattern in patterns]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Convert text into vectors
X = vectorizer.fit_transform(processed_patterns)


# Chatbot response function
def chatbot_response(user_input):
    processed_input = preprocess_text(user_input)

    # Convert input into vector
    input_vector = vectorizer.transform([processed_input])

    # Calculate cosine similarity
    similarity = cosine_similarity(input_vector, X)

    # Find best match
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    # Threshold for unknown queries
    if best_score < 0.3:
        return "Sorry, I don't understand that."

    tag = tags[best_match_index]

    return random.choice(responses[tag])


# Main chatbot loop
print("AI Chatbot is running!")
print("Type 'exit', 'quit', or 'bye' to stop.\n")

while True:
    user_input = input("You: ")

    logging.info(f"User: {user_input}")

    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye!")
        logging.info("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)

    print("Bot:", response)

    logging.info(f"Bot: {response}")