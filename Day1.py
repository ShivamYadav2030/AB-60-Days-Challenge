# Two Sum Problem

# Using Brute Force method
# arr=list(map(int,input().split()))
# target=int(input())
# n = len(arr)
# for i in range(n):
#   for j in range(i+1, n):
#     if arr[i] + arr[j] == target:
#       print(i,j)


# Using Optimal methods
arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target value: "))

seen = {}  
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        print(seen[complement], i)
        break
    seen[num] = i
        