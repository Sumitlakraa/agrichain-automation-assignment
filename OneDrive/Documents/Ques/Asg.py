def length_of_longest_substring(s):
    last_seen = {}
    start = 0 
    max_length = 0 

    for i in range(len(s)):
        char = s[i]
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Test cases
print(length_of_longest_substring("abcabcbb"))   # Given Example
print(length_of_longest_substring("bbbbb"))      # Given Example
print(length_of_longest_substring("a b x q  "))  # Random


