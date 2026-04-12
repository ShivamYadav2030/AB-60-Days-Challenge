# Maximum Subarray Sum
# Brute force
# def max_subarray(nums):
#   n = len(nums)
#   max_sum = float('-inf')
#   for i in range(n):
#         s = 0
#         for j in range(i, n):
#             s += nums[j]
#             max_sum = max(max_sum, s)
#   return max_sum

# Using Kadane algorithm
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = list(map(int, input("Enter numbers: ").split()))
result = max_subarray(nums)
print("Maximum Subarray Sum:", result)