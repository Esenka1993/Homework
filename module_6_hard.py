import math as m


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        if self.__is_valid_sides(*__sides):
            if isinstance(self, Cube):
                self.__sides = list(__sides) * self.sides_count
            else:
                self.__sides = list(__sides)
        else:
            self.__sides = [1] * self.sides_count
        self.__color = list(__color) if self.__is_valid_color(*__color) else [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0,256) and g in range(0,256) and b in range(0,256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]


    def __is_valid_sides(self, *__sides):
        cond1 = all(isinstance(side, int) and side > 0 for side in __sides)
        if isinstance(self, Cube):
            cond2 = len(__sides) == 1
        else:
            cond2 = len(__sides) == self.sides_count
        return cond1 and cond2


    def get_sides(self):
        return self.__sides


    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides: int):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * self.sides_count
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__radius = __radius = self.get_sides()[0] / (2 * m.pi)

    def get_square(self):
        return round(m.pi * m.sqrt(self.__radius), 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.count = count = [x for x in __sides]
        self.__p = __p = (sum(map(int, __sides))) / 2
        self.__height = __height = (2 * m.sqrt(__p * (__p - count[0]) * (__p - count[1]) * (__p - count[2]))) / count[0]

    def get_square(self):
        return round((self.count[0] * self.__height) / 2, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__sides = __sides

    def get_volume(self):
        return super().get_sides()[0] **2 * 6


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
