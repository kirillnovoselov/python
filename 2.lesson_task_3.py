# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
#
month_num = int(input('Введите номер месяца от 1 до 12 '))

# Решение через dict:

month_dic = {"зима":{12, 1, 2}, "весна":{3, 4, 5}, "лето":{6, 7, 8}, "осень":{9, 10, 11}}

for key, value in month_dic.items():
    if month_num in value:
        print(key)

# Решение через list:
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
season_list = ["зима", "весна", "лето", "осень"]

for month in winter_list:
    if month_num == month:
        print(season_list[0])
for month in spring_list:
    if month_num == month:
        print(season_list[1])
for month in summer_list:
    if month_num == month:
        print(season_list[2])
for month in autumn_list:
    if month_num == month:
        print(season_list[3])

