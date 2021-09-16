'''
Set a Boolean variable "first" to true.
While another value has been read successfully
 If first is true
    Set the minimum to the value.
    Set first to false.
  Else if the value is less than the minimum
    Set the minimum to the value.
Print the minimum.

'''


print("Problem P4.6")
minimum = 0
first = True
x = 0 
while x < 100:
    if first is True:
        minimum = x 
        first = False
    elif x < minimum:
        minimum = x
print(minimum)

print("Problem p4.21")
while True:
    try:
        sideLength = int(input("Enter a number- "))
        break
    except ValueError:
        print("[!] Enter Int [!]")

sideLength = 5
cap = 0
for columns in range(0, sideLength):
    for rows in range(0, sideLength):
        print("    *", end="")
        if cap == 0 or cap == sideLength:
            print("*" * sideLength, end="")
        cap += 1
         
    print("")
            

