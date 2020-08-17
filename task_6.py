products = []
index = 1
while True:
    print("1 - Добавить товар", "2 - Аналитика", "3 - Список товаров", "q - Выход", sep="\n")
    m_index = input(": ")
    if m_index == "q":
        break
    elif m_index == "1":
        name = input("Название:")
        price = input("Цена:")
        count = input("Количество:")
        unit = input("ед:")
        products.append((index, {"название": name, "цена": price, "количество": count, "ед": unit}))
        index += 1
    elif m_index == "2":
        obj = {"название": [], "цена": [], "количество": [], "ед": []}
        for row in products:
            obj["название"].append(row[1]["название"])
            obj["цена"].append(row[1]["цена"])
            obj["количество"].append(row[1]["количество"])
            obj["ед"].append(row[1]["ед"])
            obj["название"] = list(set(obj["название"]))
            obj["цена"] = list(set(obj["цена"]))
            obj["количество"] = list(set(obj["количество"]))
            obj["ед"] = list(set(obj["ед"]))
        print(obj)
    elif m_index == "3":
        for row in products:
            print(row)
