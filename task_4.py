word = input("Строка: ")
w_list = word.split()
for ind, el in enumerate(w_list):
    print(ind + 1, el[:10])
