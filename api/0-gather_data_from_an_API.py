#!/usr/bin/python3
"""Gather employee TODO list progress from REST API"""

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

    employee_name = user_response.json().get("name")
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    num_done = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, num_done, total_tasks
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
