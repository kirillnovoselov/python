"""
Реализовать базовый класс Worker (работник).

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных:
создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income_wage, "bonus": income_bonus}

class Position(Worker):

    def get_full_name(self):
        self.full_name = 'Имя сотрудника: ' + self.name + ' ' + self.surname
        return self.full_name

    def get_total_income(self):
        self.total_income = 'Доход сотрудника с учётом премии: ' \
                            + str(self._income.get("wage") + self._income.get("bonus"))
        return self.total_income

manager = Position('Ivan', "Ivaniv", "manager", 50000, 10000)
print(manager.get_full_name())
print(manager.get_total_income())
