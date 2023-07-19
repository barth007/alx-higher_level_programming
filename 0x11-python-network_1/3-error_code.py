#!/usr/bin/python3
"""
    This script takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decod('uft-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
