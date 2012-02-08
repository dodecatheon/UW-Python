"""
scrape.py
Screen-scraping demo: open a page, find and print the first anchor element

First lab, week05:  scrape all the http: links off a page
"""

import urllib2
import sys
from BeautifulSoup import BeautifulSoup as soup
from pprint import pprint
import re

# Default site
url = 'http://jon-jacky.github.com/uw_python/winter_2012/' # course page

if len(sys.argv) > 1:
    url = sys.argv[1]

page = urllib2.urlopen(url).read()  # now page is one big string
html = soup(page)

# Find all http: links on the page
for tag in html.findAll('a',{'href': True}):
    my_map = tag.attrMap['href']
    if re.match(u'http:', my_map):
        print my_map
