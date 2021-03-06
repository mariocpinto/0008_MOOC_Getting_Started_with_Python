
# 3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use raw_input to read a string and float() to convert the string to a number. 
# Include error checking the user input.

hrs = input("Enter Hours: ")
rate_per_hr = input("Enter Rate per Hour: ")
try:
    h = float(hrs)
    r = float(rate_per_hr)
except:
    print('Error! Enter numeric values')
    quit()

if h <= 40:
	gross_pay = h*r
else:
	gross_pay = 40*r + (h - 40)*1.5*r

print(gross_pay)