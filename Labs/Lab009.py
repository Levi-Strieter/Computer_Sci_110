
myList = []
for i in range(0,10):
    myList.append(2*i)
print(myList)

myList = []
for i in range(0,10):
    myList.append(0)
print(myList)

import random

myList = []
for i in range(0,10):
    myList.append(random.randint(1,100))
print(myList)

myList = [1, 4, 16, 32, 64, 128, 256, 512, "Fred"]
for x in myList:
    print(x, end=" ")
print()
myList = [-1, -2, -3, 1, 2, 3, -42]
count = 0
for x in myList:
    if x < 0:
        count += 1
print(count, "are negative in given list")

myList = []
for x in range(0,10):
    userValue = float(input("Enter a decimal number: "))
    myList.append(userValue)
myList.reverse()
for x in myList:
    print(x, end=" ")
print()

listA = [1, 2, 3, 4]
listB = [1, 2, 3, 4]
listC = [1, 1, 3, 4]
equal = True 

for x in range(0, len(listA)):
    if listA[x] != listC[x]:
        equal = False
print("Lists are same" if equal == True else "Lists are not equal")


listA = ["Charlie", "Mary", "Fred", "Annie"]
listB = []

for x in listA: listB.append(x)
print(listB)

myList = []
for x in range(0, 9):
    userValue = int(input("Enter a int: "))
    myList.append(userValue)

equation = myList[0] - myList[1] + myList[2] - myList[3] + myList[4] - myList[5] + myList[6] - myList[7] + myList[8] 
print(equation)

