txt = input("Enter any string: ")

maxx = -1
maxchar = ""

for t in txt:
    if txt.count(t) > maxx:
        maxx = txt.count(t)
        maxchar = t
print("Mode:",maxchar)
