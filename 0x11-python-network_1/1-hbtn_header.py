#!/usr/bin/python3
import urllib.request
import sys
"""
Takes in url, sends request and displays value of X-Request-Id
"""


if __name__ == '__main__':
    requesting = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(requesting) as response:
        print(response.info().get('X-Request-Id'))
