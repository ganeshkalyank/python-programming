n = int(input("Enter no. of numbers: "))

arr = []

for i in range(0,n):
    num = int(input("Enter number "+str(i+1)+": "))
    arr.append(num)
numlist=""

for i in arr:
    numlist+=str(i)+" "

print("Same line:",numlist)

print("Line by line: ")

for i in arr:
    print(i)
