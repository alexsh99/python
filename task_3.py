class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell if (self.cell - other.cell) >= 0 else other.cell - self.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell if (self.cell // other.cell) != 0 else other.cell // self.cell

    def __truediv__(self, other):
        return round(self.cell / other.cell if (self.cell / other.cell) <= 0 else other.cell / self.cell)

    def make_order(self, size):
        # как вариант
        # s = ""
        # for i in range(1, 1 + (self.cell // size)):
        #     s += ("*" * size) + "\n"
        # s += "*" * (self.cell % size)
        # return s
        return "\n".join(["*" * size for _ in range(self.cell // size)]) + "\n" + "*" * (self.cell % size)


c_1 = Cell(45)
c_2 = Cell(8)

print(f"Клетка 1: {c_1.cell}")
print(f"Клетка 2: {c_2.cell}")
print()
print(f"Сложение: {c_2 + c_1}")
print(f"Вычитание: {c_2 - c_1}")
print(f"Умножение: {c_2 * c_1}")
print(f"Деление с округлением до целого: {c_2 / c_1}")
print(f"Целочисленное деление :{c_2 // c_1}")
print()
print(f"Нарезка клетки 1 на 9 ячеек:", c_1.make_order(9), sep="\n")
print()
print(f"Нарезка клетки 2 на 3 ячейки:", c_2.make_order(3), sep="\n")