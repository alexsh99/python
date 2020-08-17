my_list = []
while True:
    el = input("Элемент. Для завершения ввода - \\end ")
    if el == "\\end":
        break
    my_list.append(el)

print(my_list)
for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)
