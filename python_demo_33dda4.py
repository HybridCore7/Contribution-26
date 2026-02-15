# Objective:
# This tutorial will teach you how to build a simple text-based chatbot in Python
# that learns from your interactions. We'll use a dictionary to store and recall
# information, demonstrating the basic concept of a chatbot with a memory.

# --- Chatbot Core Components ---

# A dictionary to act as the chatbot's "memory."
# Keys will be user inputs (questions or statements).
# Values will be the chatbot's learned responses.
# We'll initialize it with a few common greetings and questions.
chatbot_memory = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "how are you": "I'm just a program, but I'm functioning well! How about you?",
    "what is your name": "I am a simple chatbot. You can call me ChatBot.",
    "what can you do": "I can learn from our conversations and respond based on what I've learned.",
    "bye": "Goodbye! Come back soon!",
    "thanks": "You're welcome! Glad I could help."
}

# Function to get a response from the chatbot.
def get_chatbot_response(user_input):
    # Convert user input to lowercase to make matching case-insensitive.
    # This is important for consistent learning and recall.
    processed_input = user_input.lower()

    # Check if the processed input is already in our memory.
    if processed_input in chatbot_memory:
        # If it is, return the stored response.
        return chatbot_memory[processed_input]
    else:
        # If the input is new, we need to learn a response.
        # This is where the "learning" happens.
        # We ask the user what they expect as a response.
        print("I don't know how to respond to that yet. What should I say?")
        # Get the new response from the user.
        new_response = input("Your response: ")

        # Store the new input and its learned response in our memory.
        # This is the core of our simple learning mechanism.
        chatbot_memory[processed_input] = new_response

        # Inform the user that we've learned something new.
        return "Thanks! I've learned a new response for that."

# --- Main Chatbot Loop ---

# This function runs the main interaction loop for the chatbot.
def run_chatbot():
    print("Welcome to the learning chatbot! Type 'quit' to exit.")
    print("-" * 30) # A simple separator for better readability

    while True:
        # Get input from the user.
        user_message = input("You: ")

        # Check if the user wants to quit.
        if user_message.lower() == 'quit':
            print("ChatBot: Goodbye! Come back soon!")
            break # Exit the while loop.

        # Get a response from the chatbot's learning function.
        bot_response = get_chatbot_response(user_message)

        # Print the chatbot's response.
        print(f"ChatBot: {bot_response}")
        print("-" * 30) # Another separator for clarity.

# --- Example Usage ---

# To start the chatbot, we call the run_chatbot() function.
# This will begin the interactive conversation.
# You can type messages, and the chatbot will respond and learn.

if __name__ == "__main__":
    run_chatbot()

# --- Explanation of Concepts ---
# 1. Dictionary (chatbot_memory):
#    - This is the heart of our chatbot's memory.
#    - Dictionaries store data in key-value pairs.
#    - Here, a user's input (like "hello") is the key, and the chatbot's
#      pre-programmed or learned response (like "Hi there!") is the value.
#    - This allows for quick lookups: if the user says "hello", the chatbot
#      can instantly find "Hi there!" using the "hello" key.

# 2. Learning Mechanism (in get_chatbot_response):
#    - When the chatbot encounters a new user input it doesn't recognize,
#      it doesn't just say "I don't understand."
#    - Instead, it ASKS the user for a response.
#    - This user-provided response is then stored in the `chatbot_memory`
#      dictionary with the new user input as the key.
#    - This way, the next time the user says the same thing, the chatbot
#      will have a learned response ready.

# 3. Case-Insensitivity (user_input.lower()):
#    - We convert all user inputs to lowercase before checking them against
#      our memory. This means "Hello", "hello", and "HELLO" will all be
#      treated the same. This is crucial for effective learning, as we
#      don't want to store separate entries for different capitalizations
#      of the same phrase.

# 4. Infinite Loop (while True):
#    - The `while True` loop keeps the chatbot running indefinitely until
#      the user explicitly types 'quit'. This is a common pattern for
#      interactive programs.

# 5. User Input/Output (input() and print()):
#    - `input()` is used to get text from the user.
#    - `print()` is used to display text from the chatbot to the user.

# This simple example demonstrates a fundamental AI concept: learning from data.
# While this is very basic, it lays the groundwork for understanding how more
# complex AI systems can store and retrieve information to interact more intelligently.