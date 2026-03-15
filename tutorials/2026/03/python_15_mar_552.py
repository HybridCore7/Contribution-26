# knuth_morris_pratt.py

def compute_prefix_function(pattern):
    # Initialize a list to store the prefix function values
    m = len(pattern)
    pi = [0] * m
    
    # Compute the prefix function values
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    
    return pi

def search(pattern, text):
    # Initialize the prefix function values
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    
    # Initialize the indices for the pattern and text
    i = j = 0
    
    while j < len(text):
        if pattern[i] == text[j]:
            i += 1
        if i == m:
            return j - m + 1, i
        elif j < i:
            j += 1
        else:
            j += 1
            i = pi[i - 1]
    
    # If the pattern is not found in the text
    return None

def main():
    # Example usage
    pattern = "abc"
    text = "abcbcabcabcd"
    result = search(pattern, text)
    if result:
        print(f"Pattern found at index {result[0]}")
        print(f"Substring: {text[result[0]:result[1]]}")
    else:
        print("Pattern not found in the text")

if __name__ == "__main__":
    main()