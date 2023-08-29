n = int(input("No. of strings: "))

stringlist = []
for i in range(n):
    string = input("Enter string "+str(i+1)+": ")
    stringlist.append(string)

caseinverted = []
for string in stringlist:
    caseinverted.append(string.swapcase())

vowelsremoved = []
for string in stringlist:
    modstring = string
    for i in ["a","e","i","o","u"]:
        modstring = modstring.replace(i,"")
    vowelsremoved.append(modstring)

dupsremoved = []
for string in stringlist:
    modstring = string
    for s in modstring:
        if modstring.count(s) > 1:
            modstring = modstring.replace(s,"")
    dupsremoved.append(modstring)

print("Case inverted: ")
print(caseinverted)

print("Vowels removed: ")
print(vowelsremoved)

print("Duplicates removed: ")
print(dupsremoved)

print("Duplicate string check: ")
for string in stringlist:
    if stringlist.count(string) > 1:
        print(string, ": Duplicate value")
