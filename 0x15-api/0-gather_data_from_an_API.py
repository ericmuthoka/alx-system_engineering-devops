#!/usr/bin/python3
"""Fetch and display an employee's TODO list progress from a REST API."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} <employee_id>\n".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        if not user_data:
            print("No employee found with ID: {}".format(employee_id))
            sys.exit(1)

        employee_name = user_data.get("name")
        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)
        num_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, num_completed_tasks, total_tasks))

        for task in completed_tasks:
            print("\t{}".format(task["title"]))

    except requests.exceptions.RequestException as e:
        print("Error: Unable to connect to the API.")
        sys.exit(1)
