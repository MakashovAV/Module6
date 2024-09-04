# Дополнительное практическое задание по модулю: "Наследование классов."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = [*sides]
        self.filled = True

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):  # Method '__is_valid_color' may be 'static' ???
        return all(0 <= x <= 255 and isinstance(x, int) for x in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print('Нет такого цвета')

    def __is_valid_sides(self, *sides):  # сделать проверку
        return all(isinstance(x, int) for x in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(
            self):  # Метод __len__ должен возвращать периметр фигуры. Дописать !!!!!!!!!!!!!!!!!!!! для каждой свой ?
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        else:
            print('Количество сторон не верно')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != 1:
            self.set_sides(1)
        self.__radius = sides[0] / (math.pi * 2)  # R = L/2π 0.95493

    def get_square(self):
        return math.pi * self.__radius ** 2  # Через радиус: P = 2πr 2.86479


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != 3:
            sides = [1]
            self.set_sides(*sides * 3)
        if not self.__is_possible(*sides):
            print(f'Невозможно построить треугольник из отрезков: {self.get_sides()}')
            del self  # почему не удаляет ссылку на обект ???

    @staticmethod
    def __is_possible(*sides):  # Проверка на возможность построения треугольника из отрезков "a > b + c"
        if len(sides) == 3:
            a, b, c = sides
            return (a < b + c) and (b < a + c) and (c < a + b)
        else:
            return False

    def get_square(self):
        p = sum(self.get_sides()) / 2  # вычисляем полупериметр
        a, b, c = self.get_sides()
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))  # вычисляем площадь
        print("Площадь треугольника:", s)  # выводим результат
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.set_sides(*sides * 12)
        else:
            sides = [1]
            self.set_sides(*sides * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6, 5)

Triangle2 = Triangle((200, 200, 100), 5, 10, 3)  # невозможный треугольник
Triangle1 = Triangle((200, 200, 100), 4, 3, 2, 5)
print(circle1.get_sides())

# print(cube1.get_sides())
# print(cube1.get_volume())

# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
