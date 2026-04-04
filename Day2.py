# Running Sum of 1D Array

n=int(input("Enter the number of value in array:"))
arr=list(map(int,input("Enter number seperated by space:").split()))

result=[]
total=0
for num in arr:
  total+=num
  result.append(total)
print(*result)

