#!/bin/bash
# Ascript that takes in a URL, sends a request to that URL, a, and displays the size of the body of the respon
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
