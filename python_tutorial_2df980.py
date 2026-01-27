# Pixel Art Generator Tutorial

# Learning Objective:
# This tutorial will teach you how to generate simple pixel art in Python
# using user-defined color palettes and dimensions. We will focus on:
# 1. Representing pixel art data structures.
# 2. Iterating through a grid to set pixel colors.
# 3. Using a simple visualization library (Pillow) to display the art.

# Import the Pillow library for image manipulation.
# Pillow (PIL Fork) is a powerful image processing library for Python.
# We'll use it here to create and save an image file.
from PIL import Image

# --- Configuration ---

# Define the dimensions of our pixel art canvas.
# These represent the width and height of our grid in pixels.
CANVAS_WIDTH = 32
CANVAS_HEIGHT = 32

# Define a sample color palette.
# Colors are represented as RGB tuples (Red, Green, Blue).
# Each value ranges from 0 to 255.
# This is a simple example, but you could create much larger and complex palettes.
COLOR_PALETTE = {
    "background": (255, 255, 255),  # White
    "foreground": (0, 0, 0),      # Black
    "red": (255, 0, 0),          # Red
    "blue": (0, 0, 255),         # Blue
    "green": (0, 255, 0)         # Green
}

# --- Core Logic ---

def create_pixel_art(width: int, height: int, palette: dict) -> list:
    """
    Generates a 2D list representing pixel art.

    This function initializes a grid of pixels with a default color
    (usually the background color from the palette).
    It then demonstrates a simple pattern generation.

    Args:
        width: The desired width of the pixel art in pixels.
        height: The desired height of the pixel art in pixels.
        palette: A dictionary mapping color names to RGB tuples.

    Returns:
        A 2D list (list of lists) where each inner list represents a row
        and each element is an RGB tuple representing a pixel's color.
    """
    # Get the background color from the palette.
    # We use .get() for safety in case 'background' isn't defined.
    background_color = palette.get("background", (255, 255, 255))

    # Initialize the pixel grid.
    # This is a list of lists. The outer list represents rows, and the inner
    # lists represent columns within each row.
    # Initially, all pixels are set to the background color.
    pixel_grid = [[background_color for _ in range(width)] for _ in range(height)]

    # --- Example Pattern Generation ---
    # This section demonstrates how to change pixel colors based on logic.
    # You can replace this with your own creative patterns!

    # Let's draw a simple diagonal line.
    foreground_color = palette.get("foreground", (0, 0, 0))
    for i in range(min(width, height)):
        # We check if i is within the bounds of the grid to avoid errors.
        if i < height and i < width:
            pixel_grid[i][i] = foreground_color

    # Let's add some colored squares.
    red_color = palette.get("red", (255, 0, 0))
    blue_color = palette.get("blue", (0, 0, 255))

    # Draw a red square in the top-left.
    for y in range(5):
        for x in range(5):
            if y < height and x < width:
                pixel_grid[y][x] = red_color

    # Draw a blue square in the bottom-right.
    # We use the dimensions to calculate the starting point for the bottom-right square.
    square_size = 5
    for y in range(height - square_size, height):
        for x in range(width - square_size, width):
            if y < height and x < width: # Ensure we don't go out of bounds
                pixel_grid[y][x] = blue_color

    return pixel_grid

def save_pixel_art(pixel_grid: list, filename: str = "pixel_art.png"):
    """
    Saves the generated pixel art to an image file.

    This function takes the 2D pixel grid and uses Pillow to create an
    image object and save it.

    Args:
        pixel_grid: A 2D list of RGB tuples representing the pixel art.
        filename: The name of the file to save the image as.
    """
    # Get the dimensions from the pixel_grid.
    # The height is the number of rows (outer list length).
    height = len(pixel_grid)
    # The width is the number of columns in the first row (inner list length).
    # We assume all rows have the same length.
    width = len(pixel_grid[0]) if height > 0 else 0

    # Create a new Image object with RGB mode.
    # 'RGB' specifies that the image will use 3 color channels (Red, Green, Blue).
    img = Image.new('RGB', (width, height))

    # Load the pixel data into the image.
    # img.putdata() takes a sequence of pixel values and fills the image.
    # We need to flatten our 2D list into a single list of pixel tuples.
    img.putdata([pixel for row in pixel_grid for pixel in row])

    # Save the image to a file.
    # The format is automatically determined from the filename extension (e.g., .png).
    img.save(filename)
    print(f"Pixel art saved to {filename}")

# --- Example Usage ---

if __name__ == "__main__":
    # This block runs only when the script is executed directly (not imported).
    print("Generating pixel art...")

    # Create the pixel art grid using our defined dimensions and palette.
    my_pixel_art = create_pixel_art(CANVAS_WIDTH, CANVAS_HEIGHT, COLOR_PALETTE)

    # Save the generated pixel art to a PNG file.
    save_pixel_art(my_pixel_art, "my_first_pixel_art.png")

    # --- Another Example with a different palette and dimensions ---
    print("\nGenerating another piece of pixel art...")

    # Define a new, smaller color palette.
    small_palette = {
        "background": (220, 220, 220),  # Light grey
        "accent": (255, 165, 0)         # Orange
    }

    # Create pixel art with different dimensions.
    # Here, we'll create a very simple pattern for demonstration.
    small_width = 16
    small_height = 16
    small_art_grid = [[small_palette["background"] for _ in range(small_width)] for _ in range(small_height)]

    # Draw a simple "smiley" face.
    orange_color = small_palette["accent"]
    for y in range(small_height):
        for x in range(small_width):
            # Top half of the face (circle shape approximation)
            if 3 <= y < 12 and 3 <= x < 13:
                # Basic circle logic (distance from center)
                center_x = small_width / 2
                center_y = small_height / 2
                distance_squared = (x - center_x)**2 + (y - center_y)**2
                if distance_squared < (5**2): # Radius of 5
                    small_art_grid[y][x] = orange_color

            # Eyes
            if y == 6 and (x == 6 or x == 9):
                small_art_grid[y][x] = (0,0,0) # Black eyes
            if y == 7 and (x == 6 or x == 9):
                small_art_grid[y][x] = (0,0,0) # Black eyes

    save_pixel_art(small_art_grid, "smiley_face.png")