#!/usr/bin/python3
"""
Python script that, using a REST API, returns information about
an employee’s TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Get user info
    user = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = user.get("name")

    # Get TODO list
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Compute task statistics
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print output (EXACT checker format)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
