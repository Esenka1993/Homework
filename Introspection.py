import inspect
import random
class At_Ollivanders:
    def __init__(self, age: int, power: bool):
        self.age = age
        self.power = power

    def wand_choice(self):
        wood = ['Oak', 'Elm tree', 'Aspen', 'Cherry tree', 'Chestnut']
        core = ['the Dragon`s Heart Vein', 'Unicorn hair', 'Phoenix feather', 'Vale hair', 'Thestral hair']
        if self.age >= 11 and self.power:
            p1 = random.choice(wood)
            p2 = random.choice(core)
            print(f"Here is your wand: made of {p1} with core of {p2}!")
        else:
            print("Muggles and youngsters are not allowed in!")


def introspection_info(obj):
    print(type(obj))
    print(hasattr(obj, 'age'))
    print(dir(obj))
    print(inspect.getmodule(obj))
    print(inspect.isclass(obj))

myWand = At_Ollivanders(12, True)
introspection_info(myWand)
