# Дополнительное практическое задание по модулю: "Наследование классов."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = [*sides]
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
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

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            print(self.__is_valid_sides(*new_sides))
            self.__sides = [*new_sides]
        else:
            print('Количество сторон не верно')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides


class Cube(Figure):
    sides_count = 12


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
