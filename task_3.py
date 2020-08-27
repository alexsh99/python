persons = {}
with open("task_3.txt", "r", encoding="UTF-8") as file:
    for line in file:
        f_line = line.split()
        persons[f_line[0]] = float(f_line[1])
        if float(f_line[1]) <= 20000:
            print(f"{f_line[0]} - {f_line[1]}")

print(f"Средний оклад сотрудников: {sum(persons.values()) / len(persons) :.02f}")
