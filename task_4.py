class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Машина: {self.name}, цвет: {self.color}")

    def go(self):
        print(f"Поехали")

    def stop(self):
        print("Остановилась")

    def turn(self, direction):
        print(f"Повернули на {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} !!! текущая скорость {self.speed}")
        else:
            super().show_speed()


class SportCar(Car):
    def drift(self):
        print("Дрифтим")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} !!! текущая скорость {self.speed}")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super(PoliceCar, self).__init__(speed, color, name, is_police)

    def flasher_on(self):
        print("Включили сирену")


car_1 = WorkCar(100, "red", "Хлебовоз")
car_1.go()
car_1.show_speed()
car_1.turn('лево')
car_1.stop()
print()

car_2 = TownCar(50, 'Синий', 'Миникупер')
car_2.go()
car_2.show_speed()
car_2.turn('право')
car_2.stop()
print()

car_3 = SportCar(50, 'Желтый', 'Ferrari')
car_3.go()
car_3.show_speed()
car_3.drift()
car_3.turn('право')
car_3.stop()
print()

car_4 = PoliceCar(50, 'Синий', 'Form')
car_4.go()
car_4.show_speed()
car_4.turn('право')
car_4.flasher_on()
car_4.stop()
print()
