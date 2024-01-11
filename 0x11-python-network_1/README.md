# 0x11. Python - Network #1

This project contains a collection of Python scripts that demonstrate various functionalities related to sending HTTP requests and handling responses. Each script focuses on a specific task and utilizes different packages such as `urllib` and `requests`.

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Scripts](#scripts)
    1. [Script 1: Fetching Status](#script-1-fetching-status)
    2. [Script 2: Response Header Value](#script-2-response-header-value)
    3. [Script 3: POST an Email](#script-3-post-an-email)
    4. [Script 4: Error Code Handling](#script-4-error-code-handling)
    5. [Script 5: Fetching Status (Using `requests`)](#script-5-fetching-status-using-requests)
    6. [Script 6: Response Header Value (Using `requests`)](#script-6-response-header-value-using-requests)
    7. [Script 7: POST an Email (Using `requests`)](#script-7-post-an-email-using-requests)
    8. [Script 8: Error Code Handling (Using `requests`)](#script-8-error-code-handling-using-requests)
    9. [Script 9: Search API](#script-9-search-api)
    10. [Script 10: My GitHub!](#script-10-my-github)

## Description

This project consists of various Python scripts that demonstrate different techniques for sending HTTP requests and handling the responses. The scripts are designed to showcase functionalities such as fetching status, retrieving response headers, sending POST requests, handling error codes, interacting with search APIs, and accessing GitHub information using Basic Authentication.

## Installation

To run these scripts, please ensure you have Python installed on your system. These scripts also require specific packages such as `urllib` and `requests`. You can install these dependencies using the following commands:

```bash
pip install urllib
pip install requests
```

## Usage

To use the scripts, follow the instructions provided with each script. You can execute the scripts by running the corresponding Python files in your preferred Python environment.

## Scripts

### Script 1: Fetching Status

- Description: This script fetches the status from the provided URL using the `urllib` package.
- File: `0-hbtn_status.py`
- Instructions:
  - Write a Python script that fetches the status from the URL `https://alx-intranet.hbtn.io/status`.
  - Use the `urllib` package for making the request.
  - Display the body of the response with tabulation before each line.
  - Make sure to use a `with` statement.

### Script 2: Response Header Value

- Description: This script retrieves the value of the `X-Request-Id` variable from the header of the response.
- File: `1-hbtn_header.py`
- Instructions:
  - Write a Python script that takes a URL as input and sends a request to the URL.
  - Use the `urllib` and `sys` packages.
  - Display the value of the `X-Request-Id` variable found in the header of the response.
  - Note that the value of `X-Request-Id` may be different for each request.
  - Ensure you use a `with` statement.

### Script 3: POST an Email

- Description: This script sends a POST request to the provided URL with an email as a parameter and displays the response body.
- File: `2-post_email.py`
- Instructions:
  - Write a Python script that takes a URL and an email as input.
  - Send a POST request to the provided URL with the email as a parameter.
  - Use the `urllib` and `sys` packages.
  - Display the body of the response, decoded in UTF-8.
  - Ensure you use the `with` statement.

### Script 4: Error Code Handling

- Description: This script sends a request to the provided URL and displays the response body. It also handles `urllib.error.HTTPError` exceptions and prints the error code.
- File: `3-error_code.py`
- Instructions:
  - Write a Python script that takes a URL as input.
  - Send a request to the URL and display the body of the response, decoded in UTF-8.
  - Handle `urllib.error.HTTPError` exceptions and print "Error code:" followed by the HTTP status code.
  - Use the `urllib` and `sys` packages.
  - Ensure you use the `with` statement.
  - Test the script using the web server running on port 5000.

### Script 5: Fetching Status (Using `requests`)

- Description: This script fetches the status from the provided URL usingthe `requests` package.
- File: `4-hbtn_status.py`
- Instructions:
  - Write a Python script that fetches the status from the URL `https://alx-intranet.hbtn.io/status`.
  - Use the `requests` package for making the request.
  - Display the body of the response with tabulation before each line.

### Script 6: Response Header Value (Using `requests`)

- Description: This script retrieves the value of the `X-Request-Id` variable from the header of the response using the `requests` package.
- File: `5-hbtn_header.py`
- Instructions:
  - Write a Python script that takes a URL as input and sends a request to the URL.
  - Use the `requests` and `sys` packages.
  - Display the value of the `X-Request-Id` variable found in the header of the response.
  - Note that the value of `X-Request-Id` may be different for each request.

### Script 7: POST an Email (Using `requests`)

- Description: This script sends a POST request to the provided URL with an email as a parameter and displays the response body using the `requests` package.
- File: `6-post_email.py`
- Instructions:
  - Write a Python script that takes a URL and an email as input.
  - Send a POST request to the provided URL with the email as a parameter.
  - Use the `requests` and `sys` packages.
  - Display the body of the response.

### Script 8: Error Code Handling (Using `requests`)

- Description: This script sends a request to the provided URL and displays the response body. It also handles HTTP status codes greater than or equal to 400 using the `requests` package.
- File: `7-error_code.py`
- Instructions:
  - Write a Python script that takes a URL as input.
  - Send a request to the URL and display the body of the response.
  - If the HTTP status code is greater than or equal to 400, print "Error code:" followed by the value of the HTTP status code.
  - Use the `requests` and `sys` packages.
  - Test the script using the web server running on port 5000.

### Script 9: Search API

- Description: This script sends a POST request to a search API with a letter as a parameter and displays the response body, parsing it as JSON.
- File: `8-json_api.py`
- Instructions:
  - Write a Python script that takes a letter as input.
  - Send a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
  - Display the response body in the following format: "[\<id>] \<name>" if the JSON is properly formatted and not empty.
  - If the JSON is invalid, display "Not a valid JSON".
  - If the JSON is empty, display "No result".
  - Use the `requests` and `sys` packages.
  - Test the script using the web server running on port 5000. Note that the JSON generated by the server is random.

### Script 10: My GitHub!

- Description: This script uses the GitHub API to display the user's ID by authenticating with a personal access token.
- File: 10-my_github.py`
- Instructions:
  - Write a Python script that takes the user's GitHub username and personal access token as input.
  - Use the GitHub API to display the user's ID.
  - Authenticate using Basic Authentication with the provided personal access token as the password.
  - Use the `requests` and `sys` packages.

Please refer to the individual script files for detailed instructions on how to run each script.

AUTHOR @yandah1
Note: Make sure to test the scripts using the specified sandbox environment with the web server running on port 5000.
