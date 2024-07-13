#!/usr/bin/python3
"""Documentation for the checker"""
import json
import urllib.request


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/"

    # Get all users
    with urllib.request.urlopen(base_url + "users") as response:
        users_data = response.read()
        users_data = json.loads(users_data)

    todo_all_employees = {}

    for user in users_data:
        employee_id = user["id"]
        name = user["username"]

        url = "todos?userId={}".format(employee_id)
        with urllib.request.urlopen(base_url + url) as response:
            count = 0
            completed_tasks = []
            data = response.read()
            data = json.loads(data)
            for task in data:
                if task["completed"]:
                    completed_tasks.append(task["title"])
                    count += 1

        print(f"Employee {name} is done with tasks({count}/{len(data)}):")
        for task in completed_tasks:
            print("\t {}".format(task))

        todo_all_employees[employee_id] = []
        for task in data:
            todo_all_employees[employee_id].append({
                "username": name,
                "task": task["title"],
                "completed": task["completed"]})

    with open("todo_all_employees.json", "w") as file:
        json.dump(todo_all_employees, file)
