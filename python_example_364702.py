# Learning Objective:
# This tutorial teaches you how to implement Dijkstra's algorithm in Python
# to find the shortest path for an AI character in a simple 2D grid-based game.
# We'll cover graph representation, priority queues, and the core Dijkstra logic.

import heapq # For efficient priority queue implementation

# --- Game Setup ---

# Represents the game map as a 2D grid.
# '0' is a traversable path, '1' is an obstacle.
GAME_MAP = [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# --- Dijkstra's Algorithm Implementation ---

def dijkstra(graph, start, end):
    """
    Finds the shortest path from 'start' to 'end' in a 'graph' using Dijkstra's algorithm.

    Args:
        graph: A 2D list representing the grid. 0 is traversable, 1 is an obstacle.
        start: A tuple (row, col) representing the starting position.
        end: A tuple (row, col) representing the ending position.

    Returns:
        A list of tuples representing the shortest path, or None if no path exists.
    """

    rows, cols = len(graph), len(graph[0])

    # 'distances': Stores the shortest distance found so far from 'start' to each node.
    # Initialize all distances to infinity, except for the start node (0).
    distances = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
    distances[start] = 0

    # 'previous_nodes': Stores the predecessor of each node in the shortest path found so far.
    # Used to reconstruct the path later.
    previous_nodes = {}

    # 'priority_queue': A min-heap to store nodes to visit, ordered by their current shortest distance.
    # Stores tuples of (distance, (row, col)). heapq prioritizes the first element.
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest distance from the priority queue.
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we've already found a shorter path to this node, skip it.
        if current_distance > distances[current_node]:
            continue

        # If we've reached the end node, we can reconstruct the path.
        if current_node == end:
            path = []
            while current_node in previous_nodes:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start) # Add the start node
            return path[::-1] # Return the path in correct order

        # Explore neighbors of the current node.
        row, col = current_node
        # Define possible moves (up, down, left, right).
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for neighbor_row, neighbor_col in neighbors:
            # Check if the neighbor is within the grid boundaries.
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                neighbor_node = (neighbor_row, neighbor_col)
                # Check if the neighbor is not an obstacle.
                if graph[neighbor_row][neighbor_col] == 0:
                    # The 'cost' to move to a neighbor is 1 in a grid.
                    # Calculate the new distance from the start to this neighbor.
                    new_distance = current_distance + 1

                    # If this new path to the neighbor is shorter than any previously found path:
                    if new_distance < distances[neighbor_node]:
                        distances[neighbor_node] = new_distance # Update shortest distance
                        previous_nodes[neighbor_node] = current_node # Record predecessor for path reconstruction
                        # Add the neighbor to the priority queue to be explored.
                        heapq.heappush(priority_queue, (new_distance, neighbor_node))

    # If the loop finishes and the end node hasn't been reached, no path exists.
    return None

# --- Example Usage ---

if __name__ == "__main__":
    # Define player and AI positions.
    player_position = (6, 6)
    ai_position = (0, 0)

    print(f"Finding path from {ai_position} to {player_position}...")
    shortest_path = dijkstra(GAME_MAP, ai_position, player_position)

    if shortest_path:
        print("Shortest path found:")
        print(shortest_path)

        # Optional: Visualize the path on the map
        path_map = [list(row) for row in GAME_MAP] # Create a copy to modify
        for r, c in shortest_path:
            if (r, c) != ai_position and (r, c) != player_position:
                path_map[r][c] = '*' # Mark path with '*'

        print("\nMap with path:")
        for row in path_map:
            print(' '.join(map(str, row)))
    else:
        print("No path found.")