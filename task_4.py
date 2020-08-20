def is_negative_number(n):
    try:
        return int(n) < 0
    except ValueError:
        return False


def is_positive_float(f):
    try:
        return float(f) > 0
    except ValueError:
        return False


def my_func(x, y):
    print(f'Вариант через ** = {float(x) ** int(y)}')
    p = 1
    for _ in range(abs(int(y))):
        p *= float(x)
    print(f'Вариант через цикл = {1 / p}')


n_1 = n_2 = 0

while True:
    n_1 = input("Действительное число: ")
    n_2 = input("Целое отрицательное число: ")
    if is_positive_float(n_1) and is_negative_number(n_2):
        break
    print('Неверные данные, повторите ввод')

my_func(n_1, n_2)
print(f'Для проверки через pow = {pow(float(n_1), int(n_2))}')
