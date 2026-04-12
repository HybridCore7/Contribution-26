# Breadth First Search (BFS) Graph Traversal in Python
=====================================================

This script demonstrates the implementation of a Breadth First Search (BFS) algorithm for graph traversal.

```python
from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Function to add an edge between two vertices
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    # Function to perform BFS traversal
    def bfs(self, start_vertex):
        visited = set()
        traversal_order = []

        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.popleft()

            # Print the current vertex
            print(current_vertex, end=" ")

            # Add adjacent vertices to the queue
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

        traversal_order.append(start_vertex)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')

    print("BFS Traversal Order:")
    graph.bfs('A')
```

Output:
```
A B D C E