# Topological Sort in Python
=====================================

Topological sorting is an ordering of vertices in a directed acyclic graph (DAG) such that for every edge u -> v, vertex u comes before v in the ordering.

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.in_degree = {vertex: 0 for vertex in range(vertices)}

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1

    # Function to perform topological sort using DFS
    def topological_sort(self):
        queue = deque([vertex for vertex in range(self.V) if self.in_degree[vertex] == 0])
        sorted_vertices = []

        while queue:
            vertex = queue.popleft()
            sorted_vertices.append(vertex)

            for neighbor in self.graph[vertex]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if the graph has a cycle
        if len(sorted_vertices) != self.V:
            return None

        return sorted_vertices[::-1]

# Example usage
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    sorted_vertices = g.topological_sort()
    if sorted_vertices:
        print("Topological Sort:", end=' ')
        for vertex in sorted_vertices:
            print(vertex, end=' ')
    else:
        print("Graph has a cycle")