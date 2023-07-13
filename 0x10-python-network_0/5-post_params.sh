#!/bin/bash
# This scripts sends a POST request to passed URL, and displays the body of the response
curl -X POST -d '{"email":"test@gmail.com", "subject":"I will always be here for PLD"}' -H "Content-Type:application/json" "$1"
