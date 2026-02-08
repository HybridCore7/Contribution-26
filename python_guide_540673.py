# ASCII Art Generator and Manipulator Tutorial

# Learning Objective:
# This script will teach beginners how to generate and manipulate simple ASCII art
# in Python by focusing on character manipulation and basic graphical concepts.
# We'll learn to draw shapes and modify them using loops, conditional statements,
# and string formatting, creating a foundation for more complex graphical
# applications or creative text-based projects.

import os # Import the os module for clearing the screen

def clear_screen():
    # This function clears the terminal screen for a cleaner display.
    # os.name 'nt' is for Windows, 'posix' is for macOS/Linux.
    os.system('cls' if os.name == 'nt' else 'clear')

def create_canvas(width, height, fill_char=' '):
    # This function creates a 2D grid (list of lists) representing our canvas.
    # It's initialized with a specified fill character, defaulting to a space.
    # The canvas is a list of rows, and each row is a list of characters.
    return [[fill_char for _ in range(width)] for _ in range(height)]

def draw_pixel(canvas, x, y, char='*'):
    # This function "draws" a single character (pixel) at a specific coordinate.
    # It takes the canvas, the x (column) and y (row) coordinates, and the character to draw.
    # We check if the coordinates are within the canvas bounds to prevent errors.
    height = len(canvas)
    width = len(canvas[0]) if height > 0 else 0
    if 0 <= y < height and 0 <= x < width:
        canvas[y][x] = char

def draw_rectangle(canvas, x, y, width, height, char='#'):
    # This function draws a filled rectangle on the canvas.
    # It iterates through each row and column within the rectangle's boundaries
    # and uses draw_pixel to place the specified character.
    for row in range(y, y + height):
        for col in range(x, x + width):
            draw_pixel(canvas, col, row, char)

def draw_line_horizontal(canvas, x, y, length, char='-'):
    # This function draws a horizontal line.
    # It simply calls draw_pixel repeatedly for each position along the line.
    for i in range(length):
        draw_pixel(canvas, x + i, y, char)

def draw_line_vertical(canvas, x, y, length, char='|'):
    # This function draws a vertical line.
    # Similar to the horizontal line, it calls draw_pixel for each position.
    for i in range(length):
        draw_pixel(canvas, x, y + i, char)

def print_canvas(canvas):
    # This function prints the entire canvas to the console.
    # It iterates through each row and joins the characters in the row into a string,
    # then prints that string.
    for row in canvas:
        print("".join(row))

# --- Example Usage ---

if __name__ == "__main__":
    # This block runs only when the script is executed directly, not imported.

    canvas_width = 50
    canvas_height = 20
    my_canvas = create_canvas(canvas_width, canvas_height, '.') # Create a canvas filled with '.'

    # Let's draw some shapes!

    # Draw a red rectangle (using '#' character for simplicity)
    draw_rectangle(my_canvas, 5, 3, 15, 7, '#')

    # Draw a blue line (using '-' character)
    draw_line_horizontal(my_canvas, 2, 10, 20, '-')

    # Draw a green line (using '|' character)
    draw_line_vertical(my_canvas, 25, 5, 10, '|')

    # Draw a smaller yellow square (using '*' character)
    draw_rectangle(my_canvas, 30, 12, 5, 5, '*')

    # Draw a single point
    draw_pixel(my_canvas, 40, 18, 'X')

    # Now, let's see our masterpiece!
    clear_screen() # Clear the screen before printing
    print("--- Your ASCII Art ---")
    print_canvas(my_canvas)
    print("----------------------")

    # You can experiment by changing the coordinates, sizes, and characters!
    # For example, try drawing another shape or modifying an existing one.