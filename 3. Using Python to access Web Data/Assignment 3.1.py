#Extracting Data With Regular Expressions
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.

import re
fname = open("regex_sum.txt")
sum = 0
for line in fname:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    for a in y:
        a = int(a)
        sum = sum+a
print(sum)
