def find_numbers(nums):
    count = 0
    
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    
    return count

# Input from user
nums = list(map(int, input("Enter numbers: ").split()))

result = find_numbers(nums)

print("Count of numbers with even digits:", result)