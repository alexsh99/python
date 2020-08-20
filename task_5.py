result = 0
stop_flag = False
while not stop_flag:
    string = input("Ввод: (для завершения Q) ")
    for i in string.split():
        try:
            result += float(i)
        except ValueError:
            if i.upper() == "Q":
                stop_flag = True
    print(f"Результат суммы: {result}")
