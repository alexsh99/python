from itertools import count, cycle, takewhile
from random import randint

my_list = list(randint(1, 20) for _ in range(5))
a = count(3)
b = cycle(my_list)

print("Итератор, генерирующий целые числа, начиная с указанного (3), стоп на 10\n")
for i in takewhile(lambda x: x <= 10, a):
    print(i)
print("\nИтератор, повторяющий элементы писка, определенного заранее (повтор 3 раза) \n", f"Список: {my_list}", sep="")
ind = 0
for j in takewhile(lambda _: ind <= len(my_list) * 3, b):
    print(j)
    ind += 1
