
def chatbot_response(user_input):
    user_input = user_input.lower()

    
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! Nice to meet you."

    
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking."

    
    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple Python rule-based chatbot."

    
    elif user_input == "help":
        return ("You can try asking:\n"
                "- hello\n"
                "- how are you\n"
                "- what is your name\n"
                "- what can you do\n"
                "- bye")

    
    elif user_input in ["what can you do", "your features"]:
        return "I can answer basic questions and demonstrate a rule-based chatbot using Python."

    
    elif user_input == "time":
        from datetime import datetime
        return "Current time is: " + datetime.now().strftime("%H:%M:%S")

    
    elif user_input == "date":
        from datetime import datetime
        return "Today's date is: " + datetime.now().strftime("%Y-%m-%d")


    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what you can ask."


def run_chatbot():
    print("===================================")
    print("     Python Internship Chatbot     ")
    print("===================================")
    print("Chatbot: Hello! I am your assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


# Run chatbot
run_chatbot()