def climb_stairs(n):
    if n <= 2:
        return n    
    first, second = 1, 2
    for _ in range(3, n + 1):
        third = first + second
        first = second
        second = third
    
    return second

n = int(input("Enter number of stairs: "))
result = climb_stairs(n)

print("Ways to climb stairs:", result)