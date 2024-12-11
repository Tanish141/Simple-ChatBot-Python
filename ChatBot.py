# Import the regular expression modulr to hsndle pattern
import re

# A dictionary that maps keywords to predefined responses
responses = {
    "hello" : "Hi there! How can I assis you today?",
    "hi" : "Hi there! How can I help you?",
    "how are you" : "I'm just bot, but I'm doing great! How about you?",
    "what is your name" : "I'm a chatbot created to assist you.",
    "help" : "Sure, I'm here to help. What do you need assistance with?",
    "bye" : "Goodbye! Have a great day!",
    "thank you" : "You're welcome! I'm happy to help.",
    "default" : "I'm not sure I understand. Could you please rephrase?"
}

# Function to find the appropriate response based on the user's input
def chatbot_response(user_input):
    user_input = user_input.lower()

    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]
        
    return responses["default"]

# Main function to run the chat bot
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'bye' to exit)")

    while True:
        # Get user input
        user_input = input("You: ")

        # IF user types 'bye', exit the loop
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day !")
            break

        # Get chatbot's response based on user input
        response = chatbot_response(user_input)

        # Print chatbot's response
        print(f"Chatbot: {response}")

# Run the chat bot
chatbot()