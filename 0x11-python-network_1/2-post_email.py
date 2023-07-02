#!/usr/bin/python3

"""
This is a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
Args:
        email: Holds the email address
"""

import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        re = r.read().decode("utf-8")
        print(re)