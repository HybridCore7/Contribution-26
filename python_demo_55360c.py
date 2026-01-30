# Learning Objective:
# This tutorial will teach you how to build a simple text-based adventure game
# in Python that uses an AI model (simulated here) to generate dynamic story content.
# We will focus on the core concept of integrating external "intelligence"
# to create more engaging and unpredictable game experiences.

# --- Game Setup ---

# We'll use a placeholder function to simulate AI story generation.
# In a real application, this would involve calling an actual AI API
# (e.g., OpenAI's GPT, Google's Gemini).
# For now, it just returns a predefined response based on the input.
def get_ai_story_segment(player_input, current_story_context):
    """
    Simulates AI-powered story generation.
    In a real game, this function would send player_input and current_story_context
    to an AI model and return its generated text.

    Args:
        player_input (str): The player's action or decision.
        current_story_context (str): The current state of the story.

    Returns:
        str: A dynamically generated story segment.
    """
    # This is a very basic simulation. A real AI would be much more complex.
    if "look around" in player_input.lower():
        return "The room is dimly lit, with cobwebs hanging from the ceiling. You see a sturdy wooden door to your north and a rusty lever on the wall."
    elif "go north" in player_input.lower() or "open door" in player_input.lower():
        return "You push open the heavy wooden door, revealing a dark, dusty corridor. A faint scratching sound echoes from within."
    elif "pull lever" in player_input.lower():
        return "With a groan, the lever moves. A hidden panel slides open, revealing a shimmering, ethereal object."
    else:
        return "The AI ponders your action... and nothing seems to happen immediately. What do you do next?"

# --- Game State ---

# This variable will hold the current narrative.
# It's crucial for the AI to understand where the story is.
current_story = "You awaken in a damp, cold chamber. The air is thick with the smell of mildew. You can feel rough stone beneath your hands. What do you do?"

# --- Game Loop ---

def play_game():
    """
    The main game loop that drives the adventure.
    It continuously prompts the player for input, processes it,
    and updates the story using the AI.
    """
    print("Welcome to the AI Adventure!\n")
    print(current_story) # Print the initial story.

    while True: # An infinite loop until the player decides to quit.
        player_command = input("\n> ").strip() # Get player input and remove whitespace.

        if player_command.lower() == "quit": # Check for the quit command.
            print("Farewell, adventurer!")
            break # Exit the loop and end the game.

        # This is where the AI integration happens.
        # We pass the player's command and the current story context to the AI.
        new_story_segment = get_ai_story_segment(player_command, current_story)

        # Update the main story with the AI's generated content.
        current_story = new_story_segment
        print(current_story) # Display the updated story to the player.

# --- Example Usage ---

# This block ensures that the play_game() function is called only when
# the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    play_game()

# To play: Run this script and type commands like "look around", "go north", "pull lever", or "quit".
# Notice how the story changes based on your input and the simulated AI's response.