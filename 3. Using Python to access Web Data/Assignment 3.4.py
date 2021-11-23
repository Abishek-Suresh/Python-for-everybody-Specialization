#Assignment: Following Links in HTML Using BeautifulSoup
#In this assignment you will write a Python program that expands on https://www.py4e.com/code3/urllinks.py.
#The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
#scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times,
#and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL:')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))

for i in range(0,count):
    html= urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html ,'html.parser')
    tags = soup('a')
    link = tags[pos-1].get('href', None)
    print('Retrieving:',link)

result = tags[pos-1].contents[0]
print(result)
print(link)
