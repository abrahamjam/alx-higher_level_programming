#!/usr/bin/python3
import urllib.request
import sys

"""
Python script that takes in a URL, sends a request to the URL and 
displays the value of the X-Request-Id variable found in the header of the response.
using the packages urllib and sys
not allow to import packages other than urllib and sys
The value of this variable is different for each request
No need to check arguments passed to the script (number or
"""

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Retrieve headers as a dictionary
        headers = response.getheaders()
        # Convert headers dictionary to a case-insensitive dictionary for easy lookup
        headers_dict = dict((k.lower(), v) for k, v in headers)
        # Print the value of 'x-request-id' header
        print(headers_dict.get('x-request-id'))
