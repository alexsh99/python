with open('task_2.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        print(f"строка № {i}, слов в строке:  {len(line.split())}")
