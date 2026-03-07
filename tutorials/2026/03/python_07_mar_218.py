import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Function to implement Dijkstra's algorithm
    def dijkstra(self, src):
        # Create a dictionary to store the distance to each vertex
        dist = {i: float('infinity') for i in range(self.V)}
        dist[src] = 0

        # Create a priority queue to store the vertices to be processed
        pq = [(0, src)]

        while pq:
            # Get the vertex with the smallest distance from the priority queue
            curr_dist, curr_vertex = heapq.heappop(pq)

            # If the current distance is greater than the already known distance, skip this vertex
            if curr_dist > dist[curr_vertex]:
                continue

            # Iterate over all the adjacent vertices of the current vertex
            for neighbour, weight in self.graph:
                if neighbour != curr_vertex:
                    # Calculate the distance to the adjacent vertex
                    distance = curr_dist + weight

                    # If the calculated distance is less than the already known distance, update the distance
                    if distance < dist[neighbour]:
                        dist[neighbour] = distance
                        # Add the vertex to the priority queue
                        heapq.heappush(pq, (distance, neighbour))

        # Print the shortest distance to each vertex
        for i in range(self.V):
            print(f"Vertex {i} is at distance {dist[i]}")

# Create a graph with 5 vertices
g = Graph(5)

# Add edges to the graph
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.add_edge(2, 4, 8)
g.add_edge(3, 4, 10)

# Run Dijkstra's algorithm
g.dijkstra(0)