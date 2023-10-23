#!/usr/bin/python3
"""Access a REST API to retrieve employee's TODO list and export to CSV."""

import csv
import requests
import sys


if __name__ == '__main__':
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

        username = user_data.get("username")
        csv_filename = "{}.csv".format(employee_id)

        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

            for task in todos_data:
                csv_writer.writerow([employee_id, username, task["completed"], task["title"]])

        print("Data exported to {}".format(csv_filename))

    except requests.exceptions.RequestException as e:
        print("Error: Unable to connect to the API.")
        sys.exit(1)
