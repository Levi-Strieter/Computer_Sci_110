# ASCII MESSAGE TO BE DECODED 
# Computers sok!

# problem 1
n = 10
k = 2
r = n
print("n:", n, "k:", k, "r:", r)
if k < n :
  r = k
print("n:", n, "k:", k, "r:", r, "\n")
# k is less than n so the variable r now equals k #

# problem 2
n = 1
k = 2
if n < k :
  r = k
else :
  r = k + n
print("n:", n, "k:", k, "r:", r)
# since n is less than k a new var is being defined, r, which equals the same val as k #

# problem 3 
assets = float(input("Enter the monetary value of your assets: "))
if assets < 100 :
   diet = "Ramen Diet"
elif assets < 100000 :
   diet = "Healthy diet"
else :
   diet = "Steak and Lobster diet"
print("You need to be on the" , diet)


'''
1.	Basic if else Statements to determine if a number is even or odd
#Divide the number by 2 and multiply by 2 if the result is same as #input then it is an even number else it is an odd number.
#ask user to enter an integer
#if the number is even, print the message that it is even
#else print the message that it is odd
'''

userInput = int(input("enter a number: "))

mathOperation = lambda x: x%2
if mathOperation(userInput) == 0:
    print("Number is even")
else:
    print("Number is odd")



'''
2.	Use elif for exclusive conditions:
Ask the user for their age
if age < 13 print you are still a child if age < 20 print you are a teenager 
if age < 63 print you are an adult
else print you are a senior citizen
    	This algorithm has a flaw if the user enters a negative number, please fix it.
'''

userInput = int(input("Enter your age: "))
if userInput < 0:
    print("FALSE INFO")
else:
    if userInput > 63:
        print("senior citizen")
    if userInput < 63:
        print("adult person you are")
    if userInput < 20:
        print("teenager you are")
    if userInput < 13:
        print("you are a youngin")




'''
3.	Utilize Nested ifs to add more condition from the algorithm above (#2):
if age < 13, check if age < 5 then print pre-schooler else print child if age < 20, 
print teenager if age < 63, check if age is < 32 print young adult, else print adult
else print senior citizen
'''
userInput = int(input("Enter your age: "))
if userInput < 0:
    print("FALSE INFO")
else:
    if userInput < 13: 
        if userInput < 5:
            print("pre-schooler")
        else:
            print("child")
    elif userInput < 20:
        print("teenager")
    elif userInput < 63:
        if userInput < 32:
            print("yvng adult")
        else:
            print("senior citizen")

