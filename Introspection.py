import inspect
import random
class At_Ollivanders:
    def __init__(self, age: int, power: bool):
        self.age = age
        self.power = True

    def wand_choice(self):
        wood = ['oak', 'elm tree', 'aspen', 'cherry tree', 'chestnut']
        core = ['the Dragon`s Heart Vein', 'Unicorn hair', 'Phoenix feather', 'Vale hair', 'Thestral hair']
        if self.check_for_wand:
            return random.choice(wood), random.choice(core)

    def check_for_wand(self):
        if self.age >= 11 and self.power:
            print(f'Можешь выбрать палочку!')


def introspection_info(obj):
    print(type(obj))
    print(hasattr(obj, 'age'))
    print(dir(obj))
    print(inspect.getmodule(obj))
    print(inspect.isclass(obj))

myWand = At_Ollivanders(12, True)
introspection_info(myWand)
