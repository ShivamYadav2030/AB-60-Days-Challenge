def is_valid(s):
    stack = []
    pairs = {')': '(',']': '[','}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


s = input("Enter parentheses string: ")
result = is_valid(s)
if result:
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")