# Algo for Painter 

# data is psedo code data, comment out for loop to test program
MAX_PRICE = 6
LOWEST_PRICE = 2
maxCost = 0
lowestCost = 0
#              length, width, height
houseMeasurements = [30, 50, 10]
#                length, height
windowMeasurement = [3, 5]
doorMeasurement = [4, 7]

numOfDoors = 5
numOfWindows = 20

totalWindowArea = numOfWindows * (windowMeasurement[0] * windowMeasurement[1])
totalDoorArea = numOfDoors * (doorMeasurement[0] * doorMeasurement[1])
totalHouseArea = ((houseMeasurements[0] * houseMeasurements[2]) * 2) + ((houseMeasurements[1] * houseMeasurements[2]) * 2)

totalPaintedArea = totalHouseArea - totalDoorArea - totalWindowArea

# for loop to get userinput and put it into list 
x = 0
for measurement in houseMeasurements:
    houseMeasurements[x] = int(input("What is the Dimensions of the house L x W x H: "))
    x = x + 1
x = 0
for measurement in windowMeasurement:
    windowMeasurement[x] = int(input("What is the Dimensions of the Doors L x W: "))
    x = x + 1
x = 0
for measurement in doorMeasurement:
    doorMeasurement[x] = int(input("What is the Dimensions of the Windows L x W: "))
    x = x + 1

print(houseMeasurements)

# finds total costs 
maxCost = totalPaintedArea * MAX_PRICE
lowestCost = totalPaintedArea * LOWEST_PRICE

print("The Max cost is: ${}\nThe Lowest cost is: ${}".format(maxCost, lowestCost))

