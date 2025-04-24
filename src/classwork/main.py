# Задача 1 - Вводится строка, состоящая из скобочек.
# Необходимо написать функцию которая волидирует данную строку на правильность
# Правила:
# 1. Могут использоватся три вида скобочек - () [] {}
# 2. У каждой открывающейся ОБЯЗАНА быть закрывающаяся
# 3. Каждая скобочка ОБЯЗАНА закрываться скобкой своего вида
# 4. Области действия скобок НЕ МОГУТ пересекаться - ({)} -> False
# Примеры:
# ()[]{} -> True
# ({[]}) -> True
# ([) -> False
# ({)} -> False
# ([]{()}) -> True

def isBracketValidator(example : str) -> bool:
    stack = list()
    for elem in example:
        if elem in "({[":
            stack.append(elem)
        elif elem == ")":
            if stack[len(stack) - 1] == "(":
                stack.pop()
                continue
            else:
                return False
        elif elem == "}":
            if stack[len(stack) - 1] == "{":
                stack.pop()
                continue
            else:
                return False
        elif elem == "]":
            if stack[len(stack) - 1] == "[":
                stack.pop()
                continue
            else:
                return False
    return False if len(stack) else True


print(isBracketValidator("{(})"))

# Задача 2 - RomanToInt
# Дана строка, в которой содержится 1 число, записанное римскими цифрами
# Необходимо вывести строку вида: {римская запись} = {арабская запись}
# Римские цифры имеют следующие правила
# I - 1   D = 500
# V - 5   M = 1000
# X - 10
# L - 50
# C - 100
# НО, для описания некоторых чисел вводится операция вычитания - IV = 4
# У римских чисел имеются следующие правила:
# При записи числа ВСЕГДА впереди идет самый большой порядок, за исключением
# следующих ситуаций
# 1. Перед C и L может быть записано несколько X для обозначения вычитания
# 2. Перед X может быть записано V или I для обозначения вычитания
# 3. Перед V может быть записано I для обозначения вычитания
# Примеры для расшифроки:
# CLXVIII = 168
# CXLIV = 144
# LXXXVIII = 88

def romanToInt(roman : str) -> int:
    arabian = list()
    for elem in roman:
        match elem:
            case "I":
                arabian.append(1)
            case "V":
                arabian.append(5)
            case "X":
                arabian.append(10)
            case "L":
                arabian.append(50)
            case "C":
                arabian.append(100)
    result = 0
    lvl = 1
    temp = 0
    for arab in arabian[::-1]:
        if arab == lvl:
            temp += lvl
        elif arab < lvl:
            temp -= arab
        elif arab > lvl:
            result += temp
            temp = lvl = arab
    result += temp
    return result
    # romanToDigit = {
    #     "I" : 1,
    #     "V" : 5,
    #     "X" : 10,
    #     "L" : 50,
    #     "C" : 100
    # }
    # levels = "IVXLC"
    # lvl = 0
    # temp = 0
    # result = 0
    # for elem in roman[::-1]:
    #     pass
    # result += temp
    # return result

print(romanToInt("IVXCVXXL"))


