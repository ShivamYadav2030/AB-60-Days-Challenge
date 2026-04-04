# Running Sum of 1D Array

n=int(input("Enter the number of value in array:"))
arr=list(map(int,input("Enter number seperated by space:").split()))

result=[]
total=0
for num in arr:
  total+=num
  result.append(total)
print(*result)

# Using In-place 
n=int(input("Enter the number of value in array:"))
arr=list(map(int,input("Enter the number seperated by space:").split()))

for i in range(1,n):
  arr[i]=arr[i]+arr[i-1]
  
print(*arr)