def length_of_last_word(s):
    s = s.strip()
    count = 0 
    for char in reversed(s):
        if char != " ":
            count += 1
        else:
            break
    
    return count

s = input("Enter a string: ")
result = length_of_last_word(s)
print("Length of last word:", result)