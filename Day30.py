# Group anagram
def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())

words = input("Enter words separated by space: ").split()
result = group_anagrams(words)
print("Grouped Anagrams:", result)


# def product_except_self(nums):
#     n = len(nums)
#     result = [1] * n
#     prefix = 1
#     for i in range(n):
#         result[i] = prefix
#         prefix *= nums[i]
#     postfix = 1
#     for i in range(n - 1, -1, -1):
#         result[i] *= postfix
#         postfix *= nums[i]
#     return result


# nums = list(map(int, input("Enter numbers: ").split()))
# result = product_except_self(nums)
# print("Output:", result)