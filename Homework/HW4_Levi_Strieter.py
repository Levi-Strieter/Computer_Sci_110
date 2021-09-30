import math 
print("Problem P2.4")

finished = False
while finished == False:
    try:
        x = int(input("Enter a qty for val 1: "))
        y = int(input("Enter a qty for val 2: "))
        finished = True
    except ValueError:
        print("Enter a int")

vals = [x, y]
sum = x + y
difference = x - y
product = x * y
avg = (x + y) / 2
distance = abs(abs(x) - abs(y))
maximum = max(vals)
minimum = min(vals)

print("\nsum: %2d" % sum)
print("difference: %2d" % difference)
print("product: %2d" % product)
print("avg: %2d" % avg)
print("distance: %2d" % distance)
print("maximum: %2d" % maximum)
print("minimum: %2d" % minimum)

print("\nProblem P3.17")

string = input("Enter some text: ")
charsOnly = string.isalpha()
upperOnly = string.isupper()
lowerOnly = string.islower()
numOnly = string.isnumeric()
alphaNumOnly = string.isalnum()
upperFirstLetter = string[0].isupper()
endsPeriod = string[len(string)-1].endswith(".")

print("\nCharacters Only: %2s" % charsOnly)
print("Upper Only: %2s" % upperOnly)
print("lower Only: %2s" % lowerOnly)
print("numbers Only: %2s" % numOnly)
print("Alpha Only: %2s" % alphaNumOnly)
print("Upper First Letter: %2s" % upperFirstLetter)
print("end in periood: %2s" % endsPeriod)


'''
Write an application to pre-sell a limited number of cinema tickets.
Each buyer can buy as many as 4 tickets. No more than 100 tickets can be sold. 
Implement a program called TicketSeller that prompts the user for the 
desired number of tickets and then displays the number of remaining tickets. 
Repeat until all tickets have been sold, and then display the total number of buyers.
'''
print("\nProblem P4.31")


MAX_TICKETS = 100
currentTickets = 0
finished = False
def counter(currentTickets):
    if currentTickets >= MAX_TICKETS:
        if MAX_TICKETS - currentTickets == 0:
            return "finished"
        else:
            return False
    else:
        return True

while finished == False:
    tickets = int(input("How many tickets do you want: "))
    if tickets > 20 or tickets <= 0:
        print("you can not buy over 4 tickets or negative tickets")
    else:
        currentTickets += tickets
        allow = counter(currentTickets)
        if allow == "finished":
            print("All tickets are sold, thanks!!")
            finished = True
        elif allow == True:
            print("Your party bought {} tickets.".format(tickets))
        elif allow == False:
            currentTickets -= tickets
            print("Your party cannot buy {}".format(tickets))

            
        print(MAX_TICKETS - currentTickets, "remain")
 
