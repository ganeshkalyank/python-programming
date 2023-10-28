books = []

def getBook():
    name = input("Enter name: ")
    author = input("Enter author: ")
    year = input("Enter year: ")

    return {"name":name,"author":author,"year":year}

def storeBook(book):
    books.append(book)

def get2022Books():
    for book in books:
        if book['year'] == '2022':
            print(book)

def main():
    for i in range(2):
        storeBook(getBook())
    get2022Books()

if __name__ == "__main__":
    main()
