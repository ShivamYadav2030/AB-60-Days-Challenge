# Palindrome Number
def is_palindrome(num):
    original = num
    reverse = 0
    
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    
    if original == reverse:
        return True
    else:
        return False


num = int(input("Enter a number: "))

result = is_palindrome(num)

if result:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")