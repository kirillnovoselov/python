"""
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open('subjects_file.txt', encoding='utf-8') as subjects_file:
    subjects_lines = subjects_file.readlines()

subjects_dict = dict()
for line in subjects_lines:
    subject = line.split()
    subject_name = subject[0]
    sum_lessons = sum([int(x[:x.find('(')]) for x in subject[1:] if '(' in x])
    subjects_dict[subject_name[:-1]] = sum_lessons
print(subjects_dict)