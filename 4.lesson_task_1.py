"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

"""
Parameters
work_time = 8, rate_per_hour = 500, bonus = 1000
"""
work_hours, rate_per_hour, bonus = map(float, sys.argv[1:])

salary = lambda work_hours, rate_per_hour, bonus: work_hours * rate_per_hour + bonus

print(f'ЗП сотрудника {salary(work_hours, rate_per_hour, bonus)}')
