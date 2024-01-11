#!/usr/bin/python3
'''
This script uses the GitHub API to display the user's ID by
authenticating with a personal access token.
'''

import sys
import requests

if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        data_json = response.json()
        print(data_json["id"])
    except Exception:
        print("None")
