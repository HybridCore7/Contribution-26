def compute_prefix_function(pattern):
    # Initialize prefix function with zeros
    prefix = [0] * len(pattern)
    j = 0
    # Traverse the pattern from the second character to the end
    for i in range(1, len(pattern)):
        # If the current character matches the character at the current prefix position
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j - 1]
        # If the characters match, move to the next character
        if pattern[j] == pattern[i]:
            j += 1
        # Update the prefix function
        prefix[i] = j
    return prefix


def kmp_search(text, pattern):
    # Compute the prefix function
    prefix = compute_prefix_function(pattern)
    # Initialize the search position
    j = 0
    # Traverse the text
    for i in range(len(text)):
        # If the current character matches the character at the current prefix position
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        # If the characters match, move to the next character
        if text[i] == pattern[j]:
            j += 1
        # If the entire pattern has been matched
        if j == len(pattern):
            # Return the position of the matched pattern
            return i - j + 1
    # If the pattern is not found
    return -1


# Example usage
text = "banana"
pattern = "ana"
position = kmp_search(text, pattern)
if position != -1:
    print(f"Pattern found at position {position} in text: {text}")
else:
    print("Pattern not found in text")