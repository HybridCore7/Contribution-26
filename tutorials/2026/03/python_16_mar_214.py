# Breadth First Search Graph Traversal in Python
=============================================

This script demonstrates the implementation of Breadth First Search (BFS) algorithm on a graph. BFS is a traversal strategy that visits all nodes in a graph level by level.

```python
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    # Adds an edge to the graph
    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    # Performs BFS traversal on the graph
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        
        while queue:
            node = queue.popleft()  # Get the first node from the queue
            
            if node not in visited:  
                # Mark the node as visited and add it to the result
                visited.add(node)
                print(node, end=" ")
                
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        # Add the unvisited neighbors to the queue
                        queue.append(neighbor)

# Create a new graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

# Start BFS traversal from node 'A'
print("BFS Traversal:")
g.bfs('A')