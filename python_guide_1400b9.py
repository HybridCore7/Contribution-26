# Fractal Generation Tutorial: The Sierpinski Triangle

# Learning Objective:
# This tutorial demonstrates how to generate intricate fractal patterns
# using the power of recursion and graphical plotting in Python.
# We will focus on creating the famous Sierpinski Triangle as a
# practical example to understand the core concepts.

# --- What are Fractals? ---
# Fractals are self-similar patterns, meaning they exhibit the same
# structure at different scales. Zooming into a fractal reveals
# smaller copies of the overall pattern.

# --- What is Recursion? ---
# Recursion is a programming technique where a function calls itself
# to solve smaller instances of the same problem. It's like a set
# of Russian nesting dolls, where each doll contains a smaller version
# of itself.

# We need a library to draw shapes. The 'matplotlib' library is
# excellent for plotting. If you don't have it, install it with:
# pip install matplotlib
import matplotlib.pyplot as plt

# --- The Sierpinski Triangle Logic ---
# The Sierpinski Triangle can be generated recursively by starting
# with a single equilateral triangle. Then, at each step, we find the
# midpoints of each side and connect them to form a new, smaller
# inverted triangle in the center. This process is repeated for the
# three remaining smaller triangles.

# We'll represent our triangle by its three corner points (vertices).
# Each point will be a tuple (x, y).

def sierpinski_triangle(points, depth):
    """
    Recursively generates the points for a Sierpinski Triangle.

    Args:
        points: A list of three tuples, representing the (x, y) coordinates
                of the initial triangle's vertices.
        depth: The current level of recursion. This controls how many
               times the subdivision process is repeated.
    """

    # Base Case: When the recursion depth reaches 0, we've finished
    # subdividing. We return the current set of points, which will
    # eventually be drawn.
    if depth == 0:
        return points

    # Recursive Step: If depth is greater than 0, we need to subdivide.
    # 1. Calculate the midpoints of each side of the current triangle.
    #    The midpoint between two points (x1, y1) and (x2, y2) is
    #    ((x1+x2)/2, (y1+y2)/2).

    # Midpoint between point 0 and point 1
    mid1 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
    # Midpoint between point 1 and point 2
    mid2 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
    # Midpoint between point 2 and point 0
    mid3 = ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)

    # 2. Recursively call sierpinski_triangle for the three smaller
    #    triangles. Each recursive call uses one of the original vertices
    #    and two of the newly calculated midpoints.
    #    We decrease the depth by 1 in each recursive call.

    # First smaller triangle: uses original point 0 and midpoints 1 and 3
    tri1_points = sierpinski_triangle([points[0], mid1, mid3], depth - 1)
    # Second smaller triangle: uses original point 1 and midpoints 1 and 2
    tri2_points = sierpinski_triangle([points[1], mid1, mid2], depth - 1)
    # Third smaller triangle: uses original point 2 and midpoints 3 and 2
    tri3_points = sierpinski_triangle([points[2], mid3, mid2], depth - 1)

    # 3. Combine the results from the recursive calls.
    #    We're essentially collecting all the triangle points generated
    #    at the deepest level of recursion.
    return tri1_points + tri2_points + tri3_points

# --- Plotting the Fractal ---

def plot_fractal(points_list):
    """
    Plots the generated fractal points.

    Args:
        points_list: A list of points, where each point is a tuple (x, y).
    """
    # Extract x and y coordinates into separate lists for plotting.
    x_coords = [p[0] for p in points_list]
    y_coords = [p[1] for p in points_list]

    # Create a figure and an axes object for plotting.
    fig, ax = plt.subplots()

    # Scatter plot the points. 'o' specifies circular markers.
    ax.scatter(x_coords, y_coords, s=2, c='blue') # s is size, c is color

    # Set the aspect ratio to 'equal' so triangles don't look distorted.
    ax.set_aspect('equal', adjustable='box')

    # Hide the axes ticks and labels for a cleaner fractal look.
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Set a title for the plot.
    ax.set_title("Sierpinski Triangle")

    # Display the plot.
    plt.show()

# --- Example Usage ---
if __name__ == "__main__":
    # Define the initial vertices of the main triangle.
    # This triangle will be equilateral.
    initial_points = [(0, 0), (1, 0), (0.5, 0.866)] # Approx. sqrt(3)/2 for height

    # Set the desired recursion depth.
    # Higher depth means more intricate detail and more points.
    # Be mindful of performance with very high depths (e.g., > 10).
    recursion_depth = 6

    print(f"Generating Sierpinski Triangle with depth {recursion_depth}...")

    # Generate all the points for the Sierpinski Triangle.
    fractal_points = sierpinski_triangle(initial_points, recursion_depth)

    print(f"Generated {len(fractal_points)} points. Plotting...")

    # Plot the generated fractal.
    plot_fractal(fractal_points)

    print("Tutorial finished. You can experiment with different recursion_depth!")
# End of code tutorial.