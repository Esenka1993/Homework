import inspect
import random
import pprint
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
    attributes = []
    methods = []
    for atr in dir(obj):
        if callable(getattr(obj, atr)):
            attributes.append(atr)
        else:
            methods.append(atr)
    info = {'Тип объекта': type(obj),
            'Атрибуты': attributes,
            'Методы': methods,
            'В каком мы модуле': inspect.getmodule(obj),
            'Проверка классовости': inspect.isclass(obj)}
    return info
myWand = At_Ollivanders(50, False)
obj_info = introspection_info(myWand)
pprint.pprint(obj_info)
number_info = introspection_info(42)
pprint.pprint(number_info)

