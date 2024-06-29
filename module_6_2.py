class Vehicle:
    import re
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power
    def get_model(self):
        return f"Модель: {self.__model}"
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(Vehicle.get_model(self), Vehicle.get_horsepower(self), Vehicle.get_color(self), f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        for i in Vehicle.__COLOR_VARIANTS:
            Vehicle.__COLOR_VARIANTS = [i.upper() for i in Vehicle.__COLOR_VARIANTS]
        if new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

