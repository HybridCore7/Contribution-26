# Fractal Art Generation with Recursion in Python

# Learning Objective:
# This tutorial will guide you through generating beautiful fractal art using
# the power of recursion and fundamental mathematical principles in Python.
# We will focus on the concept of recursive drawing, where a function calls
# itself to create intricate, self-similar patterns.

import turtle
import random

# --- Configuration ---
# These constants control the appearance and behavior of our fractal.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
INITIAL_PEN_SIZE = 3
INITIAL_PEN_COLOR = "blue"
MAX_RECURSION_DEPTH = 10 # Controls how many times the drawing can repeat.
                          # Higher values create more detail but take longer.
LENGTH_DECAY_FACTOR = 0.7 # How much the line length shrinks with each recursion.
                          # A value between 0 and 1.

# --- Fractal Drawing Function ---
def draw_fractal(artist, length, level, angle_range):
    """
    Recursively draws a fractal pattern.

    Args:
        artist (turtle.Turtle): The turtle object used for drawing.
        length (float): The current length of the line segment to draw.
        level (int): The current recursion depth.
        angle_range (tuple): A tuple (min_angle, max_angle) representing the
                             range of random angles to turn.
    """
    # Base Case: If we've reached the maximum recursion depth, stop drawing.
    # This is crucial for preventing infinite recursion and ensuring the
    # program terminates.
    if level >= MAX_RECURSION_DEPTH:
        return

    # --- Drawing the current segment ---
    # Set the pen size based on the recursion level. Thicker lines at the
    # start, thinner lines as we go deeper for a more visually appealing effect.
    artist.pensize(max(1, INITIAL_PEN_SIZE - level // 2))

    # Randomly choose a color for each segment to add visual variety.
    # We're using RGB tuples for more control over color.
    r = random.random()
    g = random.random()
    b = random.random()
    artist.pencolor((r, g, b))

    # Move the turtle forward by the current length. This draws a line.
    artist.forward(length)

    # --- Recursive Calls: Creating the branches/sub-patterns ---
    # For each level, we create multiple "branches" or sub-patterns.
    # The number of branches and their angles are key to the fractal's shape.

    # Store the current position and heading so we can return to it
    # after drawing a sub-pattern. This is essential for branching.
    current_pos = artist.pos()
    current_heading = artist.heading()

    # Determine the number of branches for this level.
    # We can make this more dynamic, but for simplicity, let's use a fixed
    # number or a small random variation.
    num_branches = random.randint(2, 4)

    # Calculate the angle increment to distribute branches evenly.
    # We'll spread the branches across a range, not a full circle.
    angle_spread = angle_range[1] - angle_range[0]
    angle_increment = angle_spread / (num_branches - 1) if num_branches > 1 else 0

    # Calculate the starting angle for branching.
    start_angle = angle_range[0]

    # Loop to create each branch.
    for i in range(num_branches):
        # Calculate the angle for this specific branch.
        branch_angle = start_angle + i * angle_increment

        # Randomly perturb the angle slightly within the specified range.
        # This adds organic variation to the fractal.
        random_angle_offset = random.uniform(-angle_range[0] * 0.2, angle_range[0] * 0.2)
        final_branch_angle = branch_angle + random_angle_offset

        # Rotate the turtle to the calculated branch angle.
        # We need to save the current heading first, then turn.
        artist.left(final_branch_angle)

        # Recursively call draw_fractal for the new branch.
        # - The length is reduced by the decay factor.
        # - The recursion level is increased by 1.
        # - The angle range is slightly narrowed to keep patterns focused.
        draw_fractal(artist,
                     length * LENGTH_DECAY_FACTOR,
                     level + 1,
                     (angle_range[0] * 0.9, angle_range[1] * 0.9)) # Narrow angle range

        # --- Returning to the branching point ---
        # After a branch is drawn, we need to return the turtle to its
        # original position and orientation at the branching point.
        # This allows us to draw the next branch from the same spot.
        artist.penup() # Lift the pen to avoid drawing while repositioning.
        artist.goto(current_pos) # Move back to the saved position.
        artist.setheading(current_heading) # Restore the original heading.
        artist.pendown() # Put the pen down to continue drawing.

        # Rotate back to the original heading after drawing a branch.
        # This is important if we adjusted the heading for the branch.
        artist.right(final_branch_angle)


# --- Main Execution Block ---
if __name__ == "__main__":
    # 1. Setup the screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black") # Set a dark background for better contrast.
    screen.title("Recursive Fractal Art")
    screen.tracer(0) # Turn off screen updates for faster drawing.

    # 2. Create a turtle object
    artist = turtle.Turtle()
    artist.speed(0) # Set the fastest animation speed.
    artist.penup() # Lift the pen initially to move to the starting position.
    artist.goto(0, -SCREEN_HEIGHT / 2 + 50) # Start near the bottom center.
    artist.left(90) # Point the turtle upwards.
    artist.pendown() # Put the pen down to start drawing.
    artist.color(INITIAL_PEN_COLOR)
    artist.pensize(INITIAL_PEN_SIZE)

    # 3. Start the fractal generation
    # We initiate the recursive drawing process.
    # - Initial length: How long the first line segment is.
    # - Initial level: Start at recursion depth 0.
    # - Initial angle range: The initial spread for branching angles.
    initial_length = 150
    initial_angle_range = (20, 45) # Degrees for the left and right turns.
    draw_fractal(artist, initial_length, 0, initial_angle_range)

    # 4. Finalize drawing
    screen.update() # Update the screen once all drawing is complete.
    screen.mainloop() # Keep the window open until it's manually closed.

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., fractal_art.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python fractal_art.py
#
# You can experiment with:
# - MAX_RECURSION_DEPTH: Increase for more detail, decrease for speed.
# - LENGTH_DECAY_FACTOR: Affects how quickly branches shrink.
# - INITIAL_PEN_SIZE: Starting thickness of lines.
# - INITIAL_PEN_COLOR: Starting color.
# - initial_length and initial_angle_range: Change the overall scale and shape.
# - The logic within the draw_fractal function, especially how num_branches
#   and branch_angle are determined, to create different types of fractals.