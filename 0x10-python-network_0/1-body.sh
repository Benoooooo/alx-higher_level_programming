#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1

response=$(curl -s -o /tmp/response.body -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
  cat /tmp/response.body
else
  echo "Failed to retrieve response body. Status code: $response"
fi

rm /tmp/response.body
