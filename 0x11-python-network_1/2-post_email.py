#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

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
