from person import Person

if __name__ == "__main__":
    human_1 = Person()
    human_1.age = 20
    human_2 = Person("Margaret")
    human_2.age = 40

    # human_2.name = "Megan"
    # print(human_1.name)
    # print(human_2.name)
    # print(human_1.name)

    # human_1._Person__age = 10
    # print(human_1.age)
    # human_1.age = 1540
    # print(human_1.age)

    print(human_1.say_hello())
    print(human_2.say_hello())