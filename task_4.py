s_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходный список:\n", s_list, sep="")
n_list = (el for el in s_list if s_list.count(el) == 1)
print("Элементы списка, не имеющие повторений:\n", list(n_list), sep="")
