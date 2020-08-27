import json
firm_dict = {}
average_profit = []
with open('text_7.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        try:
            data = line.split()
            profit = int(data[2]) - int(data[3])
            if profit > 0:
                average_profit.append(profit)
            firm_dict[data[0]] = profit
        except ValueError:
            pass
with open('task_7.json', 'w', encoding="UTF-8") as w_file:
    json.dump([firm_dict, {"average_profit": sum(average_profit) / len(average_profit)}], w_file, indent=4, ensure_ascii=False)
