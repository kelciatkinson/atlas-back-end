#!/usr/bin/python3
"""Documentation for the checker"""
import urllib.request


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        username = data.get('name')

    with urllib.request.urlopen(url + 'todos') as response:
        data = response.read()
