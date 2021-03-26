"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def ligth_turn(self):
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(7)

traffic_lights = TrafficLight()
traffic_lights.ligth_turn()
