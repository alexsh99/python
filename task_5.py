class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):

    def draw(self):
        print(f"Напишем {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Рисуем {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"Выделяем {self.title}")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
pen.draw()
pencil.draw()
handle.draw()
