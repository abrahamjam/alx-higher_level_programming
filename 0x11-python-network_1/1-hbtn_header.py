#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Retrieve headers as a dictionary
        headers = response.getheaders()
        # Convert headers dictionary to a case-insensitive dictionary for easy lookup
        headers_dict = dict((k.lower(), v) for k, v in headers)
        # Print the value of 'x-request-id' header
        print(headers_dict.get('x-request-id'))
