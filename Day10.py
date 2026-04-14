def move_zeroes(nums):
    j = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

nums = list(map(int, input("Enter numbers: ").split()))
result = move_zeroes(nums)
print("Output:", result)