def reverse_string_loop(s):
    reversed = "" 
    for char in s:
        reversed = char + reversed    
    return reversed

#Using slicing
# def reverse_string(s):
#     return s[::-1]

s = input("Enter a string: ")

print("Reversed String:", reverse_string_loop(s))