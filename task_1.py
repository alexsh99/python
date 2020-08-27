import sys
lines = []
print("Запись данных в файл построчно. Окончание ввода - пустая строка.")
for line in sys.stdin:
    if line == '\n':
        break
    lines.append(line)
with open("task_1.txt", 'w', encoding='UTF-8') as file:
    file.writelines(lines)
