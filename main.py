import spacy
import re

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

# Define responses with dictionary, targeted for students learning OOP
responses = {
    "default" : "I'm sorry, I didn't understand that. Could you rephrase?",
    "help" : "I can answer your questions. Try asking about something more specific!",
    "greet" : "Hello! can I help you?",
    "bye" : "Goodbye! Have a great day!",
    "variables": "Containers for storing data values. In Java, you must declare a variable before using it.", 
    "data types": "Defines the type of data a variable can hold, such as int, float, char, and boolean.", 
    "operators": "Symbols that perform operations on variables and values, such as +, -, *, /, and %.", 
    "loops": "Used to execute a block of code repeatedly, including for, while, and do-while loops.", 
    "arrays": "A collection of elements of the same type, accessed by an index. They can store multiple values in a single variable.", 
    "strings": "A sequence of characters, used to represent text. Strings are immutable in Java.",
    "methods": "Blocks of code that perform a specific task, defined with a name and can take parameters and return a value.", 
    "classes": "Blueprints for creating objects. A class defines properties (attributes) and behaviors (methods).", 
    "objects": "Instances of classes that encapsulate data and methods. They represent real-world entities.", 
    "inheritance": "A mechanism where one class can inherit fields and methods from another class, promoting code reuse.", 
    "polymorphism": "The ability of different classes to be treated as instances of the same class through a common interface.", 
    "encapsulation": "The bundling of data (attributes) and methods that operate on the data into a single unit (class).", 
    "interfaces": "A reference type in Java that can contain only constants, method signatures, default methods, static methods, and nested types.", 
    "abstract classes": "Classes that cannot be instantiated and can contain abstract methods that must be implemented by subclasses.", 
    "exception handling": "A mechanism to handle runtime errors using try, catch, and finally blocks to maintain normal program flow.",
    "if statement": "An 'if statement' in Java is used to evaluate a boolean expression. If the expression is true, the block of code inside the 'if' statement is executed. It allows for conditional execution of code.", 
    "else": "The 'else' statement in Java is used in conjunction with an 'if statement'. It provides an alternative block of code that executes when the 'if' condition evaluates to false.", 
    "logical operators": "Logical operators in Java are used to combine multiple boolean expressions. The main logical operators are '&&' (AND), '||' (OR), and '!' (NOT). They help in making complex conditional statements.", 
    "2d arrays": "A 2D array in Java is an array of arrays, allowing you to store data in a grid-like structure. It is declared using two sets of square brackets, e.g., 'int[][] array = new int[rows][columns];'.", 
    "array lists": "ArrayLists in Java are part of the Java Collections Framework. They are resizable arrays that can grow as needed. Unlike arrays, ArrayLists can store objects and provide methods for adding, removing, and accessing elements.", 
    "break": "The 'break' statement in Java is used to exit a loop or a switch statement prematurely. When 'break' is encountered, the control flow jumps to the statement immediately following the loop or switch.", 
    "math functions": "Java provides a Math class that contains methods for performing basic numeric operations such as exponentiation, logarithms, square roots, and trigonometric functions. For example, 'Math.sqrt()' computes the square root.", 
    "type casting": "Type casting in Java is the process of converting a variable from one data type to another. It can be done explicitly (manual) or implicitly (automatic) depending on the types involved. For example, 'int to double' is an implicit cast.", 
    "scope": "Scope in Java refers to the visibility and lifetime of variables. Variables defined within a method are local to that method, while class-level variables (fields) are accessible throughout the class.",
    "main" : "The main method is the block of code that the program will look for and execute first."
}

# Define keywords to that apply to the appropriate response (for those that apply) from the responses dictionary
keywords = { 
    "help" : {"help", "advice", "question"},
    "greet" : {"hi", "hello", "greetings", "how are you"},
    "bye" : {"bye", "goodbye", "see you", "have a good day"},
    "variables": ["variables", "declaration", "initialization", "variable"], 
    "data types": ["data types", "int", "float", "double", "char", "boolean", "String", "byte", "short", "long"], 
    "operators": ["operators", "operator", "arithmetic", "relational", "bitwise", "assignment", "unary"], 
    "loops": ["loop", "loops", "for", "while", "do while"],
    "arrays": ["arrays", "array", "single-dimensional", "indexing"], 
    "strings": ["string", "strings", "substring", "concat", "equals", "indexOf", "index of"], 
    "methods": ["methods", "parameters", "return type", "recursion"], 
    "classes": ["class", "classes", "definition", "fields", "constructors"], 
    "objects": ["instantiation", "reference", "object", "objects"], 
    "inheritance": ["inheritance", "superclass", "subclass", "extends"], 
    "polymorphism": ["polymorphism", "overloading", "overriding", "dynamic binding"], 
    "encapsulation": ["encapsulation", "getter", "setter", "data hiding"], 
    "interfaces": ["interface", "implementation", "multiple inheritance", "abstract methods"], 
    "abstract classes": ["abstract", "abstract methods"], 
    "exception handling": ["exception", "handling", "try", "catch", "finally", "throw", "throws", "custom exceptions"], 
    "if statement": ["conditional", "true", "false", "nested", "if"], 
    "else": ["alternative block", "else"], 
    "logical operators": ["logical", "logical operator", "and", "or", "not", "&&", "||", "!"], 
    "2d arrays": ["2d", "two-dimensional", "accessing elements", "lengths"], 
    "array lists": ["array list", "dynamic array", "add element", "remove"], 
    "break": ["exit loop", "break", "stop loop"], 
    "math functions": ["math", "abs", "sqrt", "pow", "random", "round"], 
    "type casting": ["casting", "implicit", "explicit", "primitive"], 
    "scope": ["scope", "local", "out of scope"],
    "main": ["main", "start"]
}

# Process User Input with NLP and return appropriate response
def get_response(input):
    response = responses["default"]
    keyIdx = 0
    # Process input with NLP
    statement = nlp(input)
    for token in statement:
        token = token.text.lower()
        # Check if the token matches any keyword for the appropriate response
        for key, value in keywords.items():
            # Prioritize responses higher with higher index in dictionary
            # Ex. "hi bye" will prioritize "bye" since its response comes after "hi"
            if token in value and list(keywords).index(key) >= keyIdx:
                response = responses[key]
                keyIdx = list(keywords).index(key)
    return response

# User Interaction Loop
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