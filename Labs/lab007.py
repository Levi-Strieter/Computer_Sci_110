#Strings Lab 

'''
1.	Write a Python program that prompts the user to enter a 5-letter word,
 and then prints the first, third, and fifth letters of that word.
'''
import random


string = input("Please enter a 5 letter word: ")
print("The first, third, and fifth letters are:", string[0], string[2], string[4])


'''
2.	Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string
'''
string1 = input("Input string 1: ")
string2 = input("Input string 2: ")
modString1 = string1.replace(string1[0], string2[0])
modString2 = modString1.replace(string1[1], string2[1])

modString3 = string2.replace(string2[0], string1[0])
modString4 = modString3.replace(string2[1], string1[1])

print("resulting string:", modString2, modString4)

time = input("What is the time please (HH:MM)? ")

time = time.split(":")
print("Thanks! It is now {} minutes after {} o'clock.".format(time[1], time[0]))



string = input("Enter a random string: ").lower()
repeatedLetters = []
repeatedLettersIndex = 0
for x in string:
    repeated = string.count(x)
    if repeated > 1:
        if x not in repeatedLetters:
            repeatedLetters.append(x) 
string = list(string)
for x in repeatedLetters:
    firstOccurence = string.index(x)
    for y in range(firstOccurence+1, len(string)):
        if string[y] == repeatedLetters[repeatedLettersIndex]:
            string[y] = "*"
    repeatedLettersIndex += 1
for x in string:
    print(x, end="")

print()

    


string = input("Enter a string: ")

if len(string) < 3:
    print(string)
elif string.endswith("ing"):
    string = string.strip("ing")
    
    print("word is:", string + "ly")
elif len(string) >= 3:
    print("word is:", string + "ing")
        