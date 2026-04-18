num = int(input("Enter number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


arr = list(map(int,input().split()))
seen = set()
for num in arr:
    if num in seen:
        print(num)
        break
    seen.add(num)

arr = list(map(int,input().split()))
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print("Largest element is:", largest)