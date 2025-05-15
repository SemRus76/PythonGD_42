class Stack:
    __container = list()
    __size = 0

    def __init__(self):
        pass

    def __del__(self):
        if self.__size > 0:
            self.__size = 0
            self.__container.clear()

    def push(self, element):
        self.__container.append(element)
        self.__size += 1

    def pop(self):
        self.__size -= 1
        return self.__container.pop()

    def top(self):
        return self.__container[self.__size - 1]

    @property
    def size(self):
        return self.__size
