class TrieNode:
    """
    A node in the Trie data structure.
    """

    def __init__(self):
        # Initialize a dictionary to store children nodes
        self.children = {}
        # Initialize a boolean to indicate the end of a word
        self.is_end_of_word = False


class Trie:
    """
    A Trie data structure.
    """

    def __init__(self):
        # Initialize the root node
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the Trie.
        """
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the current node's children, the word is not in the Trie
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return whether the end of the word is marked
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Search for all words in the Trie that start with a given prefix.
        """
        # Start at the root node
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the current node's children, there are no words that start with the prefix
            if char not in node.children:
                return []
            # Move to the child node
            node = node.children[char]
        # Return all words that start with the prefix
        return self._get_words(node, prefix)

    def _get_words(self, node, prefix):
        """
        Recursively get all words that start with a given prefix.
        """
        words = []
        # If the node is the end of a word, add it to the list
        if node.is_end_of_word:
            words.append(prefix)
        # Iterate over each child node
        for char, child_node in node.children.items():
            # Recursively get all words that start with the child node's prefix
            words.extend(self._get_words(child_node, prefix + char))
        return words


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("band")

print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("banana")) # True
print(trie.search("band"))   # True
print(trie.search("ban"))    # False

print(trie.starts_with("app")) # ["app", "apple"]
print(trie.starts_with("ban")) # ["band", "banana"]