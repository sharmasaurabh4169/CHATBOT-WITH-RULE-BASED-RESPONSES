def chatbot_response(user_input):
    # Normalize input
    user_input = user_input.lower().strip()

    # Basic greeting responses
    if any(greet in user_input for greet in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']):
        return "Hello! How can I help you today?"

    # Simple question about chatbot's name
    if 'your name' in user_input:
        return "I'm ChatBot, your friendly assistant."

    # Asking about wellbeing
    if any(phrase in user_input for phrase in ['how are you', 'how do you feel', 'are you okay']):
        return "I'm just a program, but thanks for asking!"

    # Asking for help or assistance
    if any(phrase in user_input for phrase in ['help', 'support', 'assist me', 'can you help']):
        return "Sure! What do you need help with?"

    # Asking about time or date
    if 'time' in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S')
        return f"The current time is {current_time}."

    if 'date' in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime('%Y-%m-%d')
        return f"Today's date is {current_date}."

    # Simple farewell
    if any(farewell in user_input for farewell in ['bye', 'see you', 'goodbye', 'exit', 'quit']):
        return "Goodbye! Have a great day."

    # Catch-all fallback response
    return "Sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("ChatBot: Hi! I'm here to chat with you. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("ChatBot: Goodbye! Talk to you later.")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == '__main__':
    main()
