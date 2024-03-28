#!/usr/bin/python3
import requests
import sys
"""a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display id
 using  the package requests and sys
"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    # Set up the authentication using Basic Authentication
    auth = (username, password)

    # Make a GET request to fetch user information
    response = requests.get('https://api.github.com/user', auth=auth)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and extract the user id
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    else:
        # Print None if the request was not successful
        print(None)
