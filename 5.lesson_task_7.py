"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
with open("firms_list.txt", encoding="utf-8") as firms_list:
    firms_lines = firms_list.readlines()

firms_dict = dict()
profit_list = []
for line in firms_lines:
    firm_name, form, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    firms_dict[firm_name] = profit
    if profit > 0:
        profit_list.append(profit)
average_profit = sum(profit_list) / len(profit_list)
result_dict = [firms_dict, {"average_profit" : average_profit}]

with open('firms_list.json', "w") as write_f:
    json.dump(result_dict, write_f)

with open('firms_list.json') as read_f:
    data = json.load(read_f)
print(data)