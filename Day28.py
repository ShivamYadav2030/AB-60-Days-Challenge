def two_sum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
    return []



nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

result = two_sum(nums, target)

print("Indices:", result)