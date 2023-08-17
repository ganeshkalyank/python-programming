a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a>b:
    largest = a
else:
    largest = b
if c>largest:
    largest = c
print("Largest: ", largest)
