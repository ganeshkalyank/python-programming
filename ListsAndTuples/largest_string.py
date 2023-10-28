n = int(input("Enter no of strings: "))
txtlist = []

for i in range(n):
    txtlist.append(input("Enter string "+str(i+1)+": "))

txtlist.sort(key=lambda word: sum([ord(c) for c in word]))

print("Largest:",txtlist[-1])
