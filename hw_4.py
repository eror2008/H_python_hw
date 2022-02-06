# Python_homework_4

"""
1. Дано целое число (int). Определить сколько нулей в этом числе.
"""
import random

print("Task_1")

values = random.randint(0, 999999)
print(values)
print(f"Количество '0' в числе: {str(values).count('0')}")

print("#" * 40, "\n")

"""
2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
"""
import random

print("Task_2")

num = random.randint(0, 9999999)
print(num)
values = str(num)
print(f"Количество '0' в конце числа: {len(values) - len(values.rstrip('0'))}")

print("#" * 40, "\n")


"""
3. Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить
элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
"""
import random

print("Task_3")

my_list_1, my_list_2 = [random.randint(0, 200) for _ in range(20)], [random.randint(0, 200) for _ in range(20)]
print(f"{my_list_1=}\n{my_list_2=}")
even_num = [my_list_1[i] for i in range(len(my_list_1)) if my_list_1[i] % 2 == 0]
odd_num = [my_list_2[i] for i in range(len(my_list_2)) if my_list_2[i] % 2 == 1]
my_result = even_num + odd_num
print(f"{my_result=}")

print("#" * 40, "\n")

"""
4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
"""
import random

print("Task_4")


my_list = [random.randint(0, 200) for _ in range(4)]
print(f"{my_list=}")
new_list = my_list[1:] + [my_list[0]]
print(f"{new_list=}")

print("#" * 40, "\n")

"""

5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
"""

print("Task_5")

my_list = [1, 2, 3, 4]
print(my_list)
list_value = my_list.pop(0)
my_list.append(list_value)
print(my_list)

print("#" * 40, "\n")

"""

6. Дана строка в которой есть числа (разделяются пробелами).
Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
Для данного примера ответ - 133. (используйте split и проверку isdigit)
"""
print("Task_6")

my_string = "43 больше чем 34 но меньше чем 56"
my_str_ls = my_string.split()
counter = 0
for i in my_str_ls:
    if i.isdigit():
        counter += int(i)
print("Result: ", counter)

print("#" * 40, "\n")

"""
7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
"""

print("Task_7")

my_str = "My long string"
l_limit, r_limit = "o", "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]

s_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]

print(sub_str)

print("#" * 40, "\n")


"""

8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
(используйте срезы длинны 2)
"""
import random

print("Task_8")

my_str = random.choice('Разделите эту строку на пары из двух символов и поместите эти пары в список'.split())

result_list = []
str_len = len(my_str)

print([my_str[i: i + 2].ljust(2, '_') for i in range(0, str_len, 2)])

print("#" * 40, "\n")

"""

9. Дан список чисел. Определите, сколько в этом списке элементов,
которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
"""
import random

print("Task_9")

my_ls = [random.randint(0, 100) for _ in range(20)]
print(my_ls)
counter = 0
for i in range(0, len(my_ls) -1):
    if my_ls[i] > sum([my_ls[i - 1] + my_ls[i + 1]]):
        counter += 1
print(f"Result: {counter}")
