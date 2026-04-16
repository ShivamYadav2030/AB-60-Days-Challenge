def is_anagram(s, t):
    if len(s) != len(t):
        return False   
    freq = {}   
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in t:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    
    return True

# Input
s = input("Enter first string: ")
t = input("Enter second string: ")
result = is_anagram(s, t)
if result:
    print("Valid Anagram")
else:
    print("Not an Anagram")