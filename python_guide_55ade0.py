# Learning Objective:
# This tutorial will teach you how to procedurally generate visually stunning fractal art
# using the concept of recursion in Python. We'll focus on creating a simple
# but effective fractal pattern, the Sierpinski Triangle, to illustrate the power
# of recursive functions in generating complex geometry.

import turtle

# --- Configuration ---
# Define global constants for easy modification of our fractal's appearance.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = "black"
PEN_COLOR = "white"
INITIAL_PEN_SIZE = 2
RECURSION_LEVELS = 5 # Controls the complexity of the fractal. Higher means more detail.
INITIAL_SIZE = 300  # The side length of our initial triangle.

# --- Fractal Generation Function ---
def draw_sierpinski(turtle_obj, level, size):
    """
    Recursively draws a Sierpinski Triangle.

    Args:
        turtle_obj (turtle.Turtle): The turtle object to draw with.
        level (int): The current recursion depth.
        size (float): The side length of the current triangle to draw.
    """
    # BASE CASE: If the recursion level reaches 0, we stop drawing.
    # This is crucial to prevent infinite recursion.
    if level == 0:
        return

    # Recursive Step: Divide the current triangle into three smaller triangles
    # and recursively call draw_sierpinski on each.

    # 1. Draw the current triangle. This forms the larger structure
    #    at each recursive step before we subdivide.
    for _ in range(3):
        turtle_obj.forward(size)
        turtle_obj.left(120)

    # 2. Calculate the size of the smaller triangles.
    #    Each smaller triangle's side is half the size of the current one.
    smaller_size = size / 2

    # 3. Recursively draw the bottom-left smaller triangle.
    #    We move the turtle to the starting position of this smaller triangle.
    #    The turtle is already at the start of the main triangle.
    #    We move forward 'smaller_size' to position for the next sub-triangle.
    draw_sierpinski(turtle_obj, level - 1, smaller_size) # Move to the next level

    # 4. Recursively draw the bottom-right smaller triangle.
    #    To draw the bottom-right triangle, we need to move the turtle.
    #    From the end of the first smaller triangle, we move backward by 'smaller_size'
    #    and then turn left 60 degrees to face the starting point of the next
    #    smaller triangle.
    turtle_obj.backward(smaller_size)
    turtle_obj.right(60)
    turtle_obj.forward(smaller_size)
    turtle_obj.left(120)
    draw_sierpinski(turtle_obj, level - 1, smaller_size) # Move to the next level

    # 5. Recursively draw the top smaller triangle.
    #    To draw the top triangle, we need to reposition again.
    #    From the end of the second smaller triangle, we move backward by 'smaller_size',
    #    turn right 120 degrees, move forward 'smaller_size', and then turn left 120 degrees.
    #    This places the turtle at the correct orientation and position to start the top triangle.
    turtle_obj.left(60)
    turtle_obj.backward(smaller_size)
    turtle_obj.right(120)
    turtle_obj.forward(smaller_size)
    turtle_obj.left(120)
    draw_sierpinski(turtle_obj, level - 1, smaller_size) # Move to the next level

    # After drawing the three smaller triangles, we need to return the turtle
    # to its original position and orientation for the parent call.
    # This is a crucial part of maintaining the correct state in recursion.
    # We move back to the position it was before calling itself.
    turtle_obj.right(120)
    turtle_obj.forward(size)
    turtle_obj.left(120)

# --- Setup and Execution ---
def main():
    # Create a screen object. This is the window where our drawing will appear.
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Recursive Sierpinski Triangle Fractal")

    # Create a turtle object. This is our drawing "pen".
    artist = turtle.Turtle()
    artist.speed(0)  # Set the fastest drawing speed.
    artist.color(PEN_COLOR)
    artist.pensize(INITIAL_PEN_SIZE)
    artist.hideturtle() # Hide the turtle icon for a cleaner final image.

    # Position the turtle to start drawing the fractal.
    # We move it down and to the left to center the base of the triangle.
    artist.penup() # Lift the pen so we don't draw while moving.
    artist.goto(-INITIAL_SIZE / 2, -INITIAL_SIZE / 2)
    artist.pendown() # Put the pen down to start drawing.

    # Start the recursive drawing process.
    # We call our fractal function with the initial level and size.
    draw_sierpinski(artist, RECURSION_LEVELS, INITIAL_SIZE)

    # Keep the window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that 'main()' is called only when the script
    # is executed directly (not when imported as a module).
    main()