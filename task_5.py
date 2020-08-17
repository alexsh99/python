rate = [7, 5, 3, 3, 2]
while True:
    print('Текущий рейтинг: ', rate)
    el = input("Элемент рейтинга(натуральное число, q - Выход): ")
    if el == "q":
        break
    elif int(el) in rate:
        rate.insert(rate.index(int(el)) + rate.count(int(el)), int(el))
    elif rate[0] < int(el):
        rate.insert(0, int(el))
    elif rate[-1] > int(el):
        rate.append(int(el))
    else:
        for ind in range(len(rate) - 1):
            if rate[ind] > int(el) > rate[ind + 1]:
                rate.insert(ind + 1, int(el))
