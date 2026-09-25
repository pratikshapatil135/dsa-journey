def first_non_repeating(s):
    count = {}

    # Count frequency of each character
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Find the first character with frequency 1
    for char in s:
        if count[char] == 1:
            return char

    return None


s = "leetcode"

result = first_non_repeating(s)

print("First non-repeating character:", result)