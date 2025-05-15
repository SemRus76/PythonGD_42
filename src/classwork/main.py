# from person import Person
from book import Book
from stack import Stack

if __name__ == "__main__":
    price = float(input("Введите цену:"))

    book = Book(price=price)

    print(book.get_data())

# Задание - Создать класс для структуры данных Stack
# Класс должен иметь методы - push, pop, top, size
# push - добавляет элемент в стэк
# pop - удаляет элемент из стэка и возвращает его значение
# top - возвращает значение верхнего элемента стэка
# size - возвращает кол-во элементов в стэке
    stc = Stack()
    stc.push("First")
    stc.push(2)
    stc.push(3.0)
    while stc.size > 0:
        print(stc.pop())

