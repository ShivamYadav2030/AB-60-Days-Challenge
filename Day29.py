def top_k_frequent(nums, k):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    return result


# Input
nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter value of k: "))

result = top_k_frequent(nums, k)

print("Top K Frequent Elements:", result)