#!/usr/bin/python3
'''
write a python script that fetches the url provided
'''

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_cod}")
