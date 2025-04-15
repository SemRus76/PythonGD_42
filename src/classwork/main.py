print("Hello World")
print("Hello World 2")
print("Hello World 3")
print("Hello World 4")
from function.function import getMathFunc as getMath

def SplitExample(example : str) -> list:
    temp = ""
    first = 0
    sign = ""
    second = 0
    for char in example:
        if char in "+-*/^":
            sign = char
            first = int(temp)
            temp = ""
        else:
            temp += char
    second = int(temp)
    return [first, sign, second]

def Equales(example : str) -> int:
    exList = SplitExample(example)
    func = getMath(exList[1])
    return func(exList[0],exList[2])
def InterFib(number : int) -> int:
    first = 0
    second = 1
    for i in range(2, number + 1):
        second = first + second
        first = second - first
    return second


ex = input("Введите пример: ")
print(f"Ответ: {ex}={Equales(ex)}")
