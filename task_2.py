from random import randint
start_list = [randint(1, 500) for _ in range(1, 20)]
print("Исходный список:\n", start_list, sep="")
new_list = (start_list[x] for x in range(1, len(start_list)) if start_list[x] > start_list[x - 1])
print("Элементы списка, значения которых больше предыдущего элемента:\n", list(new_list), sep="")
