#!/usr/bin/python3
"""  Python script that export to a JSON. """
import json
import requests
import sys

if __name__ == "__main__":
    ids = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(ids)).json()
    todo = requests.get(url + "todos", params={"userId": ids}).json()
    userName = user.get('username')
    employee = {}
    employee[ids] = []
    for item in todo:
        i = {}
        i['username'] = userName
        i['task'] = item.get('title')
        i['completed'] = item.get('completed')
        employee[ids].append(i)
    with open('{}.json'.format(ids), 'w') as file:
        json.dump(employee, file)
