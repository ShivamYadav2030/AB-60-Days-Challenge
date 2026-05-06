def contains_nearby_duplicate(nums, k):
    index_map = {}
    for i in range(len(nums)):
        if nums[i] in index_map and i - index_map[nums[i]] <= k:
            return True  
        index_map[nums[i]] = i
    return False


nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))
result = contains_nearby_duplicate(nums, k)

if result:
    print("Duplicate found within range")
else:
    print("No such duplicate")