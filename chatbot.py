"""
CodeAlpha Python Programming Internship - Task 4
Basic Rule-Based Chatbot

A simple chatbot that responds to predefined user inputs
(greetings, small talk, farewells) using if-elif matching.
"""

import random

GREETING_INPUTS = ["hello", "hi", "hey", "hola"]
GREETING_RESPONSES = ["Hi!", "Hello there!", "Hey! How can I help?"]

FAREWELL_INPUTS = ["bye", "goodbye", "see you", "exit", "quit"]
FAREWELL_RESPONSES = ["Goodbye!", "See you later!", "Bye! Take care."]

THANKS_INPUTS = ["thanks", "thank you", "thx"]
THANKS_RESPONSES = ["You're welcome!", "Anytime!", "No problem!"]


def get_response(user_input):
    text = user_input.lower().strip()

    if any(word in text for word in GREETING_INPUTS):
        return random.choice(GREETING_RESPONSES)
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text:
        return "I'm a simple CodeAlpha chatbot!"
    elif any(word in text for word in THANKS_INPUTS):
        return random.choice(THANKS_RESPONSES)
    elif any(word in text for word in FAREWELL_INPUTS):
        return random.choice(FAREWELL_RESPONSES)
    else:
        return "Sorry, I don't understand that yet. Try saying 'hello' or 'bye'."


def chat():
    print("=" * 40)
    print("Simple Chatbot (type 'bye' to exit)")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print(f"Bot: {response}")

        if any(word in user_input.lower() for word in FAREWELL_INPUTS):
            break


if __name__ == "__main__":
    chat()
