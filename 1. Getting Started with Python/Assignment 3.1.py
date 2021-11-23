#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.


hrs = input('enter Hours:')
rate = input('enter rate:')
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, plese enter numeric input')
ot = r*1.5  #overtime calculation
if h <= 40:
    pay = r*h
    print(pay)
elif h>40:
    pay= (r*40)+(ot*(h-40))
    print(pay)
