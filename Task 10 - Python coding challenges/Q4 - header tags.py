#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


def getheadertags():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'lxml')
    for heading in soup.find_all(['h1', 'h2','h3', ]):
        print(heading.name + ' ' + heading.text.strip())
    

if __name__ == "__main__":
    getheadertags()
