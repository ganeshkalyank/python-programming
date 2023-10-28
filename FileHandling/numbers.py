import csv

l = int(input("Starting number: "))
r = int(input("Ending number: "))

even = []
odd = []
div3 = []

for i in range(l,r+1):
    if i%3 == 0:
        div3.append(i)
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

filename = input("Enter filename: ")

with open(filename, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(even)
    writer.writerow(odd)
    writer.writerow(div3)
    print("Written successfully!")
    print()

with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
