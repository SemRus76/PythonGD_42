# from person import Person
from book import Book

if __name__ == "__main__":
    price = float(input("Введите цену:"))

    book = Book(price=price)

    print(book.get_data())

