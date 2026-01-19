# Fractal Art with Recursion: A Python Tutorial

# Learning Objective:
# This tutorial will teach you how to programmatically create and visualize
# stunning fractal art using the power of recursion in Python.
# We will focus on the concept of self-similarity, a key characteristic of fractals.
# By the end, you'll understand how a simple rule, applied repeatedly, can generate
# intricate and beautiful patterns.

# We'll be using the `turtle` module, which is a built-in Python library
# for simple graphics, perfect for visualizing geometric patterns.
import turtle

# --- Fractal Generation Function ---

def draw_fractal(t, order, size, angle):
    """
    Recursively draws a fractal pattern.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        order (int): The current depth of recursion (how many times the rule is applied).
        size (float): The length of the current line segment to draw.
        angle (float): The angle to turn at each branching point.
    """
    # Base Case: When the order reaches 0, we stop recursing and just draw a line.
    # This is crucial to prevent infinite recursion.
    if order == 0:
        t.forward(size)
        return

    # Recursive Step: If the order is greater than 0, we apply the fractal rule.
    # We divide the current line segment into smaller parts and draw them,
    # turning at specific angles. This is where the "self-similarity" comes in.
    # The pattern is composed of smaller, identical versions of itself.

    # Calculate the size of the smaller segments.
    # We divide the current size by a factor (here, 2) for each recursive call.
    new_size = size / 2

    # --- The Fractal Rule (Koch Curve example) ---
    # For this tutorial, we'll implement a simplified Koch curve.
    # The rule is: replace a line segment with four smaller segments.
    # Three segments are straight, and the middle one forms a peak.

    # 1. Draw the first segment (same as the first part of the rule)
    draw_fractal(t, order - 1, new_size, angle)

    # 2. Turn left to prepare for the upward peak
    t.left(angle)
    # Draw the second segment (the upward peak)
    draw_fractal(t, order - 1, new_size, angle)

    # 3. Turn right to come back down and face the original direction
    t.right(angle * 2) # Turn right by twice the angle to account for the left turn
    # Draw the third segment (coming down)
    draw_fractal(t, order - 1, new_size, angle)

    # 4. Turn left again to prepare for the final segment
    t.left(angle)
    # Draw the fourth segment (the final part of the rule)
    draw_fractal(t, order - 1, new_size, angle)


# --- Main Execution Block ---

if __name__ == "__main__":
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black") # A dark background makes fractals pop

    # Create a turtle object
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(0) # Set speed to fastest (0) for quicker drawing
    fractal_turtle.color("cyan") # Choose a vibrant color
    fractal_turtle.penup() # Lift the pen so it doesn't draw while moving to start position
    fractal_turtle.goto(-200, 0) # Move the turtle to a starting position
    fractal_turtle.pendown() # Put the pen down to start drawing

    # --- Example Usage ---
    # Define parameters for the fractal
    # 'order' controls the complexity. Higher order means more detail but longer drawing time.
    # 'initial_size' is the length of the starting line.
    # 'branch_angle' determines the shape of the fractal.
    initial_order = 4
    initial_size = 400
    branch_angle = 60 # For a Koch-like curve, 60 degrees is common

    print(f"Drawing fractal with order: {initial_order}, size: {initial_size}, angle: {branch_angle} degrees.")

    # Call the recursive function to draw the fractal
    draw_fractal(fractal_turtle, initial_order, initial_size, branch_angle)

    # Hide the turtle cursor when done
    fractal_turtle.hideturtle()

    # Keep the window open until it's closed manually
    screen.mainloop()

# How to run this code:
# 1. Save the code as a Python file (e.g., fractal_art.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using: python fractal_art.py
# A new window will appear, and you'll see the fractal being drawn!