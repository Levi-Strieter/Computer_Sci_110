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
# while x < 100:
#     if first is True:
#         minimum = x 
#         first = False
#     elif x < minimum:
#         minimum = x
# print(minimum)

print("Problem p4.21")
while True:
    try:
        Length = int(input("Enter a number- "))
        break
    except ValueError:
        print("[!] Enter Int [!]")


for rows in range(0, Length):
    if rows <= Length:
        if rows == 0 or rows == Length - 1:
            print("*" * Length, "*" * Length)
        else:
            print("*"*Length, "*", " "*(Length-1), "*")
    else:
        break


'''
Write a program that first asks the user to type today’s price
for one dollar in Japanese yen, then continually reads U.S. dollar 
values and converts each to yen until the user enters 0.
'''
print("Problem p4.28")

while True:
    try:
        yenVal = float(input("Today's price for one dollar in japanese yen: "))
        while True:
            usVal = float(input("Enter US dollar amount you want to convert to Yen: "))
            print("$US to Yen=", yenVal*usVal)
            if usVal == 0:
                break
        break
    except ValueError:
        print("[!] Enter Int [!]")


'''
You need to control the number of people who can be in
an oyster bar at the same time. Groups of people can always leave the bar, 
but a group cannot enter the bar if they would make the number of people in the 
bar exceed the maximum of 100 occupants. Write a program that reads the 
sizes of the groups that arrive or depart. Use negative numbers for departures. 
After each input, display the current number of occupants. As soon as the bar holds 
the maximum number of people, report that the bar is full and exit the program.
'''
print("Problem p4.32")

MAX_PEOPLE = 100
currentPeople = 0

def counter(currentPeople):
    if currentPeople > MAX_PEOPLE:
        return False
    else:
        return True

while True:
    entering = int(input("How many people are coming in: "))
    currentPeople += entering
    allow = counter(currentPeople)
    if allow == True:
        print("Your party can enter, {} people are in the oyster bar.".format(currentPeople))
    else:
        print("Your party cannot enter the bar, {} people would be in the bar and your party will exceed max cappacity.".format(currentPeople))
        break
    exiting = int(input("How many people are exiting: "))
    currentPeople -= exiting
    print(currentPeople, "are in the bar")
 





    
            

