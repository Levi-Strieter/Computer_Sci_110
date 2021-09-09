import math

print("Problem R1.20\n")
'''  
Input-
1. length 
2. width
3. height
4. number of windows & doors 
5. door & windows, L W H
6. cost of paint

Output- 
1. surface area of house
2. total cost

totalArea = (2 * (width * height) + 2 * (length * height)) - doorAmnt * (doorLength * Width * Height) - windowAmnt(windowLength * windowWidth * windowHeight)
cost = totalArea * costPerSquareFoot
'''

print("Problem P1.11\n")
num = float(input("Enter int- "))
if num > 0.0:
    print("num is positive\n")
elif num < 0.0:
    print("num is negative\n")
else:
    print("num is 0\n")

'''
Write a program that reads an integer and prints how many digits 
the number has, by checking whether the number is ≥ 10, ≥ 100, 
and so on. (Assume that all integers are less than ten billion.) 
If the number is negative, first multiply it by –1
'''
print("Problem P2.3")
num = int(input("enter a number: "))
base = 10
counter = 1
if num < 0: num *= -1
while num >= base:
    base *= 10
    counter += 1
print(num, "has", counter, "digits in it\n")

'''
Write a unit conversion program that asks the users from which  
unit they want to convert (ft or mi) and to which unit they want to convert 
(cm, m, km). Reject incompatible conversions (such as gal → km). 
Ask for the value to be converted, then display the result:
Convert from? ft
Convert to? km
Value? 6250
6250 ft = 1.905 km
'''
print("Problem P2.8")
units = {
    1: "mi",
    2: "ft",
    3: "km",
    4: "m",
    5: "cm",
}

metricToMetric = {
    1: 1000, # Kilo
    2: .01,  # Centi
    3: .001  # Meter
}

standardMetric = {
    1 : 1.60934,                 # mi -> km
    2 : 1609.33999997549,        # mi -> m
    3 : 160933.99999754899181,   # mi -? cm
    4 : 0.0003048,               # ft -> km

    5 : 0.3048,                  # ft -> m
    6 : 30.48,                   # ft -> cm
}

for key, value in units.items():
    print("{}: {}".format(key, value))
while True:
    try:
        convertFrom = int(input("Which unit do you want to convert from: "))
        convertTo = int(input("Which unit do you want to convert to: "))
        valueToConvert = int(input("What value do you want to be converted from {} to {}: ".format(units.get(convertFrom), units.get(convertTo))))
        break
    except ValueError:
        print("Please choose an int from the list")

def metricToMetricConversion(x,y,val):
    if x == 3 and y == 4:  # Km -> m
        convertedVal = metricToMetric.get(1) * val
        return convertedVal
    if x == 3 and y == 5:
        convertedVal = metricToMetric.get(2) * val
        return convertedVal
    if x == 3 and y == 4:
        convertedVal = metricToMetric.get(3) * val
        return convertedVal



if convertFrom >= 3 and convertTo >= 3:
    finalVal = metricToMetricConversion(convertFrom, convertTo, valueToConvert)


print(finalVal)

    



'''
Write a program that reads in the name and salary of an employee. 
Here the salary will denote an hourly wage, such as $9.25. Then ask how many hours 
the employee worked in the past week. Be sure to accept fractional hours. 
Compute the pay. Any overtime work (over 40 hours per week) is paid at 150 percent 
of the regular wage. Print a paycheck for the employee.
'''
print("Problem P2.11")

while True:
    try:
        firstName = str(input("Enter First Name: "))
        lastName = str(input("Enter Last Name: "))
        wage = float(input("Enter your hourly wage: "))
        hoursWorked = float(input("How many hours did {} {} work: ".format(firstName, lastName)))
        break
    except ValueError:
        print("[!] please use only strings or ints [!]")

pay = lambda wage, hours: (wage * 1.5)*hours if hours > 40 else wage * hours 

totalPay = pay(wage, hoursWorked)

print("#"*20)
print(hoursWorked, "hours worked with a rate of", wage)
print("Total Pay:", totalPay)
print("#"*20)