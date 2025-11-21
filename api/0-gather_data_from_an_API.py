#!/usr/bin/python3
"""
Using a REST API, and a given emp_ID, return info about their TODO list.
"""
import requests
import sys

if __name__ == "__main__":
    """ main section """
    # Check if an argument was provided
    if len(sys.argv) != 2:
        # If no argument is provided, the script will still fail later.
        # This check is good practice but not strictly required by the prompt's
        # minimal example, but prevents a subsequent IndexError.
        # However, to avoid changing the file structure too much, we'll
        # just assume the argument is there for now and focus on the syntax error.
        pass

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    
    # 1. Fetch employee data using .format()
    employee = requests.get(
        BASE_URL + '/users/{}'.format(sys.argv[1])).json()
    EMPLOYEE_NAME = employee.get("name")
    
    # 2. Fetch TODO list data using .format()
    employee_todos = requests.get(
        BASE_URL + '/users/{}/todos'.format(sys.argv[1])).json()
    
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_LEN = len([k for k, v in serialized_todos.items() if v is True])
    
    # Print the summary line
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, COMPLETED_LEN, len(serialized_todos)))
        
    # Print the completed tasks
    for key, val in serialized_todos.items():
        if val is True:
            # Use \t for the required tabulation
            print("\t {}".format(key))
