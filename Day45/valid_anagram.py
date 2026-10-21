
def is_anagram(s, t):
    return sorted(s) == sorted(t)


s = input("Enter first string: ").lower()
t = input("Enter second string: ").lower()

if is_anagram(s, t):
    print("True - They are anagrams")
else:
    print("False - They are not anagrams")
