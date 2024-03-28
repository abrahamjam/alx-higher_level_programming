#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

"""
Python script that takes in a URL and an email, sends a POST request to the passed 
URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
"""

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Data should be bytes
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
