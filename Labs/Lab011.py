from os import name
from typing import final


names = open("Labs/FileLab/Names.dat", "r")
nameList = []
for line in names:
    line = line.rstrip()
    nameList.append(line)
print(", ".join(nameList))

nameList.sort()
print(", ".join(nameList))
names.close()


file = open("Labs/FileLab/hopedale(1).dat", "r")
data = [line.rstrip().strip("        "[:len(line)]) for line in file ]
print(",".join(data))
file.close()

finished = False
while finished == False:
    try:
        fileToOpen= input("Enter the Filename: ")
        file = open(fileToOpen, "r")
        data = [int(line) for line in file ]
        finished = True 
    except IOError as error:
        print(error)
    finally:
        file.close()

print("smallest:", min(data), "\nlargest:", max(data), "\nAvg:", round(sum(data)/len(data), 5))


finished = False
while finished == False:
    try:
        fileToOpen= input("Enter the Filename: ")
        file = open(fileToOpen, "r")
        data = [line.rstrip().split(",") for line in file]
        finished = True 
    except IOError as error:
        print(error)
    finally:
        file.close()
# print(",".join(x) for x in data)
for x in data:
    print(", ".join(x))

finished = False
while finished == False:
    try:
        fileToOpen= input("Enter the Filename: ")
        file = open(fileToOpen, "r")
        data = [int(line[24:27]) for line in file]
        finished = True 
    except IOError as error:
        print(error)
    finally:
        file.close()


print("Total Precip:", sum(data))



finished = False
while finished == False:
    try:
        fileToOpen= input("Enter the Filename: ")
        file = open(fileToOpen, "r")
        fileToWrite = input("Enter the Output File: ")
        data = [line for line in reversed(file)]
        outputFile = open(fileToWrite, "w")
        outputFile.write(data)
        finished = True 
    except IOError as error:
        print(error)
    finally:
        file.close()

import sys
print("Creating", sys.argv[2], "and transferring", sys.argv[1], "data")
finished = False
while finished == False:
    try:
        inputFile = open(sys.argv[1], "r")
        outputFile = open(sys.argv[2], "w")

        lineList = [line for line in inputFile]
        lineList.reverse()
        for line in lineList:
            outputFile.write(line)
        finished = True
    except IOError as error:
        print(error)
    finally:
        outputFile.close()
        inputFile.close()



finished = False
while finished == False:
    try:
        numbers1File = open("Labs/FileLab/numbers1.txt", "r")
        numbers2File = open("Labs/FileLab/numbers2.txt", "r")
        num1Data = [line.rstrip() for line in numbers1File]
        num2Data = [line.rstrip() for line in numbers2File]
        overlap = [x for x in num2Data if x in num1Data]
        finished = True
    except IOError as error:
        print(error)
    finally:
        numbers1File.close()
        numbers2File.close()

print(", ".join([str(x) for x in overlap]))





