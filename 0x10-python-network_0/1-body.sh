#!/bin/bash
# This script sends a GET request to the URL, and displays the body of the response
url="$1";
curl -X GET -sL "$url"
