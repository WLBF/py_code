# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
count = int(raw_input('Enter count:'))
pos = int(raw_input('Enter position:'))


# Retrieve all of the anchor tags

#print len(tags)
#print tags[2]
#for tag in tags:
#   print tag.get('href', None)

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos-1].get('href', None)
    print url
