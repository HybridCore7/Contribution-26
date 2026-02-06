# Learning Objective:
# This tutorial will teach you how to build a simple interactive data
# visualization tool using Python's Matplotlib library. We'll focus on
# creating a scatter plot where users can interactively select points
# to display their exact coordinates. This will introduce basic event
# handling in Matplotlib.

# Import necessary libraries
import matplotlib.pyplot as plt # Used for creating plots and visualizations
import numpy as np              # Used for numerical operations, especially for creating sample data

# --- Data Preparation ---
# Let's create some sample data to visualize.
# In a real-world scenario, you'd load this from a file (CSV, Excel, etc.)
# or fetch it from a database.
np.random.seed(42) # For reproducible random data
num_points = 50
# Generate random x and y coordinates for our scatter plot.
x_data = np.random.rand(num_points) * 10
y_data = np.random.rand(num_points) * 10

# --- Visualization Setup ---

# Create a figure and an axes object.
# A figure is the overall window or page that contains the plot.
# An axes is the actual plotting area within the figure.
fig, ax = plt.subplots()

# Create the scatter plot.
# 's' controls the size of the markers.
# 'c' sets the color of the markers.
# 'alpha' controls the transparency of the markers (0 is fully transparent, 1 is fully opaque).
scatter_plot = ax.scatter(x_data, y_data, s=50, c='blue', alpha=0.7)

# Set labels for the x and y axes.
ax.set_xlabel("X-Axis Label")
ax.set_ylabel("Y-Axis Label")
ax.set_title("Interactive Scatter Plot")

# --- Interactive Event Handling ---

# This is where the magic happens for interactivity!
# We define a function that will be called whenever an event occurs on our plot.
# In this case, we're interested in 'button_press_event'.

def onclick(event):
    # The 'event' object contains information about the event,
    # such as the coordinates where the click occurred.

    # Check if the click occurred within the axes of our plot.
    if event.inaxes != ax:
        return # If not, do nothing and exit the function.

    # Get the x and y coordinates of the click.
    click_x, click_y = event.xdata, event.ydata

    # Find the closest data point to the click.
    # We calculate the distance from the click to all data points.
    distances = np.sqrt((x_data - click_x)**2 + (y_data - click_y)**2)
    # Find the index of the point with the minimum distance.
    closest_point_index = np.argmin(distances)

    # Get the coordinates of the closest data point.
    closest_x = x_data[closest_point_index]
    closest_y = y_data[closest_point_index]

    # Update the visualization to highlight the clicked point.
    # First, reset the colors of all points to their original state.
    scatter_plot.set_color('blue')
    # Then, set the color of the closest point to red.
    scatter_plot.get_offsets()[closest_point_index] = [closest_x, closest_y] # Ensure offset is correct if needed
    scatter_plot.get_facecolors()[closest_point_index] = [1, 0, 0, 1] # Set to red [R, G, B, Alpha]

    # Redraw the canvas to show the updated plot.
    fig.canvas.draw_idle()

    # Print the coordinates of the clicked point to the console.
    print(f"Clicked point coordinates: X={closest_x:.2f}, Y={closest_y:.2f}")

# Connect the 'button_press_event' to our 'onclick' function.
# This tells Matplotlib to call 'onclick' whenever the user presses a mouse button
# while the mouse cursor is over the figure.
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# --- Display the Plot ---
# This command displays the Matplotlib figure window.
# The program will pause here until the figure window is closed.
plt.show()

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., interactive_plot.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using: python interactive_plot.py
#
# Once the plot window appears:
# - Click on any of the blue dots.
# - Observe that the clicked dot turns red, and its coordinates are printed in the terminal.
# - Clicking on another dot will reset the previous one and highlight the new one.
# - You can reconnect to the event handler if needed, though in this simple script, it's already connected.
# - To disconnect, you would use: fig.canvas.mpl_disconnect(cid)