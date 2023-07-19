#!/usr/bin/python3
"""
   This script takes in a URL, sends a request to the URL and
   displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        response.raise_for_status
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(response.status_code))
