#!/usr/bin/python3
"""
Using a REST API and an EMP_ID, save info about their TODO list in a json file
"""
import json
import requests
import sys

if __name__ == "__main__":
    """ Main section """
    
    if len(sys.argv) != 2:
        print("Usage: python3 {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
        
    employee_id = sys.argv[1]
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    
    # Fetch employee data (corrected for PEP8 line length)
    user_url = '{}/users/{}'.format(BASE_URL, employee_id)
    employee = requests.get(user_url).json()
    employee_name = employee.get("username")
    
    # Fetch TODO data (corrected for PEP8 line length)
    todos_url = '{}/users/{}/todos'.format(BASE_URL, employee_id)
    emp_todos = requests.get(todos_url).json()
    serialized_todos = []

    # Format the tasks as required
    for todo in emp_todos:
        serialized_todos.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee_name
        })

    # Create final dictionary structure (User ID as string key)
    output_data = {employee_id: serialized_todos}
    
    # Write to JSON file
    file_name = "{}.json".format(employee_id)
    with open(file_name, 'w') as file:
        json.dump(output_data, file)
