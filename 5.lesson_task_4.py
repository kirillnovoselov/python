"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
num_dict = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
with open("one_four_file.txt", encoding='utf-8') as num_file:
    lines = num_file.readlines()

with open("rus_one_four_file.txt", "w", encoding='utf-8') as rus_num_file:
    for line in lines:
        for key, value in num_dict.items():
            if line.split()[0] == key:
                line = line.replace(line.split()[0], value)

        rus_num_file.write(line)

with open("rus_one_four_file.txt", encoding='utf-8') as rus_num_file:
    print(rus_num_file.read())
