# Write a Python program to simulate the final exam 
# scores of N students in a given class. The user will 
# provide the value of N. Print only the distribution of 
# the grades, how many students got A, B, C, D and F. 
import random
from typing import Callable
def simGrades(N, M):
    counter = 0
    gradeList = []
    A, B, C, D, F = 0, 0 , 0 , 0, 0
    avgA, avgB, avgC, avgD, avgF, = 0,0,0,0,0
    for simRuns in range(0, M):
        while counter <= N:
            grade = random.randint(0, 4)
            gradeList.append(grade)
            counter += 1
        for number in gradeList:
            if number == 0: A += 1
            elif number == 1: B += 1
            elif number == 2: C += 1
            elif number == 3: D += 1
            elif number == 4: F += 1
    
    avgA = A/M
    avgB = B/M
    avgC = C/M
    avgD = D/M
    avgF = F/M

    return avgA, avgB, avgC, avgD, avgF


def WRandom(lower, upper):
    nums = [lower, upper]
    small = min(nums)
    large = max(nums)
    return random.randint(small, large)


M = 77
A, B, C, D, F = simGrades(30, M)
print("{} obtained A (after {} sims)\n{} Obtained B (after {} sims)\n{} Otained C (after {} sims)\n{} Obtained D (after {} sims)\n{} Obtained F (after {} sims)".format(A,M,B,M,C,M,D,M,F,M))

value = WRandom(random.randint(-100, 100), random.randint(-100, 100))

number=random.randint(1, 20)

name = input("Hello! What is your name? ")
print("Well,", name, "I am thinking of a number between 1 and 20.")
guesses = 0
while guesses < 6:
    guess = int(input("Take a Guess: "))
    guesses += 1
    if guess is not number:
        if guess < number:
            print("Your Guess is Too Low!")
        else:
            print("Your Guess is Too High!")
    else:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses))
        guesses = 10



usersNumbers = []
dealersNumbers = []
dealerBust = False
for x in range(0, 2):
    number = random.randint(1, 11)
    dealerNum = random.randint(1, 11)
    usersNumbers.append(number)
    dealersNumbers.append(dealerNum)
finished = False
while finished == False:
    while sum(dealersNumbers) < 17:
        nextNum = random.randint(1,11)
        dealersNumbers.append(nextNum)
        if sum(dealersNumbers) > 21:
            print("The Dealer Busted, Numbers were", dealersNumbers, "\nYour Numbers were", usersNumbers)
            dealerBust = True
    print("Your Numbers are,", end="")
    for num in usersNumbers:
        print(num, end=",")
    print("Would you like you stand (S) or draw (D)?")
    sh = input("Stand or Draw (S/D): ")

    if sh.upper() == "D":
        nextNum = random.randint(1,11)
        usersNumbers.append(nextNum)
        if sum(usersNumbers) > 21:
            print("You Busted Suks to Suk")
            print("Dealer had numbers", dealersNumbers)
            finished = True
    else:
        if sum(dealersNumbers) > sum(usersNumbers) and dealerBust == False:
            print("The Dealer Wins, numbers were: ", end="")
            for num in dealersNumbers:
                print(num, end=",")
            print("\nYour numbers were ", end="")
            for num in usersNumbers:
                print(num, end=",")
            finished = True
        else: 
            print("You Win, numbers were: ", end="")
            for num in usersNumbers:
                print(num, end=",")
            print("Dealers numbers were: ", end="")
            for num in dealersNumbers:
                print(num, end=",")
            finished = True
    

