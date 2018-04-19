#!/usr/bin/env python3

import argparse
import os
import requests
import re
import sys
import socket
import time
import threading
import socket
import traceback
import cookielib

try: # For Python 3.0 and later
    import urllib.request
except ImportError:
    import urllib2

from time import sleep
from multiprocessing import Process, Queue

URL_REGEX='(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'

class startThread(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self)
        self.target = target

    def stop(self):
        exit

    def run(self):
        searchURLs(self.target)

# Common Utils
def green(s):
    return '\033[1;32m' + s + '\033[0m'

def red(s):
    return '\033[1;31m' + s + '\033[0m'

def blue(s):
    return '\033[1;34m' + s + '\033[0m'

def gray(s):
    return '\033[1;31m' + s + '\033[0m'

def print_good(s):
    print(green('[+]') + ' ' + s)

def print_fail(s):
    print(red('[-]') + ' ' + s)

def print_info(s):
    print(blue('[+]') + ' ' + s)

def readuntil(s, stop):
    res = ''
    while not res.endswith(stop):
        c = s.recv(1)
        if c == '':
            raise Exception("EOF")
        res += c
    return res

def readline(s):
    return readuntil(s, "\n")

# submits the data / flags to our own server
def searchURLs(target):
    try:
        cj = cookielib.CookieJar()

        http_url = "https://{}/".format(target)

        res = requests.get(http_url, cookies=cj)

        # Retrieve sources
        sources = res.text

        # Check for URLs in Sources
        urls = re.findall(URL_REGEX, sources)

        if not urls:
            print_fail("No URL found in "+target+" HTML Sources !")
            return

        print("============================================================================================================================================================")
        print_info("Found %d URLs from %s" % (len(urls), target))
        print("============================================================================================================================================================")

        for url in urls :
            print_good(url[0]+"://"+url[1]+url[2])

        print("============================================================================================================================================================\n")
    
    except Exception as e:
        print_fail("Exception: " + str(e))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

if __name__ == '__main__':
    
    # Get Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--urls', dest='urls', nargs='+', help='<Required> Set URLs to check', required=True)
    args = parser.parse_args()

    urls_to_check = []

    for url in args.urls:
        urls_to_check.append(startThread(url))

    for url in urls_to_check:
        url.start()