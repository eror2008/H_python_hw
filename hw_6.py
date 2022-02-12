# Python_homework_5

"""
1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
    ```
    Андрей Говорухи               6  6  1  4  9  9  10 4  8  2  3  8
    Василий Петров                2  9  4  7  6  6  3  6  5  5  2  4
    Гавриил Варфаломеев           10 10 4  10 7  9  4  6  8  1  1  1
    Игнат Тюльпанов               8  1  4  1  1  5  2  5  2  2  10 8
    Илья Муромцев                 1  6  4  7  10 9  5  3  7  4  7  2
    Кощей Бессмертный             3  10 1  4  1  8  10 6  2  10 7  4
    Максим Мухин                  10 8  9  9  5  8  6  5  7  2  4  10
    Маргарита Мартынова           9  1  5  1  10 10 2  4  4  9  8  10
    Петр Николаев                 2  9  5  9  1  2  8  7  8  1  9  1
    Полина Гусева                 9  2  8  7  3  9  9  5  1  9  2  6
    Спиридов Тереньтьев           4  7  7  3  10 9  7  2  10 9  8  1
    Станислав Трердолобов         8  1  6  1  4  1  10 8  8  1  8  8
    ```
    Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
    записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл":
    ```
    Говорухи А.         5.83
    Петров В.           4.92
    Варфаломеев Г.      5.92
    Тюльпанов И.        4.08
    Муромцев И.         5.42
    Бессмертный К.      5.5
    Мухин М.            6.92
    Мартынова М.        6.08
    Николаев П.         5.17
    Гусева Г.           5.83
    Тереньтьев С.       6.42
    Трердолобов С.      5.33
    ```
    Выравнивание колонок - желательно!
"""

print("Task_1 \n")

format_print = '{fio:<30} {avr_ball:>10.2}'

total = 0
count = 0

print('Список учеников у которых средний бал меньше 5:')

with open('file.txt', 'r') as src_file:
    while True:
        data = src_file.readline()
        if data:
            tmp_ls = data.strip('\n').split()
            full_name = tmp_ls[0]
            name = tmp_ls[0][0] + '.'
            first_name = tmp_ls[1]
            gpa = sum(list(map(int, tmp_ls[2:]))) / len(tmp_ls[2:])
            res_for_file = format_print.format(fio=first_name + ' ' + name, avr_ball=gpa)
            with open('new_file.txt', 'a') as new_src:
                new_src.writelines(res_for_file + '\n')
            res_on_screen = format_print.format(fio=first_name + ' ' + full_name, avr_ball=gpa)
            if gpa < 5:
                print('\t', res_on_screen)
            total += gpa
            count += 1
        else:
            break

print('\n Средний балл по классу:', round(total / count, 2))

print("#" * 30, '\n')

"""
2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
"""
print("Task_2 \n")


def user_info():
    while True:
        res = input('Input something: ')
        with open('input.txt', 'a') as new_file:
            new_file.writelines(res + '\n')
        if not res:
            break
    return


user_info()
