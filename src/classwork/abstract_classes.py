# Абстрактные классы

# Необходимо реализовать систему классов для оружия в игре
# Пистолеты, автоматы, снайперская винтовка и БФГ

# Gun (оружие) - стрелять, целится, перезаряжатся и урон(п)
# Pistol
# AutoGun
# Snipe
# BFG
import abc # Библиотека для создания абстрактных классов

class Gun(abc.ABC):

    _damage = 0
    _bullet = 0

    def __init__(self, damage: int = 0, bullet_count: int = 0):
        self._damage = damage
        self._bullet = bullet_count

    def __del__(self):
        pass

    @abc.abstractmethod
    def fire(self):
        pass

    @abc.abstractmethod
    def aim(self):
        pass

    @abc.abstractmethod
    def reload(self):
        pass

    def __str__(self):
        return f"This is class GUN"

class BigFuckingGun(Gun):

    def __init__(self, damage: int = 0):
        super().__init__(damage)

    def __del__(self):
        pass

    def fire(self):
        print("ВЫСТРЕЛ БФГ - БОЙСЯ ВСЕЯ И ВСЕ")

    def aim(self):
        print("ЗАЧЕМ ТЫ ЦЕЛИШЬСЯ, ГЛУПЕЦ?!")

    def reload(self):
        print("ТЫ ДОВЕЛ БФГ ДО ПЕРЕЗАРЯДКИ? ЗАВОД АДУ ЗАКРЫЛИ, ПАТРОНОВ НЕТ!")

class AutoGun(Gun):
    def __init__(self, damage: int = 0, bullet_count: int = 0):
        super().__init__(damage, bullet_count)

    def __del__(self):
        pass

    def fire(self):
        for i in range(0,3):
            print("Ра-та-та-та")

    def reload(self):
        print("Перезарядка автомата")

    def aim(self):
        print("Целиться с автомата - терять время впустую")

def choice_weapon(weapon : Gun):
    weapon.fire()
    weapon.reload()
    weapon.aim()
    weapon.fire()



bfg = BigFuckingGun(1000)
ak = AutoGun(10)

choice_weapon(ak)
print("-===========-")
choice_weapon(bfg)
print("-===========-")

