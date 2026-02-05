# Learning Objective:
# This tutorial will guide you through building a simple text-based adventure game engine in Python.
# We will focus on using dictionaries to represent game data (like rooms and items) and
# conditional logic (if-elif-else statements) to handle player actions and game state changes.
# This will provide a practical understanding of these fundamental programming concepts.

# --- Game Data Structure ---

# We'll use a dictionary to store all the information about our game world.
# Each key in this dictionary will represent a 'room' in the game.
# The value associated with each room key will be another dictionary, containing details about that room.
# This nested dictionary structure is a powerful way to organize complex data.
game_world = {
    # 'start_room' is the key for our initial location.
    'start_room': {
        # 'description' is a string that tells the player what they see.
        'description': "You are in a dimly lit room. There's a door to the north.",
        # 'exits' is another dictionary mapping directions (keys) to room names (values).
        # This defines where the player can go from this room.
        'exits': {'north': 'hallway'},
        # 'items' is a list of items present in this room.
        'items': ['key']
    },
    # 'hallway' is another room.
    'hallway': {
        'description': "You are in a long, narrow hallway. There's a door to the south and another to the east.",
        'exits': {'south': 'start_room', 'east': 'treasure_room'},
        'items': [] # This room has no items initially.
    },
    # 'treasure_room' is a special room.
    'treasure_room': {
        'description': "You've entered a room filled with glittering treasure! You win!",
        'exits': {'west': 'hallway'},
        'items': ['gold coin']
    }
}

# --- Game State Variables ---

# This variable keeps track of the player's current location in the game_world.
current_room = 'start_room'

# This list will store items the player is carrying.
inventory = []

# This variable acts as a flag to determine if the game is still running.
game_over = False

# --- Game Engine Logic ---

def display_room_info():
    """
    Prints the description of the current room and lists any visible items and available exits.
    This function helps keep our main game loop cleaner.
    """
    print("\n" + "="*20) # Separator for better readability
    print(f"You are in: {current_room.replace('_', ' ').title()}") # Make room names look nice
    print(game_world[current_room]['description'])

    # Check if there are any items in the current room and display them.
    if game_world[current_room]['items']:
        print("You see:", ", ".join(game_world[current_room]['items'])) # Use join for neat item listing

    # Check if there are any exits from the current room and display them.
    exits = game_world[current_room]['exits']
    if exits:
        print("Exits:", ", ".join(exits.keys())) # Display directions available

def process_command(command):
    """
    Processes the player's input command and updates the game state accordingly.
    This is where our conditional logic shines!
    """
    global current_room # We need to modify the global current_room variable
    global inventory # We need to modify the global inventory variable
    global game_over # We need to modify the global game_over variable

    # Split the command into words to easily identify the verb and object.
    # Example: "go north" -> ['go', 'north'], "take key" -> ['take', 'key']
    command_parts = command.lower().split()

    # If the command is empty, do nothing.
    if not command_parts:
        return

    # The first word is usually the action (verb).
    verb = command_parts[0]

    # --- Conditional Logic for Player Actions ---

    if verb == 'go':
        # The second word is usually the direction.
        if len(command_parts) > 1:
            direction = command_parts[1]
            # Check if the desired direction is a valid exit from the current room.
            if direction in game_world[current_room]['exits']:
                # Update the player's current room to the new room.
                current_room = game_world[current_room]['exits'][direction]
                # After moving, the new room's info will be displayed by the main loop.
            else:
                print("You can't go that way.")
        else:
            print("Go where?") # Player needs to specify a direction.

    elif verb == 'take':
        # The second word is usually the item to take.
        if len(command_parts) > 1:
            item_to_take = command_parts[1]
            # Check if the item is present in the current room.
            if item_to_take in game_world[current_room]['items']:
                # Add the item to the player's inventory.
                inventory.append(item_to_take)
                # Remove the item from the current room's item list.
                game_world[current_room]['items'].remove(item_to_take)
                print(f"You took the {item_to_take}.")
            else:
                print(f"There is no {item_to_take} here.")
        else:
            print("Take what?") # Player needs to specify an item.

    elif verb == 'inventory':
        # Display the player's current inventory.
        if inventory:
            print("Inventory:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")

    elif verb == 'quit':
        # Set game_over to True to end the game loop.
        game_over = True
        print("Thanks for playing!")

    else:
        # Handle unrecognized commands.
        print("I don't understand that command. Try 'go', 'take', 'inventory', or 'quit'.")

    # --- Special Win Condition ---
    # We can add a win condition by checking the current room.
    if current_room == 'treasure_room':
        print("\n" + "="*20)
        print(game_world[current_room]['description'])
        game_over = True # End the game upon reaching the treasure room.

# --- Main Game Loop ---

print("Welcome to the Simple Adventure Game!")
print("Type 'go [direction]', 'take [item]', 'inventory', or 'quit'.")

# The game loop continues as long as game_over is False.
while not game_over:
    # Display information about the current location.
    display_room_info()

    # Get input from the player.
    player_input = input("> ").strip() # .strip() removes leading/trailing whitespace.

    # Process the player's command.
    process_command(player_input)

# --- Example Usage ---
# To run this game:
# 1. Save the code as a Python file (e.g., adventure_game.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using: python adventure_game.py

# --- Learning Points Recap ---
# Dictionaries: Used to represent the game world (rooms, exits, items) and room details.
# Conditional Logic (if-elif-else): Crucial for determining player actions, valid moves, and game outcomes.
# Global Variables: Used to share and modify game state (current_room, inventory, game_over) across functions.
# Functions: Help organize code and make it more readable and reusable (display_room_info, process_command).
# Lists: Used to store items in rooms and in the player's inventory.
# String Methods: .lower(), .split(), .join(), .strip() are useful for handling text input and output.