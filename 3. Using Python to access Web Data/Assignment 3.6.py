#Extracting Data from JSON
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse
#and extract the comment counts from the JSON data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location:')
uh = urllib.request.urlopen(url)
print('Retrieving',url)

data = uh.read().decode()
print('Retrieved',len(data),' characters')
js = json.loads(data)
count = 0
sum = 0
for u in js['comments']:
        count = u['count'] + 1
        sum = sum + u['count']
print('count:',count)
print('sum:',sum)
