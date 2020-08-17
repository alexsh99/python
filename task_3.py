season_list = ["Зима", "Весна", "Лето", "Осень"]
season_dict = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень"}
while True:
    month = input("Номер месяца от 1 до 12 (q для выхода): ")
    if month == "q":
        break
    elif not month.isdecimal() or int(month) < 1 or int(month) > 12:
        continue
    ind = int(month) // 3 if int(month) // 3 != 4 else 0
    print(season_list[ind])
#    print(season_dict[ind]) #
