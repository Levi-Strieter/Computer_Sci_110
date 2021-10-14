import random

print("Problem P6.1")

list = []
for x in range(0, 10):
    list.append(random.randint(0,10))
print("Original List: " , list)
print("Vals at Even Index: ", end="")
for x in range(0, len(list)):
    if x % 2 == 0:
        print(list[x], end=", ")
print()
print("Even Vals: ", end="")
for x in list:
    if x % 2 == 0:
        print(x, end=", ")

print()
list.reverse()
print("Reversed List: ", list)
print("First Value:", list[len(list)-1], "\nSecond Value:", (list[0]))


print("\nProblem P6.7")

def removeMin(list):
    previous = list[0]
    minVal = 0
    index = 0 
    for x in list:
        if x < previous:
            minVal = x
    for x in list:
        if x == minVal:
            list.pop(index)
        index += 1
    return list, minVal

poppedList, minVal = removeMin(list)
print("Original List is:", list)
print("New List is:", poppedList, "\nMin was:", min)

print("\nProblem P6.11")
def equals(a, b):
    matches = True
    index = 0
    for x in a:
        if x != b[index]:
            matches = False
        index += 1
    return matches

listA = [1, 2, 34, 5, 45]
listB = [1, 2, 34, 5, 45]
listC = [1, 34, 2, 45, 5]
print(equals(listA, listC)) # list B returns True

print("\nProblem P6.16")

randomList = []
for x in range(0, 20):
    randomList.append(random.randint(0, 99))

print("Sequence of Nums:", randomList)
randomList.sort()
print("sorted List: ", randomList)

print("\nProblem P6.23")

def minMaxScaler(list):
    maxVal = max(list)

    if maxVal > 40:
        return 40 / maxVal
    else:
        return False


userInput = 0
lineLenghts = []
finished = False
while finished == False:
    for x in range(0, 5):
        if userInput == -1:   
            finished = True
        else:
            userInput = int(input("Enter val for line: "))
            lineLenghts.append(userInput)
    if finished is False:
        scaler = minMaxScaler(lineLenghts)
        if scaler == False:
            for x in lineLenghts:
                print("*"*x)
        else:
            for x in lineLenghts:
                print("*"*round((x*scaler)))
    else:
        continue