class Book:
    book_id = 0
    book_name = ""
    price = 0
    author_name = ""

    def calculate_discount_price(self):
        pass

class PrintedBook(Book):
    publisher = ""
    isbn_no = 0
    pages = 0
    year_of_edition = 0

    def calculated_discount_price(self):
        if self.pages <= 400:
            discount_price = self.price - 0.05*self.price
        elif self.pages > 400 and self.pages <100:
            discount_price = self.price - 0.1*self.price
        else:
            discount_price = self.price - 0.15*self.price
        return discount_price
    
    def print_details(self):
        print(f"{self.book_id}\t{self.book_name}\t{self.price}\t{self.author_name}\t{self.publisher}\t{self.isbn_no}\t{self.pages}\t{self.year_of_edition}")
    
class EBook(Book):
    type = ""
    size = ""

    def calculate_discount_price(self):
        if self.type == "Video":
            discount_price = self.price - 0.15*self.price
        elif self.type == "Audio":
            discount_price = self.price - 0.1*self.price
        elif self.type == "Text":
            discount_price = self.price - 0.05*self.price
        else:
            discount_price = 0
        return discount_price
    
    def print_details(self):
        print(f"{self.book_id}\t{self.book_name}\t{self.price}\t{self.author_name}\t{self.type}\t{self.size}")
    
def main():
    printed_books = []
    ebooks = []
    book_count = 1

    op = 0
    while True:
        print("1. Add Book")
        print("2. View All Books")
        print("3. View Book")
        print("4. Delete Book")
        print("5. Exit")
        op = int(input("Choose an option: "))

        match op:
            case 1:
                type = int(input("Enter Book Type (1. Printed, 2. Ebook): "))
                book_id = book_count
                book_count += 1
                book_name = input("Enter Book Name: ")
                price = int(input("Enter Book Price: "))
                author_name = input("Enter Author Name: ")
                if type == 1:
                    b = PrintedBook()
                    b.book_id = book_id
                    b.book_name = book_name
                    b.price = price
                    b.author_name = author_name
                    b.publisher = input("Enter Publisher: ")
                    b.isbn_no = int(input("Enter ISBN No: "))
                    b.pages = int(input("Enter Pages: "))
                    b.year_of_edition = int(input("Enter Yead of Edition: "))
                    printed_books.append(b)
                    print("Book added succesfully!")
                elif type == 2:
                    b = EBook()
                    b.book_id = book_id
                    b.book_name = book_name
                    b.price = price
                    b.author_name = author_name
                    b.type = input("Enter Content Type (Audio, Video, Text): ")
                    b.size = input("Enter File Size: ")
                    ebooks.append(b)
                    print("Book added succesfully!")
                else:
                    print("Invalid type!")
                    book_count -= 1
            case 2:
                print("\nPrinted Books: ")
                for printed_book in printed_books:
                    printed_book.print_details()
                print("\nEbooks: ")
                for ebook in ebooks:
                    ebook.print_details()
                print()
            case 3:
                id = int(input("Enter Book ID: "))
                for book in ebooks+printed_books:
                    if book.book_id == id:
                        book.print_details()
            case 4:
                id = int(input("Enter Book ID: "))
                for book in ebooks:
                    if book.book_id == id:
                        ebooks.remove(book)
                for book in printed_books:
                    if book.book_id == id:
                        printed_books.remove(book)
                print("Book removed succesfully (if exists)!")
            case 5:
                break


if __name__ == "__main__":
    main()
