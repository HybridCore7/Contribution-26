# Learning Objective:
# This tutorial will teach you how to create a compelling story
# with your data by animating a matplotlib visualization.
# We will focus on animating a line plot to show the progression
# of a single data series over time, making it easier to
# understand trends and patterns.

# Import necessary libraries
import matplotlib.pyplot as plt  # For plotting
import matplotlib.animation as animation  # For creating animations
import numpy as np  # For numerical operations, especially creating sample data

# --- Configuration ---
# Define parameters for our animation
FPS = 30  # Frames per second - controls the smoothness of the animation
INTERVAL = 1000 / FPS  # Interval between frames in milliseconds

# --- Data Generation (for demonstration purposes) ---
# Let's create some sample data that we can animate.
# Imagine this is data collected over time, like temperature, stock prices, etc.
num_points = 100  # Number of data points in our series
# Create a time axis (x-values) from 0 to num_points-1
x_data = np.arange(num_points)
# Create a y-axis data series with some fluctuations and a general upward trend
# We use a sine wave for some cyclical behavior and add linear growth.
y_data = np.sin(x_data / 10) * 5 + x_data * 0.5 + np.random.randn(num_points) * 10

# --- Animation Setup ---

# Create a figure and an axes object. This is our plotting canvas.
fig, ax = plt.subplots()

# Initialize an empty line object. This is the object we will update in each frame.
# We provide initial empty data so the line is invisible at the start.
line, = ax.plot([], [], 'r-', animated=True) # 'r-' means a red solid line. animated=True is crucial for efficient animation.

# Set plot limits. This ensures the plot doesn't rescale during animation,
# which can be jarring. We set them based on our sample data's expected range.
ax.set_xlim(0, num_points)
ax.set_ylim(y_data.min() - 10, y_data.max() + 10) # Add some padding

# Add labels and title to make the plot understandable
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Animated Data Progression")

# --- Animation Function ---

# This function is called for each frame of the animation.
# It takes the frame number as an argument.
def update(frame_number):
    # We update the data of the line object.
    # For each frame, we take a slice of our x and y data up to the current frame_number.
    # This simulates the data "growing" over time.
    line.set_data(x_data[:frame_number], y_data[:frame_number])
    # The function must return an iterable of the artists that were modified.
    # In this case, it's just our 'line' object.
    return line,

# --- Create the Animation ---

# Use matplotlib's animation module to create the animation.
# fig: the figure to animate.
# update: the function to call each frame.
# frames: the total number of frames to generate. We use num_points as the total frames.
# interval: delay between frames in milliseconds.
# blit: if True, blitting is used to optimize drawing. This means only the parts
#       of the plot that have changed are redrawn, making the animation much faster.
ani = animation.FuncAnimation(fig, update, frames=num_points,
                              interval=INTERVAL, blit=True)

# --- Example Usage ---

if __name__ == "__main__":
    # To display the animation, we use plt.show().
    # This will open a plot window and run the animation.
    # You can also save the animation to a file (e.g., GIF, MP4) using ani.save().
    print("Displaying animation. Close the plot window to exit.")
    plt.show()

    # Example of saving the animation (uncomment to use):
    # print("Saving animation to 'animated_data.gif'...")
    # ani.save('animated_data.gif', writer='imagemagick', fps=FPS)
    # print("Animation saved!")