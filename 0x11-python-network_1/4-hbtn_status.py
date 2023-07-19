#!/usr/bin/python3
import requests


def fetch_resource(url):
    """
      This script fetches https://alx-intranet.hbtn.io/status
    """
    response = requests.get(url)
    response.raise_for_status()
    print("Body response:")
    print("\t -type: {}".format(type(response.text)))
    print("\t -content: {}".format(response.text))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_resource(url)
