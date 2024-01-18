import random

def simple_chatbot(user_input):
    greetings = ["hello", "hi", "hey", "howdy", "hola"]
    farewells = ["goodbye", "bye", "see you", "take care"]

    user_input = user_input.lower()

    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you?"
    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing well. How about you?"
    elif "name" in user_input:
        return "My name is Debasis Sahoo."
    elif "highest qualification" in user_input or "degree" in user_input:
        return "My highest qualification is B.Tech in Computer Science and Engineering."
    elif "about me" in user_input or "who am i" in user_input:
        return "You are you! What can I assist you with today?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

if __name__ == "__main__":
    print("Simple Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Simple Chatbot: Goodbye! Have a nice day.")
            break

        response = simple_chatbot(user_input)
        print("Simple Chatbot:", response)
