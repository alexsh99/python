def m_divide(dividend, divider):
    """Деление чисел. Возвращает часное или None в случаии деления на 0
    или если агрументы не приводятся к типу float

    Аргументы:
    dividend - делимое. тип float или str
    divider - делитель. тип float или str

    Пример:
    m_divide('100', 20) => 5.0
    m_divide(9.99, 3) => 3.33
    m_divide('asd', '20') => None
    m_divide(100, 0) => None
    """

    try:
        return float(dividend) / float(divider)
    except ZeroDivisionError:
        return None
    except ValueError:
        return None


div_1 = input("Делимое: ")
divisor = input("Делитель: ")

print(m_divide(div_1, divisor))
