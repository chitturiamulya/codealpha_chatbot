def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I didn't understand that. 🤔"

def run_chatbot():
    print("🤖 Simple Chatbot is online! Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        reply = chatbot_response(user_input)
        print("Bot:", reply)

        if "bye" in user_input.lower():
            break

run_chatbot()