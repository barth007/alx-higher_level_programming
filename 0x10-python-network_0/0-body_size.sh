#!/bin/bash
# This scripts takes in a URL and sends a request to that URL and displays the size of the body of the
curl -I "$1" | grep -Po "content-length:\s*([0-9]+)"
