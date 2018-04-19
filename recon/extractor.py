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
import json
from bs4 import BeautifulSoup
from bs4 import Comment

try: # For Python 3.0 and later
    import urllib.request
except ImportError:
    import urllib2

from time import sleep
from multiprocessing import Process, Queue

ABSOLUTE_URL_REGEX='(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
RELATIVE_URL_REGEX='((^(http[s]?:\/\/)?([w]{3}[.])?(([a-z0-9\.]+)+(com|php))(((\/[a-z0-9]+)*(\/[a-z0-9]+\/?))*([a-z0-9]+[.](html|php|gif|png|jpg))?)$)|((^([.]\/)?((([a-z0-9]+)\/?)+|(([a-z0-9]+)\/)+([a-z0-9]+[.](html|php|gif|png|jpg))))$))'

class startThread(threading.Thread):
    def __init__(self, target, cookies):
        threading.Thread.__init__(self)
        self.target = target
        self.cookies = cookies

    def stop(self):
        exit

    def run(self):
        searchURLs(self.target, self.cookies)

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
def searchURLs(target, cookies):
    try:

        # Retrieve HTML sources from URL
        http_url = "https://{}/".format(target)
        res = requests.get(http_url, cookies=cookies)
        sources = res.text
        soup = BeautifulSoup(sources,"html.parser")

        # Check for URLs in Sources
        href_tags = soup.find_all('a', href=True)
        img_tags = soup.find_all('img', src=True)
        script_tags = soup.find_all('script', src=True)
        comments = soup.find_all(string=lambda text:isinstance(text,Comment))

        # <a> href Print
        if not href_tags:
            print_fail("No <a> tag with href attribute found in "+target+" HTML Sources !\n")
        else:
            print("============================================================================================================================================================")
            print_info("Found {} <a> tags with href attribute from {}".format(len(href_tags), target))
            print("============================================================================================================================================================")
            for a in href_tags:
                print_good (a['href'])
            print("\n")

        
        # <img> src Print
        if not img_tags:
            print_fail("No <img> tag with src attribute found in "+target+" HTML Sources !\n")
        else:
            print("============================================================================================================================================================")
            print_info("Found {} <img> tags with src attribute from {}".format(len(img_tags), target))
            print("============================================================================================================================================================")
            for img in img_tags:
                print_good (img['src'])
            print("\n")

        # <script> src Print
        if not script_tags:
            print_fail("No <script> tag with src attribute found in "+target+" HTML Sources !\n")
        else:
            print("============================================================================================================================================================")
            print_info("Found {} <script> tags with src attribute from {}".format(len(script_tags), target))
            print("============================================================================================================================================================")

            for script in script_tags:
                print_good (script['src'])
            print("\n")

        # Comments Print
        if not comments:
            print_fail("No comment tag found in "+target+" HTML Sources !\n")
        else:
            print("============================================================================================================================================================")
            print_info("Found {} comments from {}".format(len(comments), target))
            print("============================================================================================================================================================")

            for comment in comments:
                print_good ("<!-- {} -->".format(str(comment)))
            print("\n")

    except Exception as e:
        print_fail("Exception: " + str(e))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

if __name__ == '__main__':
    
    urls_to_check = []

    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--urls', dest='urls', nargs='+', help='<Required> Set URLs to check', required=True)
    parser.add_argument('-c', '--cookies', dest='cookies', type=json.loads)
    args = parser.parse_args()

    for url in args.urls:
        urls_to_check.append(startThread(url, args.cookies))

    for url in urls_to_check:
        url.start()