class UnionFind:
    def __init__(self, n):
        # Initialize the parent array, where each element is the parent of itself
        self.parent = list(range(n))
        # Initialize the rank array, where each element is the rank of itself
        self.rank = [0] * n

    def find(self, x):
        # If x is not the parent of itself, find its parent and update the parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        # Return the parent of x
        return self.parent[x]

    def union(self, x, y):
        # Find the parents of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        # If the parents are different, merge the groups
        if root_x != root_y:
            # If the rank of root_x is higher, make root_y the parent of root_x
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            # If the rank of root_y is higher, make root_x the parent of root_y
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            # If the ranks are equal, make root_y the parent of root_x and increment the rank of root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Example usage
if __name__ == "__main__":
    # Create a UnionFind object with 5 elements
    uf = UnionFind(5)
    # Perform some union operations
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    # Find the parents of some elements
    print(uf.find(0))  # Output: 0
    print(uf.find(1))  # Output: 0
    print(uf.find(2))  # Output: 0
    print(uf.find(3))  # Output: 3
    print(uf.find(4))  # Output: 3
    # Perform more union operations
    uf.union(0, 3)
    # Find the parents of some elements again
    print(uf.find(0))  # Output: 3
    print(uf.find(1))  # Output: 3
    print(uf.find(2))  # Output: 3
    print(uf.find(3))  # Output: 3
    print(uf.find(4))  # Output: 3