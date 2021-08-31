import math

print("Problem R1.20")
'''print the amount of the bill, the tip, the total cost, and the  amount each person has to pay.
 It should also print how much of what each person pays is for the bill and for the tip.

 Input
 - Bill Cost 
 - number of friends 
 - tip amount 
Output 
 - total bill 
 - split cost 
 - bill
 - tip 

 billCost = 100
 numOfFriends = 5
 tipAmnt = .15

 totalBill = (100 * tipAmnt) + billCost
 splitBill = totalBill / numOfFriends 


'''
# Write a program that prints three items, such as the names of your three best friends or favorite movies, on three separate lines.
print("Problem P1.11")
print("Talladega Nights\n@glad_Dino7681\nAmerican Pie\n")

# Write a program that reads a number and displays the square, cube, and fourth power of the number. Use the ** operator only for the fourth power.
print("Problem P2.3")
import math 
num = int(input("Type any Number:"))
print("squared:", num**2, "\nCube:", num**3, "\nfourth:", num**4, "\n")

'''Write a program that asks the user for the lengths of the sides of a rectangle. Then print
•	The area and perimeter of the rectangle
•	The length of the diagonal'''
print("Problem P2.8")
length = int(input("type length of rectangle:"))
width = int(input("type width of rectangle:"))

area = length * width
perimeter = (length * 2) + (width * 2)

pythagoreanTheorem= lambda a, b : a**2 + b**2
diagnol = pythagoreanTheorem(length, width)
print("area:", area, "\nperimeter:", perimeter, "\ndiagnol length:", math.sqrt(diagnol), "\n")

'''Write a program that asks the user to input
•	The number of gallons of gas in the tank
•	The fuel efficiency in miles per gallon
•	The price of gas per gallon
Then print the cost per 100 miles and how far the car can go with the gas in the tank.'''
print("Problem P2.11")
#  Gallons, efficiency, price 
car_stats = [10, 1, 2]

prompt = {
    0: "Gallons of gas in tank: ",
    1: "Miles per Gallon: ",
    2: "Price of gas: "
}

y = 0
for x in car_stats:
    car_stats[y] = float(input("Enter the {}".format(prompt[y])))
    y = y + 1

print("cost per 100 miles:", car_stats[2] * 100, "\nHow far car can go with gas left in tank: ", car_stats[1]*car_stats[0], "\n")
