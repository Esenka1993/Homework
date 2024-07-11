import arcade
import math
class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled = False):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = list(sides) * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = filled


    def __is_valid_color(self, r, g, b):
        for colour in [r, g, b]:
            if not (isinstance((colour), int) and 0 <= colour <= 255):
                return False
        return True

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *else_sides):
        if isinstance(self, Cube):
            cond1 = len(else_sides) * 1
        else:
            len(else_sides) == self.sides_count
        cond2 = all([isinstance(side, int) and side > 0 for side in else_sides])
        return cond1 and cond2

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * self.sides_count
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)
        self.__radius = __radius = sides / (2 * math.pi)

    def get_radius(self):
        return self.__radius


    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)
        self.__height =

    def get_square(self):




class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)


    def get_volume(self):
        for i in self.__sides:
            volume = ((self.__sides(i)**3))
        return volume

circle1 = Circle((200, 200, 100), 10)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
circle1.set_sides(15)
print(circle1.get_sides())
