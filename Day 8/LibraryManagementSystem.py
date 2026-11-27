class Book:

    def __init__(self, book_id, title, author, pages, published_date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.pages = pages
        self.published_date = published_date
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"ID : {self.book_id} | Title : {self.title} | Author : {self.author} | "
              f"Pages : {self.pages} | Published : {self.published_date} | Status : {status}")


class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Member ID: {self.member_id} | Name: {self.name}")
        print("Borrowed books:")
        if not self.borrowed_books:
            print("  None")
        for book in self.borrowed_books:
            print(f"  - {book.title}")

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book is not available")
            
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print("This book was not borrowed by this member")


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print(f"{book.title} already exists in the Library")
                return
        self.books.append(book)
        print(f"{book.title} book added to the Library")

    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print(f"{member.name} already exists") 
                return
        self.members.append(member)
        print(f"{member.name} added successfully")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_books(self):
        if not self.books:
            print("No books available in the library")
            return
        for book in self.books:
            book.display_info()

    def display_members(self):
        if not self.members:
            print("No members are registered")
            return
        for member in self.members:
            member.display()

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print(f"Member with ID {member_id} not found")
            return

        if not book:
            print(f"Book with ID {book_id} not found")
            return

        member.borrow_book(book)

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print(f"Member with ID {member_id} not found")
            return
        
        if not book:
            print(f"Book with ID {book_id} not found")
            return

        member.return_book(book)


if __name__ == "__main__":
    
    library = Library()

    
    book1 = Book(101, "1984", "George Orwell", 328, "1949-06-08")
    book2 = Book(102, "To Kill a Mockingbird", "Harper Lee", 281, "1960-07-11")

    
    member1 = Member(1, "Alice")
    member2 = Member(2, "Bob")


    print("--- Adding Books ---")
    library.add_book(book1)
    library.add_book(book2)


    print("\n--- Registering Members ---")
    library.add_member(member1)
    library.add_member(member2)


    print("\n--- Library Catalog & Members ---")
    library.display_books()
    library.display_members()

    
    print("\n--- Borrowing & Returning Operations ---")
    library.borrow_book(1, 101)

    
    library.borrow_book(2, 101)

    library.return_book(1, 101)

    library.borrow_book(2, 101)

    
    print("\n--- Final Member Status ---")
    member1.display()
    member2.display()
