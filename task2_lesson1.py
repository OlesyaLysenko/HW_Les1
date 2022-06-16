# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_sec = int(input('Введите время в секундах: '))
time_hours = time_sec // 3600
time_hours = time_hours % 24

time_minuts = time_sec // 60
time_minuts = time_minuts % 60

time_sec = time_sec % 60

print(f"{time_hours}:{time_minuts}:{time_sec}")