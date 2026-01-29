# Pixel Art Editor Tutorial

# Learning Objective:
# This tutorial will teach you the fundamentals of building a simple
# pixel art editor using Python's Tkinter library. You will learn:
# 1. How to create a graphical user interface (GUI) with Tkinter.
# 2. How to handle user events (like mouse clicks).
# 3. How to represent and manipulate a 2D grid of data (our pixel canvas)
#    using Python's 2D lists (lists of lists).
# 4. How to dynamically draw on the canvas based on user interaction.

import tkinter as tk

# --- Configuration ---
GRID_SIZE = 16  # Number of pixels wide and tall
CELL_SIZE = 25  # Size of each pixel in the GUI (in pixels)
DEFAULT_COLOR = "white" # The initial color of all pixels
DRAW_COLOR = "black"    # The color the user will draw with

# --- Main Application Class ---
class PixelArtEditor:
    def __init__(self, master):
        # 'master' is the main Tkinter window.
        self.master = master
        master.title("Simple Pixel Art Editor")

        # --- GUI Setup ---
        # Create a frame to hold the canvas. This helps organize widgets.
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack()

        # Create the Tkinter Canvas widget. This is where we'll draw.
        # We set its width and height based on our grid and cell sizes.
        self.canvas = tk.Canvas(self.canvas_frame,
                                width=GRID_SIZE * CELL_SIZE,
                                height=GRID_SIZE * CELL_SIZE,
                                bg=DEFAULT_COLOR)
        self.canvas.pack()

        # --- Data Representation (2D Array) ---
        # We use a 2D list to represent our pixel grid.
        # Each element in this list will store the color of a pixel.
        # It's a list of rows, and each row is a list of columns.
        # We initialize it with the default color for all pixels.
        self.pixel_grid = [[DEFAULT_COLOR for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # --- Event Binding ---
        # Bind the left mouse button click event (<Button-1>) to the
        # 'handle_click' method. When the user clicks the canvas,
        # this method will be called.
        self.canvas.bind("<Button-1>", self.handle_click)

        # --- Initial Drawing ---
        # Draw the initial grid lines on the canvas so the user can see the pixels.
        self.draw_grid()

    def draw_grid(self):
        # This method draws the grid lines on the Tkinter canvas.
        # It iterates through the canvas width and height at intervals of CELL_SIZE.
        for x in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            # Draw vertical lines
            self.canvas.create_line(x, 0, x, GRID_SIZE * CELL_SIZE, fill="gray")
        for y in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            # Draw horizontal lines
            self.canvas.create_line(0, y, GRID_SIZE * CELL_SIZE, y, fill="gray")

    def handle_click(self, event):
        # This method is called whenever the user clicks on the canvas.
        # 'event' is an object containing information about the click,
        # including the mouse cursor's x and y coordinates.

        # Calculate which grid cell was clicked.
        # We divide the click coordinates by CELL_SIZE and take the integer part.
        # This gives us the row and column index of the clicked pixel.
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        # Ensure the click is within the grid boundaries.
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            # --- Updating the 2D Array ---
            # Change the color of the clicked pixel in our 2D array.
            self.pixel_grid[row][col] = DRAW_COLOR

            # --- Redrawing the Pixel ---
            # Calculate the screen coordinates for the rectangle representing the pixel.
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            # Draw a filled rectangle on the canvas to represent the colored pixel.
            # 'fill' sets the color, 'outline' is the border color.
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=DRAW_COLOR, outline="gray")

# --- Example Usage ---
# This is the standard way to start a Tkinter application.
if __name__ == "__main__":
    # Create the main window object.
    root = tk.Tk()
    # Instantiate our PixelArtEditor class, passing the main window.
    editor = PixelArtEditor(root)
    # Start the Tkinter event loop. This makes the window appear and
    # waits for user interactions (like clicks).
    root.mainloop()