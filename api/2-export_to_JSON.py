#!/usr/bin/python3
"""Module that gathers data from an API for a given employee ID.

Exports the employee's TODO list data to a JSON file, using the
JSONPlaceholder REST API.
"""
import json
import sys
import requests


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(base_url)
    params = {"userId": employee_id}

    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(todos_url, params=params)
    todos_data = todos_response.json()

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_dict = {str(employee_id): tasks_list}

    file_name = "{}.json".format(employee_id)
    with open(file_name, "w") as json_file:
        json.dump(json_dict, json_file)
