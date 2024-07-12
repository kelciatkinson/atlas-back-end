#!/usr/bin/python3
"""Documentation for the checker"""
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = 'users/{}'.format(employee_id)
    with urllib.request.urlopen(url + user_url) as response:
        data = response.read()
    employee_name = data.get('name')

    todo_url = 'todos?userId={}'.format(employee_id)
    with urllib.request.urlopen(url + todo_url) as response:
        data = response.read()
    number_of_done_tasks = data.get('completed')
    helpme = 0
