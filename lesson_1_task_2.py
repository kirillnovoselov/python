# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
import datetime

seconds = int(input('Введите время в секундах: '))

a = str(datetime.timedelta(seconds=seconds))
print(a)  # Проверка ответа.

hours = seconds // 3600
print(hours)

min = (seconds % 3600) // 60
print(min)

sec = ((seconds % 3600) % 60) // 1
print(sec)

print(f"Время в часах:минутах:секундах {hours}:{min}:{sec}")


