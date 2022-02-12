# Python_homework_5

"""
1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
в) Посчитать среднее количество лет всех людей из списка.
"""
from random import randint
import names  # pip install names

print("Task_1 \n")

persons = []
for i in range(10):
    person = {
        "name": names.get_first_name(),
        "age": randint(1, 110),
    }
    persons.append(person)
print(persons)

min_age = min([persons[man]["age"] for man in range(len(persons))])
man_name = max([len(persons[i]["name"]) for i in range(len(persons))])
persons_name = [persons[man]["name"] for man in range(len(persons)) if persons[man]["age"] == min_age]
max_name = [persons[i_name]["name"] for i_name in range(len(persons)) if
            len(persons[i_name]["name"]) == man_name]
average_amount = sum([persons[index_age]["age"] for index_age in range(len(persons))]) / len(persons)

print("youngest:", *persons_name)
print("longest name:", *max_name)
print("average age:", average_amount)

print('#' * 30, '\n')

"""
2. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""
print("Task_2 \n")


def create_ls(some_str_1, some_str_2):
    res_ls = [symbol for symbol in set(some_str_1) if symbol in set(some_str_2)]
    return res_ls


print(create_ls(some_str_1="asaszxc", some_str_2="asasdf"))

print('#' * 30, '\n')
"""
3. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
"""

print("Task_3 \n")


def create_ls(some_str_1, some_str_2):
    res_ls = [symbol for symbol in some_str_1 if some_str_1.count(symbol) == 1 and some_str_2.count(symbol) == 1]
    return res_ls


print(create_ls(some_str_1="asaszxcdf", some_str_2="asasdf"))

print('#' * 30, '\n')

"""
4. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.

Пример использования функции:
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
"""

import random
import string

print("Task_4 \n")


def create_email(ls_1, ls_2):
    return random.choice(ls_2) + '.' + str(random.randint(100, 999)) + '@' + \
           ''.join(random.choice(string.ascii_lowercase) for _ in range(0, random.randint(5, 7))) + \
           '.' + random.choice(ls_1)


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
