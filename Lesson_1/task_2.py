# Задание №2_Создание списка, состоящего из кубов нечетных чисел от 1 до 1000; вычисление суммы тех чисел
# из этого списка, сумма цифр которого делиться нацело на 7; добавление к каждому элементу списка 17 и
# заново вычислить сумму тех чисел из списка.

my_list = []
all_sum = 0
n_sum = 0
a_sum = 0
all_sum_a = 0

for i in range(1, 1001, 2):
    my_list.append(i ** 3)

for n in my_list:
    all_n = n

    while n > 0:
        number = n % 10
        n_sum = n_sum + number
        n = n // 10

    if n_sum % 7 == 0:
        all_sum = all_sum + all_n

    else:
        n_sum = 0

for a in my_list:
    a += 17
    all_a = a
    while a > 0:
        number = a % 10
        a_sum = a_sum + number
        a = a // 10
    if a_sum % 7 == 0:
        all_sum_a = all_sum_a + all_a
    else:
        a_sum = 0

print(my_list)
print(all_sum)
print(all_sum_a)
