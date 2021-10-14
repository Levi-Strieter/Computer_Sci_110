
# PROBLEM P5.1
from typing import final


def smallest(x,y,z):
    args=[]
    args.append(x,y,z)
    return min(args)

def avg(x,y,z):
    return (x + y + z) / 3

# PROBLEM P5.6
def countVowels(string):
    vowels = []
    string = string.lower()
    for x in string:
        if x == "a":
            vowels.append(x)
        elif x == "e":
            vowels.append(x)
        elif x == "i":
            vowels.append(x)
        elif x == "o":
            vowels.append(x)
        elif x == "u":
            vowels.append(x)

    return vowels


# PROBLEM P5.20
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True 
    elif year % 400 != 0:
        return False
    else:
        return True


# PROBLEM P5.28
def finnacialAssistance(income, children):
    if income >= 30000 and income <= 40000 and children >= 3:
        return 1000
    elif income >= 20000 and income <= 30000 and children >= 2:
        return 1500
    elif income <= 20000:
        return 2000

# PROBLEM P5.30
def strongPassword(string):
    stringLen = len(string) >= 8
    upper = any(x.isupper() for x in string)
    lower = any(x.islower() for x in string)
    digit = any(x.isdigit() for x in string)
    if upper and lower and digit and stringLen:
        return True
                

# PROBLEM P5.6
print("PROBLEM P5.6")
vowels = countVowels("EUOUAE")
print(len(vowels)) #should return 6

# PROBLEM P5.20
print("PROBLEM P5.20")
year = 0
while year != -1:
    year = int(input("Enter a year (yyyy): "))
    Tf = isLeapYear(year)
    if Tf == True:
        print("{} is Leap Year!".format(year))
    else:
        print("{} is not a Leap Year!".format(year))

# PROBLEM P5.28
print("PROBLEM P5.28")
income = 0
while income != -1 or children != -1:
    income = int(input("Enter your income: "))
    children = int(input("Enter how many childs you have: "))
    if income == -1 or children == -1:
        print("Program Terminated!")
        income, children= -1, -1
    else:
        help = finnacialAssistance(income, children)
        if help == None:
            print("You can aquire no finnancial aid.")
        else:
            print("You can aquire {} in finnancial Aid".format(help))
        
#PROBLEM P5.30
print("PROBLEM P5.30")
finished = False
while finished == False:
    password = input("Enter a password (must have upper, lower, digit, and be greater than 8 chars): ")
    confirmation = input(str("Confirm password: "))
    if password != confirmation:
        print("[!] Passwords do not match [!]")
    else:
        if strongPassword(password) == True:
            print("Your Password is Strong!")
            finished = True
        else:
            print("[!] Your Password is Not Strong Enough [!]")
            finished = True # uncomment to loop until password is strong

    
