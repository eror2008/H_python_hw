# Python_homework_3

# Task_1
# У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [10, 25, 37, 46, 58, 64, 88, 95, 100, 115, 118, 123, 129, 135, 145, 155, 160]
for num in my_list:
    if num > 100:
        print(num)

print("#" * 30, '\n')

# Task_2
# У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [10, 25, 37, 46, 58, 64, 88, 95, 100, 110, 117, 124, 130, 140, 155, 166, 174]
my_results = [num for num in my_list if num > 100]
print(my_results)

print("#" * 30, '\n')

# Task_3
# У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

ans = 1
my_list = []

while ans == 1:
    while True:
        try:
            num = int(input("Введите целое число:"))
            if num == type(int):
                raise ValueError
            break
        except ValueError:
            print("Error: Вы ввели не целое число. Введите число без '.')")
    if num is not None:
        my_list.append(num)
        print("Число", num, "добавлено в список.")
    ans = int(input("Хотите ввести ещё число? 1. - Да. 2. - Нет. "))

if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

print("#" * 30, '\n')

# Task_4
# У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))

my_string = '0123456789'
my_ls = []
for symb_1 in my_string:
    for symb_2 in my_string:
        my_ls.append(int(symb_1 + symb_2))
print(my_ls)
