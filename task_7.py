def fact(n: int):
    s = 1
    for i in range(1, n + 1):
        s *= i
        yield s


for el in fact(10):
    print(el)
