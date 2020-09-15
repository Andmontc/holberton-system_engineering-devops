#!/usr/bin/python3
"""  Python script that export all employees in JSON. """
import json
import requests

if __name__ == "__main__":
    allEmployees = {}
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    for u in user:
        userId = u.get('id')
        userName = u.get('username')
        alltodos = []
        todo = requests.get(url + "todos", params={"userId": userId}).json()

        for item in todo:
            i = {}
            i['username'] = userName
            i['task'] = item.get('title')
            i['completed'] = item.get('completed')
            alltodos.append(i)
        allEmployees[userId] = alltodos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(allEmployees, file)
