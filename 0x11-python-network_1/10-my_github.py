#!/usr/bin/python3
"""
   script that takes your GitHub credentials
   (username and password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f'Bearer {password}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        user_id = data.get('id')
        print(user_id)
    else:
        print("None")
