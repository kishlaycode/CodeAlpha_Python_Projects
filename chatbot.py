import random

print("🤖 Welcome to Python Chatbot!")
print("Type 'bye' to exit.\n")

responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "hi": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I am fine!", "I'm doing great!", "What about you?"],
    "what is your name": ["My name is Chat bot.", "You can call me Chat bot!"],
    "who created you": ["I was created using Python."],
    "bye": ["Goodbye!", "See you again!", "Have a nice day!"]
}

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand that yet.")