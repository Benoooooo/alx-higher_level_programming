#!/usr/bin/python3
'''
This script sends a POST request to the provided URL with an email
as a parameter and displays the response body using the requests package.
'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
