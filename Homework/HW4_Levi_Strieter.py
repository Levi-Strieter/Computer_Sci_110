import math 
print("Problem P2.4")

finished = False
while finished == False:
    try:
        x = int(input("Enter a qty for val 1: "))
        y = int(input("Enter a qty for val 2: \n"))
        finished = True
    except ValueError:
        print("Enter a int")

vals = [x, y]
sum = x + y
difference = x - y
product = x * y
avg = (x + y) / 2
distance = abs(x) - abs(y)
maximum = max(vals)
minimum = min(vals)

print("sum: %2d" % sum)
print("difference: %2d" % difference)
print("product: %2d" % product)
print("avg: %2d" % avg)
print("distance: %2d" % distance)
print("maximum: %2d" % maximum)
print("minimum: %2d" % minimum)

print("\nProblem P3.17")

string = input("Enter some text: \n")
charsOnly = string.isalpha()
upperOnly = string.isupper()
lowerOnly = string.islower()
numOnly = string.isnumeric()
alphaNumOnly = string.isalnum()
upperFirstLetter = string[0].isupper()
endsPeriod = string[len(string)-1].endswith(".")

print("Characters Only: %2d" % charsOnly)
print("Upper Only: %2d" % upperOnly)
print("lower Only: %2d" % lowerOnly)
print("numbers Only: %2d" % numOnly)
print("Alpha Only: %2d" % alphaNumOnly)
print("Upper First Letter: %2d" % upperFirstLetter)
print("end in periood: %2d" % endsPeriod)


'''
Write an application to pre-sell a limited number of cinema tickets.
Each buyer can buy as many as 4 tickets. No more than 100 tickets can be sold. 
Implement a program called TicketSeller that prompts the user for the 
desired number of tickets and then displays the number of remaining tickets. 
Repeat until all tickets have been sold, and then display the total number of buyers.
'''
print("\nProblem P4.31")

MAX_TICKETS_SOLD = 100
MAX_TICKETS_BOUGHT = 4

def ticketSeller(ticketsBought, totalTickets):
    if ticketsBought > 20:
        print("[!] Can Only Buy a maximum of 4 tickets [!]")
        print("{} tickets remain".format( MAX_TICKETS_SOLD - totalTickets))
        return False
    else:
        if totalTickets > 100:
            print("[!] Can only buy {} tickets [!]".format(MAX_TICKETS_SOLD - totalTickets))
            return False
        else: 
            print("{} tickets remain".format(totalTickets - MAX_TICKETS_SOLD))
            return True 

finished = False
totalTickets = 0
while finished == False:
    try:
        tickets = int(input("How many tickets do you need? "))
        totalTickets += tickets
        buy = ticketSeller(tickets, totalTickets)
        if buy is not True:
            continue
        else:
            print("you bought {} tickets".format(tickets))
            finished = True

    except ValueError:
        print("[!] Enter only Integer [!]")
