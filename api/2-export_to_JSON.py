#!/usr/bin/python3
"""Export employee TODO list data to JSON file"""

import json
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

    employee_username = user_response.json().get("username")
    todos = todos_response.json()

    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        })

    data = {str(employee_id): tasks_list}

    filename = "{}.json".format(employee_id)
    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile)
