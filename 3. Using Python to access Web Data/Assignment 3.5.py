#Extracting Data from XML
#In this assignment you will write a Python program somewhat similar to https://py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib,
#and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file
#and enter the sum.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location:')
u = urllib.request.urlopen(url)
data = u.read().decode()
xml_data = ET.fromstring(data)
count_tags = xml_data.findall("comments/comment")

sum = 0
for tags in count_tags:
    c=tags.find('count').text
    sum +=int(c)
print('Sum:',sum)
