#Scraping HTML Data with BeautifulSoup
#In this assignment you will write a Python program to use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file


import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count=0
sum=0
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html ,'html.parser')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve all of the anchor tags
tags = soup('span')# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
for tag in tags:
    tag = tag.decode()
    y = re.findall('[0-9]+',tag)
    for a in y:
        count = count+1
        sum = sum + int(a)
print('Count',count)
print('Sum',sum)

# input is http://py4e-data.dr-chuck.net/comments_1336969.html and sum is 2826

# ANOTHER METHOD

#for tags in tag:
    #count+=1
    #sum+= int(tag.contents)
    #print('count',Count)
    #print('Sum',sum)
