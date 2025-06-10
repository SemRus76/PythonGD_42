# Задание - На завод по производству автомобилей необходимо создать
# систему классов для ведения базы данных всех выпущенных авто
# Все автомобили обладают следующими характеристиками:
# 1. Цена - Price
# 2. Название - Name
# 3. Цвет - Color
# 4. Мощность двигателя - Power Engine
# 5. Макс. скорость - Max Speed
# Необходимо реализовать классы для следующих видов машин:
# - Седан
#   1. АКПП/МКПП - Transmission Box
#   2. Кол-во дополнительных опций - Additional options
# - Внедорожник
#   1. Рамный или нет - Frame
#   2. Полный привод - Full Drive
#   3. Блокировка - Blocking
#   4. Вид топлива - Type Fuel
# - Грузовой
#   1. Тоннаж - Tonnage
#   2. Возможность установки прицепа - Trailer
#   3. Наличие спального места - Sleeping Place
#   4. Кол-во мест - Count Seats

import abc

class Interface(abc.ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @abc.abstractmethod
    def forward_moving(self):
        pass

    @abc.abstractmethod
    def backward_moving(self):
        pass

    @abc.abstractmethod
    def hand_brake(self):
        pass

    @abc.abstractmethod
    def start_engine(self):
        pass

    @staticmethod
    def static_method():
        print("Hello World")


def function(obj : Interface):
    pass

Interface.static_method()


    


