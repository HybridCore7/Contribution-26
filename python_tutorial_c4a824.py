"""
Learning Objective:
This tutorial will guide you through creating a simple text-based adventure game
in Python. The primary focus is on teaching two fundamental programming concepts:
1. State Management: How to keep track of information that changes throughout
   your program (e.g., player's location, inventory, game progress).
2. Conditional Logic: How to make decisions in your program based on specific
   conditions (e.g., if the player has a key, if they are in a certain room).

By building this game, you'll see these concepts in action in a fun and
interactive way.
"""

# --- Game State ---
# We'll use a dictionary to manage the game's state.
# This dictionary will hold all the information that can change as the player
# progresses through the game.
game_state = {
    "current_location": "forest",  # The player's starting location
    "has_key": False,             # A boolean flag to track if the player has the key
    "met_hermit": False           # A flag to track if the player has spoken to the hermit
}

# --- Game Locations ---
# A dictionary to define each location in our game.
# Each location has a description and possible exits (which lead to other locations).
locations = {
    "forest": {
        "description": "You are in a dark, spooky forest. A narrow path leads east.",
        "exits": {"east": "clearing"}
    },
    "clearing": {
        "description": "You are in a small, sunlit clearing. To the west is the forest. To the north, you see a small hut.",
        "exits": {"west": "forest", "north": "hut"}
    },
    "hut": {
        "description": "You are inside a cozy hut. An old hermit is sitting by the fire. There's a locked chest in the corner. The only way out is south.",
        "exits": {"south": "clearing"}
    }
}

# --- Game Functions ---

def display_location(state):
    """
    Displays the description of the player's current location.
    This function uses the 'current_location' from the game_state.
    """
    current_loc = state["current_location"] # Get the player's current location from state
    print(locations[current_loc]["description"]) # Print the description for that location

def move_player(direction, state):
    """
    Attempts to move the player in the given direction.
    This function updates the 'current_location' in the game_state.
    """
    current_loc_data = locations[state["current_location"]] # Get data for the current location

    # Conditional logic: Check if the chosen direction is a valid exit
    if direction in current_loc_data["exits"]:
        new_location = current_loc_data["exits"][direction] # Get the name of the next location
        state["current_location"] = new_location          # Update the player's location in the state
        print(f"\nYou move {direction}.")
        display_location(state)                           # Show the description of the new location
    else:
        print("\nYou can't go that way.") # Inform the player if the move is invalid

def interact(command, state):
    """
    Handles player interactions based on commands.
    This function uses conditional logic extensively to react to player actions.
    """
    current_loc = state["current_location"] # Get the current location

    if command == "look":
        display_location(state) # Just show the description again

    elif command == "talk" and current_loc == "hut":
        # Conditional logic: Check if the player has already met the hermit
        if not state["met_hermit"]:
            print("\nThe hermit looks up and says, 'Ah, a traveler! I might have something for you if you can help me.'")
            print("He tells you he lost his lucky charm in the forest. Perhaps you can find it?")
            state["met_hermit"] = True # Update the state to reflect meeting the hermit
        else:
            print("\nThe hermit smiles warmly. 'Still looking for that charm?'")

    elif command == "take key" and current_loc == "forest":
        # Conditional logic: Check if the player already has the key
        if not state["has_key"]:
            print("\nYou found a shiny, old key!")
            state["has_key"] = True # Update the state to indicate the player has the key
        else:
            print("\nYou already have the key.")

    elif command == "open chest" and current_loc == "hut":
        # Conditional logic: Check if the player has the key
        if state["has_key"]:
            print("\nWith a click, the chest opens! Inside, you find a loaf of bread and a map.")
            print("Congratulations! You've found a treasure!")
            # In a real game, you'd likely end the game here or give the player items.
        else:
            print("\nThe chest is locked. You need a key.")

    else:
        print("\nI don't understand that command.")

# --- Game Loop ---
def play_game():
    """
    The main game loop. It continuously prompts the player for input
    and processes their commands.
    """
    print("Welcome to the Text Adventure!")
    display_location(game_state) # Show the starting location

    while True: # An infinite loop that will run until explicitly broken
        command = input("\nWhat do you want to do? (e.g., 'go east', 'look', 'take key', 'open chest', 'talk', 'quit'): ").lower().strip()

        # Conditional logic to handle the 'quit' command
        if command == "quit":
            print("Thanks for playing!")
            break # Exit the while loop, ending the game

        # Split the command to handle directional moves like "go east"
        parts = command.split()
        if len(parts) > 1 and parts[0] == "go":
            move_player(parts[1], game_state) # Call move_player if it's a directional command
        else:
            interact(command, game_state) # Otherwise, try to interact

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that play_game() is only called when this script is
    # run directly (not when imported as a module).
    play_game()