#Задача №2. Дан список:[]
#Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
#(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
#до двух целочисленных разрядов.
#Сформировать из обработанного списка строку.


init_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(init_list)
print(id(init_list))
print(f"{'':-^80}")

for i in range(len(init_list)):
    elem = init_list.pop(0)
    if elem.isdigit():
        init_list.append(f'{int(elem):02d}')
    elif elem[0] == "+" and elem[1].isdigit():
        init_list.append(f'+{int(elem):02d}')
    else:
        init_list.append(elem)

i = 0
while i < len(init_list):
    value = init_list[i]
    if value.isdigit() or (value and value[1:].isdigit()):
        init_list.insert(i, '"')
        init_list.insert(i + 2, '"')
        i += 2
    i += 1

print(init_list)
print(f"{'':-^80}")
print(' '.join(init_list))
print(id(init_list))
