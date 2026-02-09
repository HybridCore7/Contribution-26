# Breadth-First Search (BFS) Graph Traversal

# Importing necessary modules
from collections import deque

# Defining a function for BFS traversal
def bfs(graph, root):
    """
    Performs Breadth-First Search traversal on a graph starting from the given root node.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    root (node): Root node to start the traversal from.
    
    Returns:
    list: List of nodes in the order they are visited.
    """
    # Create a queue to hold nodes to be visited, and add the root node
    queue = deque([root])
    
    # Create a set to store visited nodes
    visited = set()
    
    # Create a list to store the order of visited nodes
    order = []
    
    # While there are still nodes to be visited
    while queue:
        # Dequeue the next node
        node = queue.popleft()
        
        # If the node has not been visited before
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            
            # Add the node to the order list
            order.append(node)
            
            # Add all unvisited neighbors of the node to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    # Return the list of visited nodes
    return order

# Example usage
# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Find the order of nodes in the graph
root_node = 'A'  # Node to start the traversal from
order = bfs(graph, root_node)
print("Order of nodes:", order)