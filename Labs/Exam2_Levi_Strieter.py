from random import randint

# PROBLEM 1
def DrNarmanDice(rolls, sides):
    rollData = [randint(1, sides) for x in range(rolls)]
    avgRolls = sum(rollData) / len(rollData)
    return avgRolls

finished = False 
while finished == False:
    try:
        rolls = int(input("Please enter the dice rolls variable: "))
        sides = int(input("Please enter the number of dice sides: "))
        finished = True
    except ValueError as error:
        print(error)
playerRolls = [DrNarmanDice(rolls, sides) for x in range(0, 2)]
print("Roll 1:", round(playerRolls[0]), "\nRoll 2:", round(playerRolls[1]), "\nTotal:", sum(playerRolls))
if sum(playerRolls) > sides+1: 
    print("You Lose ({} > {})".format(sum(playerRolls), sides+1))
else:
    print("You Win ({} < {})".format(sum(playerRolls), sides+1))



# PROBLEM 2
choices = {
    1 : "Enter new order",
    2 : "Display all orders",
    3 : "Change delivery status",
    4 : "Print Completed Order",
    5 : "Exit"
}
def printOptions():
    for k,v in choices.items():
        print(k, "-", v)

finished = False 
allOrders = []
while finished == False:
    printOptions()
    try:
        userChoice = int(input())
        if userChoice == 1:
            customerName = input("Enter customer name: ")
            pizzaSize = int(input("Enter pizza size: "))
            pizzaQuantity = int(input("Enter pizza quantity: "))
            thisOrder = [customerName, pizzaSize, pizzaQuantity, False]
            allOrders.append(thisOrder)
        elif userChoice == 2:
            for x in allOrders:
                print("Customer:", x[0], "Size:", x[1], "Qty:", x[2], "Delivered:", x[3])
        elif userChoice == 3:
            orderUpdate = int(input("Enter order number to update: "))
            # added the -1 to get teh correct index value, if changed order 1 thats actaully index 0
            allOrders[orderUpdate-1][3] = True
        elif userChoice == 4:
            for x in allOrders:
                if x[3] == True:
                    print("Customer:", x[0], "Size:", x[1], "Qty:", x[2], "Delivered:", x[3])
        elif userChoice == 5:
            print("Goodbye!")
            finished = True
    except ValueError as error:
        print(error)