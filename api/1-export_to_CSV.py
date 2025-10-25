#!/usr/bin/python3
"""Export employee TODO list data to CSV file"""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/"
        "{}".format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?"
        "userId={}".format(employee_id)
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    employee_name = user_response.json().get("username")
    todos = todos_response.json()

    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])
