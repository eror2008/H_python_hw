# Python_homework_7

"""
Нужно создать для каждого пользователя csv файл. Имя файла это username пользователя.
В файл добавить задачи пользователя со следующими столбцами: id, title, completed
"""

import requests  # pip3 install requests
import csv

url_users = 'https://jsonplaceholder.typicode.com/users'
url_todos = 'https://jsonplaceholder.typicode.com/todos'


def user_task():
    users_tasks = {}
    for t in requests.get(url_todos).json():
        task_user_id = t["userId"]
        if not (task_user_id in users_tasks):
            users_tasks[task_user_id] = []
        users_tasks[task_user_id].append(t)
    return users_tasks


if __name__ == '__main__':
    for user in requests.get(url_users).json():
        ls_for_csv = []
        for task in user_task().get(user['id']):
            ls_for_csv.append({"id": task["id"], "title": task["title"], "completed": task["completed"]})
        with open(user['username'] + '.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, ["id", "title", "completed"])
            dict_writer.writeheader()
            dict_writer.writerows(ls_for_csv)
