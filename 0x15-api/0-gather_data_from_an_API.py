#!/usr/bin/python3
"""  Python script that, for a given employee ID, returns list progress. """
import requests
import sys

if __name__ == "__main__":
    ids = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(ids)).json()
    todos = requests.get(url + "todos", params={"userId": ids}).json()

    completed = [t for t in todos if t.get("completed") is True]
    totalCompleted = len(completed)
    totalTasks = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), totalCompleted, totalTasks))
    for title in completed:
        print("\t {}".format(title.get('title')))
