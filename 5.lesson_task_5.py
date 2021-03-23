"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

with open("task_5.txt", "w", encoding='utf-8') as nums_list:
    input_nums = input("Введите целые числа через пробел ")
    nums_list.write("Введеные числа " + input_nums + '\n')
    sum_nums = sum(map(int, input_nums.split()))
    nums_list.writelines('Ссумма введенных чисел равна ' + str(sum_nums))

with open("task_5.txt", encoding='utf-8') as nums_list:
    print(nums_list.read())
