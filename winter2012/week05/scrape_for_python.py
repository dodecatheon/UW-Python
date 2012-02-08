#!/usr/bin/env python
"""
scrape_for_python.py
Screen-scraping demo: open a page, find and print the first anchor element

First lab, week05:  scrape all the http: links off a page

Assignment ... adapt to scrape all python files off the site.
"""

import urllib2
import sys
from BeautifulSoup import BeautifulSoup as soup
from pprint import pprint
import re
import os
from urlparse import urljoin

# Default site
url = 'http://jon-jacky.github.com/uw_python/winter_2012/' # course page

if len(sys.argv) > 1:
    url = sys.argv[1]

page = urllib2.urlopen(url).read()  # now page is one big string
html = soup(page)

# Find all http: links on the page
for tag in html.findAll('a',{'href': True}):
    href = tag.attrMap['href']
    if href.endswith('.py'):
        directory, basename = os.path.split(href)
        print "href =", href
        print "directory =", directory
        if directory:
            if not os.path.isdir(directory):
                print "making directory", directory
                os.makedirs(directory, mode=0755)
        with open(href,'w') as f:
            f.write(urllib2.urlopen(urljoin(url,href)).read())
