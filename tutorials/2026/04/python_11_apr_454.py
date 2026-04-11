def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    prefix = [0] * len(pattern)
    
    # Compute the prefix values in a single pass over the pattern
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        # Update the prefix value at index i
        prefix[i] = j

def compute_prefix_array(text, pattern):
    # Initialize a list to store the prefix array values
    prefix = [0] * (len(pattern) + 1)
    
    # Call the function to fill in the prefix array
    compute_prefix_function(pattern)
    
    # Return the prefix array filled with zeros except at the end
    return prefix

def kmp_search(text, pattern):
    # Create the prefix array for the pattern
    prefix = compute_prefix_array(text, pattern)
    
    # Initialize the search and prefix indices
    j = 0
    m = len(pattern) - 1
    
    # Traverse the text to find a match with the pattern
    while j < len(text):
        if text[j] == pattern[m]:
            j += 1
            m -= 1
            
            # If we've matched all characters in the pattern, return the index
            if m == -1:
                print("Pattern found at index", j - len(pattern))
                return j
        
        # If not a match, reset to prefix value
        elif text[j] != pattern[m]:
            if m == 0:
                print("Pattern not found")
                break
            j = prefix[m - 1]
        
    # Pattern not found in the text
    print("Pattern not found")

text = "abracadabra"
pattern = "abraca"

kmp_search(text, pattern)