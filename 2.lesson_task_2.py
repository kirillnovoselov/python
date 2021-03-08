# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

num_list = list(input("Введите список из чисел"))
# num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print(num_list)
lengh = len(num_list) - 1
i = 0
while i <= lengh:
    try:
        first_num = num_list[i]
        sec_num = num_list[i+1]
        num_list[i] = sec_num
        num_list[i + 1] = first_num
        i+=2
    except:
        break

print(num_list)


