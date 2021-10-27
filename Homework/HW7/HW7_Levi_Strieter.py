
print("Problem 7.8")
print("only compleated if hello.py is in same directory, reverse.py will accept the file to be reversed as an argv argument")
finished = False
while finished == False:
    try:
        file = open("hello.py", "r")
        data = [list(line.rstrip("\n")) for line in file]
        finished = True
    except IOError as error:
        print(error)
        finished = True
    finally:
        file.close()

finished = False 
while finished == False:
    try:
        file = open("hello.py", "w")
        for x in range(0, len(data)):
            data[x].reverse()
            data[x].append("\n")
            for char in data[x]:
                file.write(char)
        finished = True
    except IOError as error:
        print(error)
        finished = True 
    finally:
        file.close()

print("Problem P7.9")
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

print("Problem 3")
finished = False
while finished == False:
    try:
        fileToOpen = input("Enter the filename: ")
        file = open(fileToOpen, "r")
        data = [int(line[24:27]) for line in file ]
        finished = True
    except IOError as error:
        print(error)
    finally:
        file.close()


print("Total Precipitation:", sum(data))

print("Problem 4")
finished = False
while finished == False:
    try:
        file = input("Enter the filename: ")
        inputFile = open(file, "r")
        finished = True
    except IOError as error:
        print(error)
item = inputFile.readline()  #read the first item in the file
data = int(item.rstrip())
smallest, largest, sum = data, data, data
count = 1
for item in inputFile:       #process the rest of the file
  data = int(item)
  if data > largest:         #fill in the blank
    largest = data
  if data < smallest:         #fill in the blank
    smallest = data
  sum = sum + data
  count = count + 1
print("Smallest: ",smallest," Largest: ",largest," Ave: ",sum/count)




