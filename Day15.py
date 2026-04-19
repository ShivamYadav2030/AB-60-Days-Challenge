def contains_duplicate(nums):
    seen = set()  
    for num in nums:
        if num in seen:
            return True
        seen.add(num) 
    return False

nums = list(map(int, input("Enter numbers: ").split()))
result = contains_duplicate(nums)
if result:
    print("Contains Duplicate")
else:
    print("No Duplicate Found")