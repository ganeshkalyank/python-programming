n = int(input("Enter no of numbers: "))
even = 0
odd = 0
for i in range(1,n+1):
    num = int(input("Enter number "+str(i)+": "))
    if num%2 == 0:
        even += 1
    else:
        odd += 1

print("Even: ",even)
print("Odd: ",odd)
