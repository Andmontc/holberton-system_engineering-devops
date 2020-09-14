#!/usr/bin/python3
"""  Python script that export to a csv file. """
import csv
import requests
import sys

if __name__ == "__main__":
    ids = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(ids)).json()
    todo = requests.get(url + "todos", params={"userId": ids}).json()
    userName = user.get('username')
    with open("{}.csv".format(ids), 'w', newline='') as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            w.writerow([ids, userName, t.get("completed"), t.get("title")])
