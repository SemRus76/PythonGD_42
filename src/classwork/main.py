from function.function import getMathFunc as mFunc
import os

def getResult(example : str) -> int:
    First = ""
    Second = ""
    Sign = ""
    temp = ""
    for char in example:
        if char in "+-*/^":
            First = int(temp)
            Sign = char
            temp = ""
        elif char in "\n":
            continue
        else:
            temp += char
    Second = int(temp)
    func = mFunc(Sign)
    return func(First, Second)

def getFile():
    resultLst = list()
    # file = open("resources/name.txt", "r+")
    with open("name.txt", "r+") as file:
        for line in file:
            line = line.removesuffix("\n")
            result = getResult(line)
            resultLst.append(f"{line} = {result}\n")

    return resultLst

os.chdir("resources")
results = getFile()
if not os.path.isdir("result"):
    os.mkdir("result")

os.chdir("result")
# os.kill(9288,9)
with open("results.txt", "w") as file:
    for line in results:
        file.write(line)
