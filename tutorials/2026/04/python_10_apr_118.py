# Union-Find Algorithm Implementation in Python

class UnionFind:
    def __init__(self, n):
        """
        Initialize the union-find data structure with n elements.
        
        :param n: The number of elements to represent as disjoint sets.
        """
        # Create a list to store the parent of each element
        self.parent = list(range(n))
        # Create a list to store the rank of each set
        self.rank = [0] * n

    def find(self, x):
        """
        Find the root of the set that contains x.
        
        :param x: The element to find the root for.
        :return: The root of the set that contains x.
        """
        # If x is not its own parent, find the root recursively
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merge the sets that contain x and y.
        
        :param x: An element in one set.
        :param y: An element in another set.
        """
        # Find the roots of the sets containing x and y
        root_x = self.find(x)
        root_y = self.find(y)

        # If the sets are already merged, do nothing
        if root_x == root_y:
            return

        # Merge the sets by making one root the parent of the other
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            # Increment the rank of one set when merged
            self.rank[root_x] += 1

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(5)
    print("Initial sets:")
    for i in range(5):
        print(f"{i} -> {uf.find(i)}")

    # Merge some sets
    uf.union(0, 1)
    print("\nSets after union(0, 1):")
    for i in range(5):
        print(f"{i} -> {uf.find(i)}")

    uf.union(2, 3)
    print("\nSets after union(2, 3):")
    for i in range(5):
        print(f"{i} -> {uf.find(i)}")

    # Try to merge a set with itself
    uf.union(4, 4)
    print("\nSets after union(4, 4):")
    for i in range(5):
        print(f"{i} -> {uf.find(i)}")