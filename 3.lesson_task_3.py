"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""
arg_1 = 4
arg_2 = 2
arg_3 = 6


def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    arg_list.sort(reverse=True)
    sum_max_two_arg = sum(arg_list[0:2])
    return sum_max_two_arg


print(my_func(arg_1, arg_2, arg_3))
