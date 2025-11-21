#!/usr/bin/python3
"""
Retrieves employee tasks from an API and exports data in JSON format.
"""
import json
import requests


def get_employee_tasks(employee_id):
    """
    Fetches tasks for a specific employee from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Corrected f-string 1
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_info = requests.get(user_url).json()
    
    employee_username = user_info["username"]

    # Corrected f-string 2
    todos_url = "{}/users/{}/todos".format(base_url, employee_id)
    todos_info = requests.get(todos_url).json()

    return [
        {
            "username": employee_username,
            "task": task["title"],
            "completed": task["completed"],
        }
        for task in todos_info
    ]


def get_all_employee_ids():
    """
    Fetches all employee IDs available in the API.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    users_info = requests.get(base_url).json()
    ids = [user["id"] for user in users_info]
    return ids


if __name__ == '__main__':
    all_employee_ids = get_all_employee_ids()
    
    # Note: Removed indent=4 to match typical assignment requirements 
    # for compact output, but left the method as it was in your original.
    with open('todo_all_employees.json', "w") as json_file:
        all_employees_tasks = {}
        for emp_id in all_employee_ids:
            # Keys must be strings for JSON format
            all_employees_tasks[str(emp_id)] = get_employee_tasks(emp_id)
        
        # Use json.dump for simpler writing, or stick to json.dumps + write
        json_file.write(json.dumps(all_employees_tasks))
