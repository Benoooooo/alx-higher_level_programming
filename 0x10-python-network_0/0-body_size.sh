#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response


if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1

response=$(curl -sI "$url")

content_length=$(echo "$response" | awk '/Content-Length/ { print $2 }')

if [ -z "$content_length" ]; then
  echo "Failed to retrieve content length from the response headers"
  exit 1
fi

echo "$content_length"
