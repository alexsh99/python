import re
my_dict = {}
with open("text_6.txt", "r", encoding="UTF-8") as file:
    for line in file:
        d = line.split()[0][:-1]
        my_dict[d] = sum(map(int, re.findall(r'\d+', line)))
print(my_dict)
