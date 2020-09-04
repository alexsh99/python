class Worker:
    """
    Базовый класс `работник` (Worker)
    атрибуты:
    name - Имя
    surname - Фамилия
    position - Должность
    wage - Оклад
    bonus - премия
    """

    def __init__(self, name, surname, position, wage, bonus):
        """
        Инициализация атрибутов класса
        Worker(name, surname, position, wage, bonus)
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


people_1 = Position("Вася", "Пупкин", "директор", 25000, 15000)
print(f"ФИО: {people_1.get_full_name()} в должности {people_1.position} c доходом {people_1.get_total_income()}")
people_2 = Position("Иван", "Иванов", "дворник", 15000, 50000)
print(f"ФИО: {people_2.get_full_name()} в должности {people_2.position} c доходом {people_2.get_total_income()}")
