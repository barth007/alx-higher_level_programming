#!/usr/bin/python3
"""
   This script takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.agrv[1]
        url = http://0.0.0.0:5000/search_user
        payload = {'q': letter}
        response = requests,post(url, data=payload)
        try:
            response.json()
            if data:
                print("{} {}".format(data['id'], data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a Valid JSON")
    else:
        print("No result")
