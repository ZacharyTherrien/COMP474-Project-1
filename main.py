import spacy

#Load NLP Model
nlp = spacy.load("en_core_web_sm")

#Define responses with dictionary, targeted for students learning OOP
responses = {
    "default" : "I'm sorry, I didn't understand that. Could you rephrase?",
    "greet" : "Hello! can I help you?",
    "bye" : "Goodbye! Have a great day!",
    "help" : "I can answer your questions. Try asking about something more specific!",
    "if statement" : "An if statement in Java...",
    "loop" : "A loop is used for..."
}

keywords = {
    "greet" : {"hi", "hello", "greetings", "how are you"},
    "bye" : {"bye", "goodbye", "see you", "have a good day"}
}

#Process User Input with NLP
def get_response(input):
    #Process user input with NLP model
    statement = nlp(input)
    response = responses["greet"]
    for token in statement:
        k = token.text.lower()
        for key, value in keywords.items():
            if k in value:
                response = responses[key]
                return response
    
    # for token in statement:
    #     key = token.text.lower()
    #     if key in responses:
    #         response = responses[key]
    #     else:
    #         response = responses["default"]
    return response

#User Interaction Loop
def chat():
    print("Chatbot: Hello! Enter your question for help or 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot: ", response)
        if response == responses["bye"]:
            break

if __name__ == "__main__":
    chat()