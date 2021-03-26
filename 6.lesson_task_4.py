"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}!')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 60:
            print(f'Превышение скорости в 60 км\ч!')

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 40:
            print(f'Превышение скорости в 40 км\ч!')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

town_car = TownCar(90, 'Синяя', 'Городская машина', False)
work_car = WorkCar(80, 'Серая', 'Рабочая машина', False)
sport_car = SportCar(130, 'Красная', 'Спортивная машина', False)
police_car = PoliceCar(110, 'Белая', 'Полицейская машина°', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('направо')