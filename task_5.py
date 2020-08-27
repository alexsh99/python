from random import randint
set_numbers = [str(randint(1, 100)) for _ in range(100)]

with open("task_5.txt", "w+", encoding="UTF-8") as file:
    file.writelines(" ".join(set_numbers))
    file.seek(0)
    numbers = list(map(int, file.read().split()))

print(f"сумма чисел в файле: {sum(numbers)}")
