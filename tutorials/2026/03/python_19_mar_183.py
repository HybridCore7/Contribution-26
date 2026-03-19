# Breadth First Search Graph Traversal in Python

class Graph:
    def __init__(self):
        # Initialize an empty graph with adjacency list representation
        self.adj_list = {}

    def add_edge(self, node1, node2):
        # Add a directed edge from node1 to node2
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        self.adj_list[node1].append(node2)

    def bfs_traversal(self, start_node):
        # Initialize visited set and queue for BFS traversal
        visited = set()
        queue = [start_node]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)  # Mark the node as visited
                print(node, end=" ")  # Print the node

                # Enqueue all unvisited neighbors of the current node
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited


# Create a sample graph with edges
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'F')

# Perform BFS traversal starting from node A
print("BFS Traversal of the graph starting from A:")
visited = graph.bfs_traversal('A')
print("\nVisited nodes:", visited)