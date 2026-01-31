# Fractal Art with Python Turtle: Mastering Recursion

# Learning Objective:
# This tutorial will teach you how to create beautiful fractal art
# using the power of recursion and Python's built-in Turtle graphics module.
# We will focus on understanding how recursive functions can be used
# to generate complex and self-similar patterns.

import turtle

# --- Configuration ---
# Define some constants to make our drawing easily adjustable.
# These control the initial size of our fractal.
INITIAL_LENGTH = 100
# This controls how many times our fractal pattern will repeat itself.
# Higher numbers create more detailed fractals but take longer to draw.
RECURSION_LEVEL = 4
# The speed of the turtle drawing. '0' is the fastest, '1' is slowest,
# and any number between 1 and 10 is progressively faster.
DRAWING_SPEED = 0
# The color palette for our fractal.
COLORS = ["blue", "green", "red", "purple", "orange", "cyan"]

# --- Recursive Fractal Function ---

def draw_fractal(t, length, level):
    """
    Recursively draws a fractal pattern.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        length (float): The current length of the line segment to draw.
        level (int): The current recursion depth.
    """
    # Base Case: When the recursion level reaches 0, we stop drawing.
    # This is crucial to prevent infinite recursion and to define the
    # smallest elements of our fractal.
    if level == 0:
        # Set the pen color based on the current recursion level.
        # We use the modulo operator (%) to cycle through our COLORS list.
        # This creates a visual gradient as the fractal gets smaller.
        t.pencolor(COLORS[level % len(COLORS)])
        # Draw a line segment of the specified length.
        t.forward(length)
        return  # Exit the function for this recursive call.

    # Recursive Step: If level is greater than 0, we perform the fractal's
    # transformation. For this example, we'll create a branching pattern
    # similar to a tree.

    # Set the pen color based on the current recursion level for this branch.
    t.pencolor(COLORS[level % len(COLORS)])

    # The 'length' is divided by a factor (here, 2) for each subsequent level.
    # This ensures that branches get progressively shorter.
    new_length = length / 2

    # 1. Draw the first branch.
    # We make a recursive call with a reduced length and an incremented level.
    draw_fractal(t, new_length, level - 1)

    # 2. Turn left to prepare for the second branch.
    # The angle (here, 45 degrees) determines how the branches spread out.
    t.left(45)

    # 3. Draw the second branch.
    # Another recursive call for the second branch.
    draw_fractal(t, new_length, level - 1)

    # 4. Turn right to return to the original orientation.
    # We turn right by twice the angle we turned left to face the opposite way
    # of the first branch, and then back to the original direction.
    # This "undoes" the previous turns and ensures the turtle is in the
    # correct position and orientation for the parent call.
    t.right(90)

    # 5. Draw the third branch.
    draw_fractal(t, new_length, level - 1)

    # 6. Turn left to return to the original orientation of the parent call.
    # This step is crucial for backtracking. After drawing all sub-fractals
    # from this level, we need to ensure the turtle is facing the same way
    # it was before this function was called, so subsequent branches at the
    # parent level are drawn correctly.
    t.left(45)

    # Note: For other fractal types (like the Koch snowflake or Sierpinski triangle),
    # the specific sequence of drawing, turning, and recursive calls will differ,
    # but the core principle of a base case and recursive steps remains the same.


# --- Main Execution Block ---

if __name__ == "__main__":
    # This block ensures that the code inside it only runs when the script
    # is executed directly (not when imported as a module).

    # Create a screen object for our drawing window.
    screen = turtle.Screen()
    # Set the background color of the drawing window.
    screen.bgcolor("black")

    # Create a turtle object, which is our drawing pen.
    fractal_turtle = turtle.Turtle()
    # Set the drawing speed of the turtle.
    fractal_turtle.speed(DRAWING_SPEED)
    # Hide the turtle icon itself while it's drawing for a cleaner look.
    fractal_turtle.hideturtle()
    # Set the initial thickness of the pen.
    fractal_turtle.pensize(2)

    # --- Positioning the Turtle ---
    # Move the turtle to a starting position where the fractal will be centered.
    # We lift the pen up so it doesn't draw while moving.
    fractal_turtle.penup()
    # Move to the bottom center of the screen.
    fractal_turtle.goto(0, -screen.window_height() / 2 + 50)
    # Put the pen down to start drawing.
    fractal_turtle.pendown()
    # Orient the turtle to face upwards, which is typical for tree-like fractals.
    fractal_turtle.setheading(90)

    # --- Initiate the Fractal Drawing ---
    # Call the recursive function to start drawing the fractal.
    # We pass our turtle object, the initial length, and the desired recursion level.
    print(f"Generating fractal with recursion level {RECURSION_LEVEL}...")
    draw_fractal(fractal_turtle, INITIAL_LENGTH, RECURSION_LEVEL)
    print("Fractal generation complete!")

    # Keep the drawing window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., fractal_art.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python fractal_art.py
#
# You can experiment by changing:
# - INITIAL_LENGTH: Makes the overall fractal bigger or smaller.
# - RECURSION_LEVEL: Controls the detail and complexity.
# - DRAWING_SPEED: Adjust how fast the fractal is drawn.
# - COLORS: Add or remove colors from the palette.
# - The angles in t.left() and t.right(): Change the branching structure.
# - The divisor for 'new_length': Affects how much smaller each branch becomes.