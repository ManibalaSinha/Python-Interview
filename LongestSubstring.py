#function to find the longest substring without repeating characters in python
def longest_unique_substring(s):
    start = 0 
    max_length = 0
    used_chars = {}
    longest_sub = ""

    for end in range(len(s)):
        char = s[end]
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        used_chars[char] = end
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            longest_sub = s[start:end+1]
    
    return longest_sub
