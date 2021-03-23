"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
"""

input_file = open('input_file.txt', "w")

while True:
    input_line = input("Введите текстовую строку (для выхода жми пробел) ")
    if input_line == ' ':
        break
    else:
        input_file.write(input_line + "\n")

input_file = open('input_file.txt')
content = input_file.read()
input_file.close()
print(content)
