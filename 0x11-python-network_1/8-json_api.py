#!/usr/bin/python3
import requests
import sys

"""
Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, 
display the id and name like this: [<id>] <name>
"""

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
        json_response = response.json()
        
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
