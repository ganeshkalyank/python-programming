import journal as j
import book as b

itemlist = []

n = int(input("Enter no of items: "))

for i in range(n):
    typ = input("Enter type (journal / book): ")
    match typ:
        case "journal":
            itemlist.append(j.getJournal())
        case "book":
            itemlist.append(b.getBook())

for item in itemlist:
    print(item)
