#!/usr/bin/python3
import urllib.request

"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the package urllib
Not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
"""
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
