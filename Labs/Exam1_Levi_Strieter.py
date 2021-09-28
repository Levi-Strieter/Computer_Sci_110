
print("problem 1")
while True:
    try:
        phVal = float(input("Enter a PH value: "))
        if phVal < 0 or phVal > 14:
            print("The range of pH in water is 0 to 14. Goodbye!")
            break
        elif phVal > 0 and phVal <= 3:
            print("The liquid is very acidic - be very careful!")
        elif phVal > 3 and phVal <= 7:
            print("The liquid is acidic")
        elif phVal > 7:
            print("The liquid is not acidic")
        else:
            print("The range of pH in water is 0 to 14")

    except ValueError:
        print("[!] Did not enter a integer [!]")


print("Problem 2")

findCubeRoot = lambda x : x**(1/3)

while True:
    userInput = input("Enter a number or Q to quit: ")
    if str(userInput) == "q" or str(userInput) == "Q":
        print("Done")
        break
    elif int(userInput) > 0:
        cubeRoot = findCubeRoot(float(userInput))
        print(round(cubeRoot, 2))
    else:
        print("Number needs to be positive")
    
print("Problem 3")
gapA = int(input("Please enter the first number, A: "))
gapB = int(input("Please enter the first number, B: "))
gapG = int(input("Please enter the gap between two consecutive numbers, g: "))

forwards = []
reverse = []

if gapA < gapB:
    if gapB < 0:
        gapG *= -1
    else:
        gapG = gapG
else:
    if gapB < 0:
        gapG = gapG
    else:
        gapG *= -1

for x in range(gapA, gapB, gapG):
    forwards.append(x)

if gapA < gapB:
    if gapB < 0:
        gapG *= -1
    else:
        gapG = gapG

else:
    if gapB < 0:
        gapG *= -1
    else:
        gapG = gapG

for y in range(gapB, gapA, gapG):
    reverse.append(y)

print("Forwards Direction: ", end="")
for z in forwards:
    print(z, ",", end="")
print("\n")
print("Reverse Direction: ", end="")
for a in reverse:
    print(a, ",", end="")
    