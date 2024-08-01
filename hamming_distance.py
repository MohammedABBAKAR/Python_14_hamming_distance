# Hamming distance is the number of characters that differ between two strings.

# To illustrate:

# String1: "abcbba"
# String2: "abcbda"

# Hamming Distance: 1 - "b" vs. "d" is the only difference.

# Create a function that computes the hamming distance between two strings.
# Examples

# hamming_distance("abcde", "bcdef") ➞ 5

# hamming_distance("abcde", "abcde") ➞ 0

# hamming_distance("strong", "strung") ➞ 1





def hamming_distance(str1, str2):
    # Ensure both strings are of the same length
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    
    # Initialize a counter for the differing characters
    distance = 0
    
    # Iterate through each character in the strings
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance

# Examples
print(hamming_distance("abcde", "bcdef"))  # Output: 5
print(hamming_distance("abcde", "abcde"))  # Output: 0
print(hamming_distance("strong", "strung"))  # Output: 1




def hamming_distance(str1, str2):
    # Ensure both strings are of the same length
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    
    # Initialize the distance counter
    distance = 0
    
    # Iterate through characters of both strings by index
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Examples
print(hamming_distance("abcde", "bcdef"))  # Output: 5
print(hamming_distance("abcde", "abcde"))  # Output: 0
print(hamming_distance("strong", "strung"))  # Output: 1
