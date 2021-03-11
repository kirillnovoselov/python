"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

divisible = float(input('Введите число, которое будет делимым '))
divisor = float(input('Введите число, которое будет делителем '))

while True:
    if divisor != 0:
        break
    else:
        divisor = float(input('На ноль не делится. Введите число, которое будет делителем (не ноль!) '))


def division_func(div, div_r):

    quotient = div / div_r
    return quotient


print(division_func(divisible, divisor))
