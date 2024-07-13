#!/usr/bin/python3
"""Documentation for the checker"""
import json
import sys
import urllib.request


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"

    url = "users/{}".format(employee_id)
    with urllib.request.urlopen(base_url + url) as response:
        data = response.read()
        data = json.loads(data)
        name = data["username"]

    url = "todos?userId={}".format(employee_id)
    with urllib.request.urlopen(base_url + url) as response:
        count = 0
        completed_tasks = []
        data = response.read()
        data = json.loads(data)
        for task in data:
            completed = task["completed"]
            if task["completed"]:
                completed_tasks.append(task["title"])
                count += 1

    print(f"Employee {name} is done with tasks({count}/{len(data)}):")
    for task in completed_tasks:
        print("\t {}".format(task))

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, "w") as file:
        for task in completed_tasks:
            file.write(f'"{employee_id}","{name}","{completed}","{task}"\n')
