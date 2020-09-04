class Road:
    """Класс `дорога` (Road) - атрибуты `длина` и `ширина` в метрах"""
    def __init__(self, length: int, width: int):
        """Инициализация класса. length(длина) в метрах, width(ширина) в метрах"""
        self._length = length
        self._width = width

    def asphalt_need(self, thickness: int):
        """
        расчета массы асфальта, необходимого для покрытия всего дорожного полотна в тоннах
        thickness - толщина слоя в сантиметрах
        возвращает - массу необходимого асфальта в тоннах
        """
        return self._length * self._width * 25 * thickness / 1000


road_1 = Road(5000, 20)
print(f"Масса асфальта, для покрытия всего дорожного полотна толщиной 5 см составляет: {road_1.asphalt_need(5)} тонн")
