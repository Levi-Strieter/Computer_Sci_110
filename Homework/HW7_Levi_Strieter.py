
print("Problem 7.8")
file = open("/Users/lstrieter67280/Documents/School/Coding/Marshall/hello.py", "r")

content = {
    # line1: ""
    # line2: ""
}
lineNum = 0
for line in file:
    if line != "\n":
        lineNum += 1
    content["line{}".format(lineNum)] = line

for k,v in content.items():
    lineChars = []
    for character in v:
        lineChars.append(character)
    lineChars.reverse()
    lineChars.append("\n")
    for x in lineChars:
        print(x, end="")

print("Problem P7.9")
import sys 
inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w")

lineNum = 0
lineList = []
for line in inputFile:
    lineList.append(line)
lineList.reverse()
for line in lineList:
    outputFile.write(line)

print("Problem 3")
finished = False
while finished == False:
    try:
        file = input("Enter the filename: ")
        data = open(file, "r")
        finished = True
    except IOError as error:
        print(error)

totalPrecip = [line[24:27] for line in data ]
result = ""
print(','.join([str(x) for x in totalPrecip]))

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




