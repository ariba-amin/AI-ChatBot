def get_response(user_input):

    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "salam", "assalam o alaikum"]:
        return "Hello! 👋 How can I help you?"

    # Chatbot Introduction
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a Rule-Based AI Chatbot created using Python. 🤖"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! 😊 Thanks for asking."

    # Project Explanation
    elif (
        "tell me about this project" in user_input
        or "explain this project" in user_input
        or "what is this project" in user_input
        or "project details" in user_input
        or "about this project" in user_input
    ):
        return """
This project is a Rule-Based AI Chatbot developed as part of the DecodeLabs Artificial Intelligence internship.

The main purpose of this project is to demonstrate basic Artificial Intelligence concepts using predefined rules and decision-making logic.

The chatbot is developed in Python and uses if-elif-else conditions to understand specific user inputs and provide appropriate responses. It does not use Machine Learning or Deep Learning. Instead, the responses are manually defined according to different questions and commands.

The chatbot can handle greetings such as Hi, Hello, and Hey. It can also answer predefined questions about Artificial Intelligence, Machine Learning, Deep Learning, Python, Data Science, Neural Networks, Computer Vision, NLP, databases, programming, and other technical concepts.

The chatbot also supports exit commands such as Bye, Exit, Quit, and Goodbye.

The project works continuously using a while loop. It takes input from the user, converts the input to lowercase, removes unnecessary spaces, checks the input against predefined conditions, and then returns the appropriate response.

The project also includes a Streamlit frontend. The Streamlit interface provides a simple and interactive chat-based web interface where users can enter questions and view chatbot responses.

The chatbot logic is kept separately in the chatbot.py file, while app.py handles the Streamlit frontend.

The main technologies used in this project are Python and Streamlit.

Overall, this project demonstrates fundamental AI concepts such as rule-based decision making, control flow, conditional statements, user interaction, and continuous program execution. It provides a foundation for understanding how more advanced AI systems can be developed in the future.
"""

    # Artificial Intelligence
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return "Artificial Intelligence (AI) is a technology that enables machines to perform tasks that normally require human intelligence, such as learning, reasoning, and decision-making."

    # Machine Learning
    elif "what is machine learning" in user_input or "define machine learning" in user_input:
        return "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task."

    # Deep Learning
    elif "what is deep learning" in user_input:
        return "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns."

    # Neural Network
    elif "what is neural network" in user_input or "what are neural networks" in user_input:
        return "A Neural Network is a computing model inspired by the human brain. It uses interconnected neurons to process information and learn patterns."

    # Python
    elif "what is python" in user_input:
        return "Python is a high-level programming language widely used in AI, Machine Learning, Data Science, automation, and web development."

    # Programming
    elif "what is programming" in user_input:
        return "Programming is the process of writing instructions that tell a computer how to perform specific tasks."

    # Computer
    elif "what is a computer" in user_input or "define computer" in user_input:
        return "A computer is an electronic device that processes data, performs calculations, stores information, and produces output."

    # Internet
    elif "what is internet" in user_input or "define internet" in user_input:
        return "The Internet is a worldwide network of interconnected computers and devices that communicate and share information."

    # Data Science
    elif "what is data science" in user_input:
        return "Data Science is a field that uses statistics, programming, and machine learning to analyze data and discover useful patterns."

    # Data
    elif "what is data" in user_input:
        return "Data is a collection of facts, values, observations, or information that can be processed and analyzed."

    # Algorithm
    elif "what is algorithm" in user_input:
        return "An algorithm is a step-by-step set of instructions used to solve a problem or complete a specific task."

    # Dataset
    elif "what is dataset" in user_input or "what is a dataset" in user_input:
        return "A dataset is a structured collection of data used for analysis, research, or training Machine Learning models."

    # Supervised Learning
    elif "what is supervised learning" in user_input:
        return "Supervised Learning is a type of Machine Learning where a model learns from labeled data to make predictions."

    # Unsupervised Learning
    elif "what is unsupervised learning" in user_input:
        return "Unsupervised Learning is a type of Machine Learning where a model finds patterns or groups in data without predefined labels."

    # Classification
    elif "what is classification" in user_input:
        return "Classification is a Machine Learning task that assigns data to predefined categories or classes."

    # Regression
    elif "what is regression" in user_input:
        return "Regression is a Machine Learning technique used to predict continuous numerical values, such as house prices."

    # Computer Vision
    elif "what is computer vision" in user_input:
        return "Computer Vision is a field of AI that enables computers to understand and interpret images and videos."

    # NLP
    elif "what is nlp" in user_input or "what is natural language processing" in user_input:
        return "Natural Language Processing (NLP) is a branch of AI that enables computers to understand and process human language."

    # Chatbot
    elif "what is chatbot" in user_input or "what is a chatbot" in user_input:
        return "A chatbot is a software application that communicates with users through text or voice."

    # Database
    elif "what is database" in user_input:
        return "A database is an organized collection of information that can be stored, managed, and retrieved efficiently."

    # SQL
    elif "what is sql" in user_input:
        return "SQL stands for Structured Query Language. It is used to manage and retrieve data from relational databases."

    # HTML
    elif "what is html" in user_input:
        return "HTML stands for HyperText Markup Language. It is used to structure content on web pages."

    # CSS
    elif "what is css" in user_input:
        return "CSS stands for Cascading Style Sheets. It is used to control the appearance and layout of web pages."

    # API
    elif "what is api" in user_input:
        return "API stands for Application Programming Interface. It allows different software applications to communicate with each other."

    # Accuracy
    elif "what is accuracy" in user_input:
        return "Accuracy measures the proportion of correct predictions made by a classification model."

    # Training Data
    elif "what is training data" in user_input:
        return "Training data is the portion of a dataset used to teach a Machine Learning model."

    # Testing Data
    elif "what is testing data" in user_input:
        return "Testing data is used to evaluate how well a trained Machine Learning model performs on unseen data."

    # Thank You
    elif "thank" in user_input:
        return "You're welcome! 😊"

    # Exit Commands
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! 👋 Have a great day!"

    # Unknown Question
    else:
        return "Sorry, I don't know the answer to that yet. Try asking me about AI, Machine Learning, Python, Programming, or Data Science."


# Continuous Chatbot Loop
if __name__ == "__main__":

    print("🤖 Rule-Based AI Chatbot")
    print("Ask me about AI, Machine Learning, Python, Programming, and more.")
    print("Type 'bye', 'exit', or 'quit' to stop.")
    print()

    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
            break