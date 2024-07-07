from arcade import RGB
import math
class Figure:
    sides_count = 0
    def __init__(self, __color: [], sides):
        self.__sides = sides = []
        self.__color = color = [RGB]
        self.filled = filled = bool
        if len(sides) > self.sides_count:
            sides = 1
            len(sides) == self.sides_count


    def __is_valid_color(self, r, g, b):
        if r and g and b == (0, 256):
            return True

    def set_color(self, r: int, g: int, b: int): #изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color:
            self.__color = [r, g, b]
        else:
            self.__color = __color

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *else_sides):
        for side in else_sides:
            if side == abs(int) and else_sides == self.sides_count:
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        for j in new_sides:
            if len(new_sides) != self.sides_count:
                self.__sides = self.__sides
            else:
                self.__sides = j

    def get_sides(self):
        return self.__sides

    def __len__(self):
        for i in self.__sides:
            return sum(self.__sides[i])



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = __radius = sides / (2 * math.pi)


    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__height = None


    @property
    def height(self):
        p = sum(sides) / 2
        if self.__height is None:
            for j in sides:
                self.__height = (2 * (math.sqrt(p * (p - j) * (p - j) * (p - j)))) / j
            return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def get_square(self):
        for i in sides:
            p = sum(i) / 2
            square = 2 * (math.sqrt(p * (p - i) * (p - i) * (p - i)))
        return square


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__()


    def get_volume(self):
        for i in self.__sides:
            volume = ((self.__sides(i)**3))
        return volume

circle1 = Circle((200, 200, 100), 10)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
circle1.set_sides(15)
print(circle1.get_sides())
print(circle1.get_square())
tr = Triangle((10, 10, 10), (1, 2, 3))
print(tr.height)