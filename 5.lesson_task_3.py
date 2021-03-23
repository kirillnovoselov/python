"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
employee_rate.txt:
Иванов 23543.12
Петров 13749.32
Сидоров 43323.23
Смирнов 24567.65
Кузнецов 13907.43
Попов 32456.09
Васильев 8215.66
Соколов 9768.44
Михайлов 10000.01
Новиков 9999.99
"""

with open("employee_rate.txt", encoding='utf-8') as employee_rate:
    employee_rate_list = employee_rate.readlines()

employee_rate_less_20000 = []
salary_list = []
for line in employee_rate_list:
    # print(line)
    name, salary = line.split()
    salary_list.append(float(salary))
    if float(salary) < 20000:
        employee_rate_less_20000.append(name)
print(f' Список сотрудников с окладом менее 20000 {employee_rate_less_20000}')
print(f' Средняя величина дохода всех сотрудников {sum(salary_list) / len(salary_list)}')

