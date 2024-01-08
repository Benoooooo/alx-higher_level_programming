#!/usr/bin/python3
'''
This script sends a POST request to the provided URL with an email
as a parameter and displays the response body.
'''

import sys
import urllib.parse
import urllib.request as request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
