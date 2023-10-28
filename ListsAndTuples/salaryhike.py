emptuple = ((1,"Ganesh"),(2,"Kalyan"))

emplist = ((1,3,10000),(2,5,15000))

revsallist = []

for emp in emplist:
    if emp[1] > 4:
        revsallist.append(emp)

print(revsallist)
