from functools import reduce

s_list = (el for el in range(100, 1001) if el % 2 == 0)
val = reduce(lambda a, x: a * x, s_list)
print(val)
