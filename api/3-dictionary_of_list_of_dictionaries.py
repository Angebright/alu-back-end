#!/usr/bin/python3
"""Export all employees' TODO list data to JSON file"""

import json
import requests


def fetch_users():
    """Fetch all users from API and return a dict of user_id -> username."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    return {user.get("id"): user.get("username") for user in users}


def fetch_todos():
    """Fetch all todos from API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    users = fetch_users()
    todos = fetch_todos()

    all_tasks = {}

    for task in todos:
        user_id = task.get("userId")
        username = users.get(user_id)
        task_dict = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }

        if user_id not in all_tasks:
            all_tasks[user_id] = []
        all_tasks[user_id].append(task_dict)

    # Convert keys to strings as per requirement
    all_tasks_str_keys = {str(k): v for k, v in all_tasks.items()}

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks_str_keys, jsonfile)
