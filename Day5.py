# Number of steps required to make it zero

def number_of_steps(num):
    steps = 0
    
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps += 1
    return steps


num = int(input("Enter a number: "))

result = number_of_steps(num)

print("Number of steps:", result)