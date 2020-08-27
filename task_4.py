replace_word = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыри"}
new_lines = []
with open("task_4.txt", "r", encoding="UTF-8") as file_1:
    for line in file_1:
        new_lines.append(replace_word[line.split()[0]] + " " + " ".join(line.split()[1:]) + "\n")

with open("task_4_1.txt", "w", encoding="UTF-8") as file_2:
    file_2.writelines(new_lines)
