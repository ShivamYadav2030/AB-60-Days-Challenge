# Example API
def isBadVersion(version):
    return version >= 4   


def first_bad_version(n):
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


# Input
n = int(input("Enter total versions: "))
result = first_bad_version(n)
print("First Bad Version:", result)