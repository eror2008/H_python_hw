class Notebook:
    def __init__(self, note: dict):
        self.note_dict = note

    @staticmethod
    def print_formatted(message_info):
        print('-' * 25)
        print(message_info)
        print('-' * 25)

    def start(self):
        try:
            file = open('notes.txt', 'r', encoding='utf-8')
            notes_lst = file.readlines()
            file.close()
            if len(notes_lst) == 0:
                print("ФАЙЛ ПУСТОЙ.")
            else:
                if len(notes_lst) % 10 == 1:
                    print(f"ЗАГРУЖЕНО: {len(notes_lst)} ЗАПИСЬ")
                elif len(notes_lst) % 10 == [2, 3, 4]:
                    print(f"ЗАГРУЖЕНО: {len(notes_lst)} ЗАПИСИ")
                else:
                    print(f"ЗАГРУЖЕНО: {len(notes_lst)} ЗАПИСЕЙ")
        except FileNotFoundError:
            print("ФАЙЛ 'notes.txt' НЕ НАЙДЕН...\nДОБАВЬТЕ НОВУЮ ЗАПИСЬ(№1 в МЕНЮ), ЧТОБЫ ФАЙЛ СОЗДАЛСЯ.\n")

        print("ОСНОВНОЕ МЕНЮ:\n"
              "1: Добавить запись\n"
              "2: Удалить запись\n"
              "3: Изменить запись\n"
              "4: Поиск\n"
              "5: Сортировка\n"
              "6: Выход\n")

        while True:
            try:
                num_of_operation = int(input("Сделайте Ваш выбор>"))
                if num_of_operation == 1:
                    self.add_note()
                elif num_of_operation == 2:
                    self.delete_note()
                elif num_of_operation == 3:
                    self.edit_note()
                elif num_of_operation == 4:
                    self.search()
                elif num_of_operation == 5:
                    self.sort()
                elif num_of_operation == 6:
                    self.exit()
                else:
                    print("Ошибка! Здесь такой цифры нет!\n"
                          "Доступные функциональные номера: 1, 2, 3, 4, 5 и 6")
                    continue
                break
            except ValueError:
                print("Ошибка! То, что вы ввели не является числом!\n"
                      "Доступные функциональные номера: 1, 2, 3, 4, 5 и 6")
                continue

    @staticmethod
    def exit():
        exit()

    @staticmethod
    def __list_of_str_to_list_of_dict(list_of_notes):
        # преобразуем в список со списками
        list_of_lst_notes = []
        for i in list_of_notes:
            list_of_lst_notes.append(i.split(','))
        # убираем лишнии символы
        signs = ["'", '{', '}', ':', ',', '\n']
        for i in range(len(list_of_lst_notes)):
            for j in range(len(list_of_lst_notes[i])):
                for e in range(len(list_of_lst_notes[i][j])):
                    for s in range(len(signs)):
                        if list_of_lst_notes[i][j][e] == signs[s]:
                            list_of_lst_notes[i][j] = list_of_lst_notes[i][j].replace(signs[s], ' ')
        # создаем список со списками из списков
        for i in range(len(list_of_lst_notes)):
            for j in range(len(list_of_lst_notes[i])):
                list_of_lst_notes[i][j] = list_of_lst_notes[i][j].split()
        # преобразуем элементы(списки со списками) списка в словари
        # получаем список из словарей
        list_of_dict_notes = []
        for i in range(len(list_of_lst_notes)):
            note_dict = {list_of_lst_notes[i][j][0]: list_of_lst_notes[i][j][-1]
                         for j in range(len(list_of_lst_notes[i]))}
            list_of_dict_notes.append(note_dict)
        return list_of_dict_notes

    def add_note(self):
        print("\nДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ:")
        print("Поля со * ОБЯЗАТЕЛЬНЫ к заполнению!")
        while True:
            first_name = input("*Введите Имя: ")
            if first_name == "":
                print("Это поле ОБЯЗАТЕЛЬНО к заполнению!")
                continue
            else:
                break

        while True:
            last_name = input("*Введите Фамилию: ")
            if last_name == "":
                print("Это поле ОБЯЗАТЕЛЬНО к заполнению!")
                continue
            else:
                break

        while True:
            phone_number = input("*Введите Номер Телефона: ")
            if phone_number == "":
                print("Это поле ОБЯЗАТЕЛЬНО к заполнению!")
                continue
            else:
                break

        while True:
            adress = input("Введите Адрес: ")
            if ' ' in adress or ',' in adress:
                print("ПОЖАЛУЙСТА, Введите адрес в одну строку:\nбез пробелов и запятых")
                continue
            else:
                break
        if adress == '':
            adress = 'Адрес'

        birthday = input("Введите Дату Рождения: ")
        if birthday == '':
            birthday = 'Дата_Рождения'

        self.note_dict = {
            "Имя": first_name,
            "Фамилия": last_name,
            "Номер_телефона": phone_number,
            "Адрес": adress,
            "Дата_Рождения": birthday
        }

        # Запись в файл
        file = open("notes.txt", 'a', encoding='utf-8')
        file.write(f"{str(self.note_dict)}\n")
        file.close()

        self.print_formatted("НОВАЯ ЗАПИСЬ СОХРАНЕНА!")
        self.start()


    def delete_note(self):
        self.print_formatted("УДАЛЕНИЕ ЗАПИСИ:")
        file = open("notes.txt", 'r+', encoding='utf-8')
        file_notes = file.read()
        file.close()
        if file_notes == "":
            print("ФАЙЛ ПУСТОЙ. УДАЛЯТЬ НЕЧЕГО.")
        else:

            file = open("notes.txt", 'r', encoding='utf-8')

            print("ДОСТУПНЫЕ ЗАПИСИ:")
            count = 0
            notes_lst = []
            for line in file:
                print(f"{count}:\n{line}")
                notes_lst.append(line)
                count += 1

            file.close()
            print("\n*Для возвращения обратно в меню напишите - 'menu'")
            while True:
                try:
                    num_of_del_note = input("ВВЕДИТЕ НОМЕР ЗАПИСИ ДЛЯ УДАЛЕНИЯ:")
                    if num_of_del_note == 'menu':
                        self.start()
                        break
                    else:
                        num_of_del_note = int(num_of_del_note)
                        notes_lst.remove(notes_lst[num_of_del_note])

                        file = open("notes.txt", 'w',
                                    encoding='utf-8')
                        for i in notes_lst:
                            file.write(i)
                        file.close()
                        self.print_formatted("ЗАПИСЬ УСПЕШНО УДАЛЕНА!")
                        break
                except (ValueError, IndexError):
                    print("ОШИБКА!\n")
                    continue
        self.start()


    def edit_note(self):
        self.print_formatted("ИЗМЕНЕНИЕ ЗАПИСИ:")

        file = open("notes.txt", 'r+', encoding='utf-8')
        file_notes = file.read()
        if file_notes == "":
            print("ФАЙЛ ПУСТОЙ. ИЗМЕНЯТЬ НЕЧЕГО.")
            file.close()
            self.start()
        else:
            file.close()
            file = open("notes.txt", 'r', encoding='utf-8')

            self.print_formatted("ДОСТУПНЫЕ ЗАПИСИ:")
            count = 0
            notes_lst = []
            for line in file:
                print(f"{count}:\n{line}")
                notes_lst.append(line)
                count += 1
            file.close()

            print("\n*Для возвращения обратно в меню напишите - "
                  "menu")
            while True:
                try:
                    num_of_edit_note = input("ВВЕДИТЕ НОМЕР ЗАПИСИ ДЛЯ ИЗМЕНЕНИЯ:")
                    if num_of_edit_note == 'menu':
                        self.start()
                        break
                    else:
                        num_of_edit_note = int(num_of_edit_note)
                        print(f"Выбранная вами запись:\n{notes_lst[num_of_edit_note]}")
                        editing_note_lst = notes_lst[num_of_edit_note].split(',')

                        signs = ["'", '{', '}', ':', ',', '\n']

                        for i in range(len(editing_note_lst)):
                            for j in range(
                                    len(editing_note_lst[i])):
                                for s in range(len(signs)):
                                    if editing_note_lst[i][j] == signs[s]:
                                        editing_note_lst[i] = editing_note_lst[i].replace(signs[s], ' ')
                        for i in range(len(editing_note_lst)):
                            editing_note_lst[i] = editing_note_lst[i].split()
                        editing_note_dict = {editing_note_lst[i][0]: editing_note_lst[i][-1]
                                             for i in range(len(editing_note_lst))}
                        count = 1
                        for k in editing_note_dict:
                            print(f"{count}. {k}")
                            count += 1
                        while True:
                            try:
                                num_of_editing_point = int(input("Введите номер пункта, который хотите поменять:"))
                                if num_of_editing_point == 1:
                                    while True:
                                        first_name = input("*Новое Имя:")
                                        if first_name == '':
                                            print("Вы ничего не ввели...")
                                            continue
                                        else:
                                            break
                                    editing_note_dict['Имя'] = first_name
                                    break
                                elif num_of_editing_point == 2:
                                    while True:
                                        last_name = input("*Новая Фамилия:")
                                        if last_name == '':
                                            print("Вы ничего не ввели...")
                                            continue
                                        else:
                                            break
                                    editing_note_dict['Фамилия'] = last_name
                                    break
                                elif num_of_editing_point == 3:
                                    while True:
                                        phone_number = input("*Новый Номер Телефона:")
                                        if phone_number == '':
                                            print("Вы ничего не ввели...")
                                            continue
                                        else:
                                            break
                                    editing_note_dict['Номер_телефона'] = phone_number
                                    break
                                elif num_of_editing_point == 4:
                                    while True:
                                        adress = input("Введите Адрес: ")
                                        if ' ' in adress or ',' in adress:
                                            print("ПОЖАЛУЙСТА, Введите адрес в одну строку:\nбез пробелов и запятых")
                                            continue
                                        elif adress == "":
                                            print("Вы ничего не ввели...")
                                            continue
                                        else:
                                            break
                                    editing_note_dict['Адрес'] = adress
                                    break
                                elif num_of_editing_point == 5:
                                    while True:
                                        birthday = input("*Новая Дата Рождения:")
                                        if birthday == '':
                                            print("Вы ничего не ввели...")
                                            continue
                                        else:
                                            break
                                    editing_note_dict['Дата_Рождения'] = birthday
                                    break
                                else:
                                    print("ОШИБКА!\nЗдесь такой цифры нет!\n"
                                          "Доступные функциональныеномера:1, 2, 3, 4 и 5")
                                    continue

                            except ValueError:
                                print("ОШИБКА!")
                                continue

                        file = open('notes.txt', 'r', encoding='utf-8')
                        notes_lst = []
                        for line in file:
                            notes_lst.append(line)
                        file.close()

                        notes_lst[num_of_edit_note] = str(editing_note_dict) + "\n"
                        file = open('notes.txt', 'w', encoding='utf-8')
                        for i in notes_lst:
                            file.write(i)
                        file.close()
                        self.print_formatted("ЗАПИСЬ УСПЕШНО ИЗМЕНЕНА!")
                        break
                except ValueError:
                    print("ОШИБКА!\nТо, что вы ввели не является числом!\n"
                          "Доступные функциональныеномера:1, 2, 3, 4 и 5")
                    continue
        self.start()

    def search(self):
        self.print_formatted("ПОИСК ЗАПИСИ")
        searching_dict = {
            1: "Поиск по Имени",
            2: "Поиск по Номеру Телефона"
        }
        for k, v in searching_dict.items():
            print(f"{k}. {v}")

        # открываем файл сохраняем все записи в виде списка строк

        file = open("notes.txt", 'r+', encoding="utf-8")
        list_of_notes = file.readlines()
        file.close()
        list_of_dict_notes = self.__list_of_str_to_list_of_dict(list_of_notes)

        while True:
            try:
                num_of_searching = int(input("==>"))
                if num_of_searching == 1:
                    self.print_formatted("ПОИСК ПО ИМЕНИ")
                    searching_phone_number = input("==>")
                    list_of_found = []
                    for i in range(len(list_of_dict_notes)):
                        if searching_phone_number == list_of_dict_notes[i]["Имя"]:
                            list_of_found.append(list_of_dict_notes[i])
                    if len(list_of_found) > 0:
                        self.print_formatted("НАЙДЕННЫЕ ЗАПИСИ: ")
                        for i in list_of_found:
                            print(i)
                    else:
                        print("ПО ДАННОМУ ЗАПРОСУ НИЧЕГО НЕ НАЙДЕНО.")

                    break
                elif num_of_searching == 2:
                    self.print_formatted("ПОИСК ПО НОМЕРУ ТЕЛЕФОНА")
                    searching_phone_number = input("==>")
                    list_of_found = []
                    for i in range(len(list_of_dict_notes)):
                        if searching_phone_number == \
                                list_of_dict_notes[i][
                                    "Номер_телефона"]:
                            list_of_found.append(
                                list_of_dict_notes[i])
                    if len(list_of_found) > 0:
                        print("НАЙДЕННЫЕ ЗАПИСИ: ")
                        for i in list_of_found:
                            print(i)
                    else:
                        print(
                            "ПО ДАННОМУ ЗАПРОСУ НИЧЕГО НЕ НАЙДЕНО.")
                    break
                else:
                    print("!ОШИБКА!\nЗдесь такой цифры нет!\nДоступные функциональные номера: 1 и 2")
                    continue
            except ValueError:
                print("!ОШИБКА!\nТо, что вы ввели не является числом!\nДоступные функциональные номера: 1 и 2 ")
                continue
        self.start()

    def sort(self):
        self.print_formatted("СОРТИРОВКА ЗАПИСЕЙ")

        file = open("notes.txt", 'r+', encoding="utf-8")
        list_of_notes = file.readlines()
        file.close()
        list_of_dict_notes = self.__list_of_str_to_list_of_dict(list_of_notes)

        print("1. Сортировка По Имени\n"
              "2. Сортировка По Фамилии")
        file = open("notes.txt", 'r', encoding='utf-8')
        file_notes = file.read()
        file.close()
        if file_notes == '':
            print("ФАЙЛ ПУСТОЙ. СОРТИРОВАТЬ НЕЧЕГО.")
        else:
            while True:
                try:
                    sort_by = int(input("==>"))
                    if sort_by == 1:
                        sorted_list_of_dict = sorted(list_of_dict_notes, key=lambda l: l['Имя'])
                        file = open('notes.txt', 'w', encoding='utf-8')
                        for i in sorted_list_of_dict:
                            file.write(f'{str(i)}\n')
                        file.close()
                        print("ФАЙЛ УСПЕШНО ОТСОРТИРОВАН!")
                        break
                    elif sort_by == 2:
                        sorted_list_of_dict = sorted(list_of_dict_notes, key=lambda l: l['Фамилия'])
                        file = open('notes.txt', 'w', encoding='utf-8')
                        for i in sorted_list_of_dict:
                            file.write(f'{str(i)}\n')
                        file.close()
                        print("ФАЙЛ УСПЕШНО ОТСОРТИРОВАН!")
                        break
                    else:
                        print("!ОШИБКА!\nЗдесь такой цифры нет!\nДоступные функциональные номера: 1 и 2")
                        continue
                except ValueError:
                    print("!ОШИБКА!\nТо, что вы ввели не является числом!\nДоступные функциональные номера: 1 и 2 ")
                    continue
        self.start()


if __name__ == '__main__':
    # Start
    n1 = Notebook({})
    n1.start()
