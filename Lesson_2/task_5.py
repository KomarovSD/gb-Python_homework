# Задача №5.Создать список, содержащий цены на товары (10–20 товаров), например:[57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.
# Подумать, как из цены получить рубли и копейки, как добавить нули,# если, например, получилось 7 копеек или 0 копеек.
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Вывести цены этих товаров по возрастанию, написав минимум кода.

init_list = [57.8, 46.51, 97, 76.05, 13.11, 87.93, 27, 97.09, 0.16, 42,
             96.64, 34.17, 97.45, 40.62, 84.94, 7, 52.23, 93.74, 89, 3.93]

source_id = id(init_list)
print(init_list)
print(f"{'':-^80}")

end_word = ", "
for i, num in enumerate(init_list):

    price = str(f"{float(num):.2f}").split(".")
    if i == len(init_list) - 1:
        end_word = "\n"
    print(f"{price[0]} руб {price[1]} коп", end=end_word)

print(f"{'':-^80}")

print(f"id до сортировки {source_id}")
init_list.sort()
print(init_list)
print(f"id после сортировки {id(init_list)}")

if source_id == id(init_list):
    print("Identically")
else:
    print("Different")

print(f"{'':-^80}")

copy_of_list = init_list[:]
copy_of_list.sort(reverse=True)
print(copy_of_list)
print(source_id)
print(id(copy_of_list))

if source_id == id(copy_of_list):
    print("Identically")
else:
    print("Different")

print(f"{'':-^100}")
print("Пять самых дорогих товаров", init_list[-6:-1])
