# Задание №1_Реализация выводв информации о промежутке времени в зависимости от
# его продолжительности в секундах.

duration = int(input('Введите продолжительность в секундах: '))

second = duration % 60
minute = (duration // 60) % 60
hour = (duration // 3600) % 24
day = (duration // 86400) % 365

if duration < 60:
    print(f'{second} сек')

elif duration >= 60 and duration < 3600:
    print(f'{minute} мин {second} сек')

elif duration >= 3600 and duration < 86400:
    print(f'{hour} ч {minute} мин {second} сек')

else:
    print(f'{day} д {hour} ч {minute} мин {second} сек')
