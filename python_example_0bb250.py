# Tutorial: Generating Fractal Art with Recursive Functions in Python

# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal art
# using Python. We will focus on the concept of recursion, a powerful
# programming technique where a function calls itself to solve a problem.
# By understanding recursion and basic graphical rendering, you can
# create intricate and self-similar patterns like the Koch snowflake.

# We'll use the 'turtle' module for graphical rendering, which is
# built into Python and is excellent for beginners learning graphics.

import turtle

# --- Global Configuration ---
# These variables control the appearance and behavior of our fractal.
# Using global variables is acceptable here for simplicity in a tutorial.

SCREEN_WIDTH = 800  # The width of our drawing window.
SCREEN_HEIGHT = 800 # The height of our drawing window.
PEN_SPEED = 0       # The speed of the turtle's drawing (0 is fastest).
BACKGROUND_COLOR = "black" # The color of the drawing background.
PEN_COLOR = "cyan"       # The color of the line drawn by the turtle.
INITIAL_LENGTH = 300     # The initial length of the lines in our fractal.
RECURSION_LEVEL = 3     # The depth of recursion, controlling complexity.

# --- Fractal Generation Function (Recursive) ---

def koch_snowflake_segment(t, length, level):
    """
    This function recursively draws a single segment of the Koch snowflake.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        length (float): The current length of the line segment to draw.
        level (int): The current recursion level. This determines how
                     many times we apply the Koch curve rule.
    """

    # BASE CASE: If the recursion level reaches 0, we've gone deep enough.
    # At this point, we simply draw a straight line of the given length.
    # This is crucial to stop the recursion from running infinitely.
    if level == 0:
        t.forward(length)
        return # Exit the function, stopping further recursion for this branch.

    # RECURSIVE STEP: If the recursion level is greater than 0, we apply
    # the Koch curve rule. The Koch curve is made of 4 smaller, similar
    # segments. Each segment is 1/3 the length of the parent segment.

    # Calculate the length of the smaller segments.
    new_length = length / 3.0

    # 1. Draw the first segment.
    koch_snowflake_segment(t, new_length, level - 1)

    # 2. Turn left by 60 degrees and draw the second segment.
    t.left(60)
    koch_snowflake_segment(t, new_length, level - 1)

    # 3. Turn right by 120 degrees (60 + 60) and draw the third segment.
    # Turning right is the opposite of turning left.
    t.right(120)
    koch_snowflake_segment(t, new_length, level - 1)

    # 4. Turn left by 60 degrees and draw the fourth segment.
    t.left(60)
    koch_snowflake_segment(t, new_length, level - 1)

    # After drawing all four segments, we are back at the starting orientation
    # of this particular segment, which is important for the next part of the fractal.
    # If we didn't adjust our orientation, the fractal would be skewed.
    # We effectively "undo" the turns by adding the opposite turns.
    t.right(120) # Undo the last left(60) and right(120) combination.
    t.forward(new_length) # Move back to the original starting point of the segment.
    t.left(60) # Return to the original orientation before the first recursive call.

# --- Setup and Main Execution ---

def setup_screen():
    """
    Sets up the turtle screen and the turtle pen.
    This function initializes our drawing environment.
    """
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT) # Set the window dimensions.
    screen.bgcolor(BACKGROUND_COLOR)        # Set the background color.
    screen.title("Recursive Fractal Art: Koch Snowflake") # Set the window title.
    return screen

def setup_turtle():
    """
    Sets up the turtle pen with desired properties.
    This function configures how the turtle will draw.
    """
    t = turtle.Turtle()
    t.speed(PEN_SPEED)           # Set the drawing speed.
    t.color(PEN_COLOR)           # Set the pen color.
    t.penup()                    # Lift the pen so it doesn't draw while moving to start.
    # Position the turtle to start drawing the fractal from the center-left.
    # This helps ensure the entire fractal fits within the screen.
    t.goto(-INITIAL_LENGTH / 2, INITIAL_LENGTH / 2)
    t.pendown()                  # Put the pen down to start drawing.
    return t

def draw_koch_snowflake(t, length, level):
    """
    Draws the complete Koch snowflake by calling the segment function three times.
    A snowflake is made of three identical Koch curves forming an equilateral triangle.
    """
    # The Koch snowflake is formed by three sides of an equilateral triangle.
    for _ in range(3):
        koch_snowflake_segment(t, length, level)
        # After drawing one side, turn to draw the next side of the triangle.
        t.right(120)

# --- Example Usage ---

if __name__ == "__main__":
    # This block of code runs only when the script is executed directly
    # (not when imported as a module). This is a standard Python best practice.

    print("Generating Koch Snowflake...")

    # 1. Set up the drawing environment.
    screen = setup_screen()

    # 2. Set up the drawing tool (the turtle).
    my_turtle = setup_turtle()

    # 3. Draw the fractal!
    draw_koch_snowflake(my_turtle, INITIAL_LENGTH, RECURSION_LEVEL)

    # 4. Hide the turtle icon after drawing is complete.
    # This makes the final artwork look cleaner.
    my_turtle.hideturtle()

    # 5. Keep the window open until it's manually closed by the user.
    # This is essential to see the generated artwork.
    screen.mainloop()

    print("Fractal generation complete. Close the window to exit.")