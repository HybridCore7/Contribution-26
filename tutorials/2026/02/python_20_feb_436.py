# Knuth-Morris-Pratt Algorithm Implementation in Python

# The KMP algorithm is a linear-time string searching algorithm that uses the observation
# that when a mismatch occurs, the information about the mismatch can be used to skip
# characters in the text and to shift the pattern along the text. The algorithm is
# efficient because it uses the information about the mismatch to skip characters in
# the text.

def compute_prefix_function(pattern):
    """
    Compute the prefix function for the KMP algorithm.

    The prefix function is an array where the i-th element is the length of the longest
    proper prefix of the pattern that is also a proper suffix.

    Args:
        pattern (str): The pattern to compute the prefix function for.

    Returns:
        list: The prefix function for the pattern.
    """
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    return prefix

def kmp_search(text, pattern):
    """
    Search for the pattern in the text using the KMP algorithm.

    Args:
        text (str): The text to search for the pattern in.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of indices where the pattern is found in the text.
    """
    prefix = compute_prefix_function(pattern)
    indices = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            indices.append(i - j + 1)
            j = prefix[j - 1]
    return indices

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABAB"
indices = kmp_search(text, pattern)
print("Pattern found at indices:", indices)

text = "AAAAABBBBCCCCDDDD"
pattern = "AB"
indices = kmp_search(text, pattern)
print("Pattern found at indices:", indices)

text = "ABCDEFG"
pattern = "CD"
indices = kmp_search(text, pattern)
print("Pattern found at indices:", indices)