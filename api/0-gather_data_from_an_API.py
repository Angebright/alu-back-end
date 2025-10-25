#!/usr/bin/python3
"""
Python script that, using a REST API, returns information
about an employee’s TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee data
    user = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = user.get("name")

    # Get employee todos
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Extract completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]

    # Display formatted output
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
