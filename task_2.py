from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def fabric_calculation(self):
        pass

    def __add__(self, other):
        return self.fabric_calculation + other.fabric_calculation


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_calculation(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def fabric_calculation(self):
        return 2 * self.growth + 0.3


coat_1 = Coat(42)
print(f"Расход ткани на пальто 42 размера составит: {coat_1.fabric_calculation:.3f}")

costume_1 = Costume(174)
print(f"Расход ткани на костюм для роста 174 составит: {costume_1.fabric_calculation:.3f}")

print(f"Общий расход ткани: {costume_1 + coat_1:.3f}")
