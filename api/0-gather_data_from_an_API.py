#!/usr/bin/python3
"""Documentation for the checker"""
import urllib.request
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    with urllib.request.urlopen(url + 'users/{}'.format(employee_id)) as response:
        data = response.read()
    employee_name = data.get('name')

    with urllib.request.urlopen(url + 'todos?userId={}'.format(employee_id)) as response:
        data = response.read()
    number_of_done_tasks = data.get('completed')