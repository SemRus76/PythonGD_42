# class <Имя класса>:

class Person:
    def __init__(self, name : str = "Name", age : int = 0):
        self.__age = age
        self.__name = name

    def __del__(self):
        pass
        # print(f"Удален {self.__name}")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter # Сеттеры могут быть объявлены ТОЛЬКО после объявления свойств
    def age(self, new_age : int):
        if new_age > 0 and new_age < 110:
            self.__age = new_age

    def say_hello(self) -> str:
        return f"Hello, my name is {self.__name}! I am {self.__age} years old"