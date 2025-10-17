class Book:
    def __init__(book, title, author, available):
        book.title = title
        book.author = author
        book.available = available

    def display(book):
        print(f"Title: {book.title}\nAuthor: {book.author}\nAvailability: {book.available}\n")
    
book1 = Book("The Midnight Library", "J.K Rowling", )

book1.display()