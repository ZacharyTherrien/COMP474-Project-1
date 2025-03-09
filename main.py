import spacy

#Load NLP Model
nlp = spacy.load("en_core_web_sm")

#Define responses with dictionary, targeted for students learning OOP
reponses = {
    "default" : "I'm sorry, I didn't understand that. Could you rephrase?",
    "greet" : "Hello! can I help you?",
    "bye" : "Goodbye! Have a great day!",
    "help" : "I can answer your questions. Try asking about something more specific!",
    "if statement" : "An if statement in Java...",
    "loop" : "A loop is used for..."
}

#Process User Input with NLP
def get_response(response):
    return ""

#User Interaction Loop
def chat():
    print("Chatbot: Hello! Enter your question for help or 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            break
        response = get_response(user_input)
        print("Chatbot: ", response)
    print("Chatbot: Goodbye!")

if __name__ == "__main__":
    chat()