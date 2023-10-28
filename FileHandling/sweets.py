sweets = []

op = "y"
while op == "y":
    sweet = []
    sweet.append(input("Enter sweet name: "))
    sweet.append(input("Enter price: "))
    sweets.append(sweet)
    op = input("Add another? (y/n): ")

with open("sweets.txt","w") as file:
    for sweet in sweets:
        file.write(sweet[0]+","+sweet[1]+"\n")
    print("Written successfully!")

sweetsread = []
with open("sweets.txt", "r") as file:
    for line in file:
        line = line.strip()
        sweetread = line.split(",")
        sweetsread.append(sweetread)

price = input("Enter price: ")
for sweetread in sweetsread:
    if sweetread[1] == price:
        print(sweetread)
