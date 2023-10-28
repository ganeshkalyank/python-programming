lista = [1,2,3,4]
listb = [1,3,5,7]

union = []
intersection = []

for a in lista + listb:
    if a in lista and a in listb and a not in union:
        union.append(a)
    if (a in lista or a in listb) and a not in intersection:
        intersection.append(a)

print("Union: ",union)
print("Intersection: ", intersection)
