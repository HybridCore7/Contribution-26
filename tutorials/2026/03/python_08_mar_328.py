# Dijkstra's Shortest Path Algorithm Implementation

import heapq

def dijkstra(graph, start_node):
    """
    Dijkstra's Shortest Path Algorithm Implementation

    Args:
        graph (dict): A dictionary representing the graph where each key is a node
                      and its corresponding value is another dictionary with
                      neighboring nodes as keys and edge weights as values.
        start_node (str): The node to start the search from.

    Returns:
        A dictionary with the shortest distances from the start node to all other nodes.
    """
    # Initialize distances to all nodes as infinity, except for the start node which is 0
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0

    # Initialize the priority queue with the start node
    priority_queue = [(0, start_node)]

    while priority_queue:
        # Extract the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the already known distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor through the current node
            distance = current_distance + weight

            # If this distance is less than the already known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push the neighbor into the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Define a graph as a dictionary
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Find the shortest distances from node 'A' to all other nodes
    shortest_distances = dijkstra(graph, 'A')
    print(shortest_distances)