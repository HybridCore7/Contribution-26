# Python Turtle Graphics: Visualizing and Exploring Fractal Patterns

# Learning Objective:
# This tutorial will teach you how to use Python's Turtle graphics library to
# create and explore simple fractal patterns. We will focus on understanding
# the concept of recursion and how it applies to generating these self-similar
# geometric shapes. By the end of this tutorial, you will be able to:
# 1. Understand the basics of Python's Turtle graphics.
# 2. Grasp the concept of recursion for fractal generation.
# 3. Write Python code to draw a simple fractal (the Sierpinski Triangle).
# 4. Experiment with changing parameters to see how the fractal changes.

import turtle

# --- Setup the Turtle Screen ---
# We need a window to draw on. This sets up the drawing area.
screen = turtle.Screen()
screen.setup(width=800, height=700) # Set the size of the window
screen.bgcolor("black") # Make the background black for better visibility of the drawing
screen.title("Exploring Fractals with Python Turtle") # Set a title for the window

# --- Create a Turtle Object ---
# This is our "pen" that will draw on the screen.
fractal_turtle = turtle.Turtle()
fractal_turtle.speed(0) # Set the speed to the fastest possible (0 means no animation delay)
fractal_turtle.penup() # Lift the pen so it doesn't draw while moving to the starting position
fractal_turtle.hideturtle() # Hide the turtle icon itself for a cleaner look

# --- Core Fractal Logic: The Sierpinski Triangle ---

# Fractals are often defined recursively. This means a function calls itself.
# For the Sierpinski Triangle, we break down the problem into smaller,
# identical sub-problems.

# The 'level' parameter controls the complexity of the fractal.
# A higher level means more detail and more recursive calls.
def draw_sierpinski(turtle_obj, length, level, p1, p2, p3):
    """
    Recursively draws the Sierpinski Triangle.

    Args:
        turtle_obj (turtle.Turtle): The turtle object to use for drawing.
        length (int): The length of the base of the current triangle.
        level (int): The current recursion level.
        p1, p2, p3 (tuple): Coordinates of the three vertices of the current triangle.
    """
    # Base Case: When the recursion level reaches 0, we draw a single filled triangle.
    # This is the smallest, non-divisible unit of our fractal.
    if level == 0:
        turtle_obj.goto(p1)
        turtle_obj.pendown()
        turtle_obj.fillcolor("white") # Set the color for the smallest triangles
        turtle_obj.begin_fill()
        turtle_obj.goto(p2)
        turtle_obj.goto(p3)
        turtle_obj.goto(p1)
        turtle_obj.end_fill()
        turtle_obj.penup()
    else:
        # Recursive Step: If the level is greater than 0, we divide the current
        # triangle into three smaller triangles. We then recursively call
        # draw_sierpinski for each of these smaller triangles.

        # Calculate the midpoints of each side of the current triangle.
        # These midpoints will form the vertices of the three smaller triangles.
        mid_p1_p2 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        mid_p2_p3 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
        mid_p3_p1 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)

        # Recursively call draw_sierpinski for the three smaller triangles.
        # We reduce the level by 1 for each recursive call, bringing us closer to the base case.
        # Each recursive call draws a triangle with vertices at one original vertex
        # and two midpoints.
        draw_sierpinski(turtle_obj, length / 2, level - 1, p1, mid_p1_p2, mid_p3_p1)
        draw_sierpinski(turtle_obj, length / 2, level - 1, p2, mid_p2_p3, mid_p1_p2)
        draw_sierpinski(turtle_obj, length / 2, level - 1, p3, mid_p3_p1, mid_p2_p3)

# --- Example Usage ---

# Define the initial parameters for the Sierpinski Triangle.
# This is the outermost triangle that will be subdivided.
initial_length = 400 # The size of the largest triangle
recursion_level = 4  # How many times to subdivide (adjust for complexity)

# Define the vertices of the initial large triangle.
# These coordinates are relative to the center of the screen (0,0).
# We aim to center the triangle on the screen.
v1 = (-initial_length / 2, -initial_length * (3**0.5) / 4) # Bottom-left
v2 = (initial_length / 2, -initial_length * (3**0.5) / 4)  # Bottom-right
v3 = (0, initial_length * (3**0.5) / 4)                    # Top

# Start the fractal drawing process.
# The first call to draw_sierpinski initiates the recursion.
print(f"Drawing Sierpinski Triangle with level {recursion_level}...")
draw_sierpinski(fractal_turtle, initial_length, recursion_level, v1, v2, v3)
print("Drawing complete!")

# Keep the window open until it's manually closed.
# This is important so you can see the drawing.
screen.mainloop()

# --- How to Experiment ---
# 1. Change `recursion_level`: Try values like 0, 1, 2, 3, 5, 6.
#    - Level 0: Draws a single triangle.
#    - Level 1: Draws 3 smaller triangles.
#    - Higher levels create more intricate patterns.
# 2. Change `initial_length`: This will scale the entire fractal.
# 3. Change `v1`, `v2`, `v3`: You can shift the initial triangle's position
#    or change its orientation. Be careful, as this can affect how it looks.
# 4. Change `fillcolor`: Experiment with different colors for the smallest triangles.
# 5. Explore other fractals: This recursive approach can be adapted to create
#    other fractals like the Koch snowflake or Cantor set.

# For example, to draw a Koch snowflake, you'd define a function that draws
# a line segment, then recursively calls itself to draw three segments
# at the ends and one in the middle with a "bump" in between. The core idea
# of breaking down a problem into smaller, self-similar parts remains the same.