#!/usr/bin/python3
'''
This script sends a POST request to a search API with a letter as
a parameter and displays the response body, parsing it as JSON.
'''

import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    text = response.text

    try:
        json_data = response.json()
        if 'id' not in json_data:
            print('No result')
        else:
            print(f"[{json_data['id']}] {json_data['name']}")
    except ValueError:
        print("Not a valid JSON")
