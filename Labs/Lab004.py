
s = 1
for n in range(1, 6):
   s = s + n
   print(s)

# loop prints: 2, 4, 7, 11, 16

s = 1
n = 1
MAX = 6
while n < MAX:
    s = s + n
    print(s)
    n = n + 1

# loop prints: 2, 3, 4, 7, 11, 16


# product = 1
# n = 1
# MAX = 5
# while n < MAX:
#     product = product * n
#     print(product)
 
# [!] ERROR [!] infinite loop n is always 1 [!] ERROR [!]

i = 10
j = 0
n = 0
print("\ni    j    n" )
while i > 0:
    i = i - 1
    j = j + 1
    n = n + 1 - j
    print("%0d %4d %4d" % (i, j, n), end="")
    print("")

''' 
i    j    n
9    1    0
8    2   -1
7    3   -3
6    4   -6
5    5  -10
4    6  -15
3    7  -21
2    8  -28
1    9  -36
0   10  -45  
'''

# 5. Write a loop that computes all even numbers between 2 and 100 (inclusive):
total = 0
for x in range(2, 101, 2):
    total = total + x
print(total)

# 6. Write a loop that computes the sum of all squares between 1 and 150 (inclusive):
import math 
total = 0 
counter = 0
checkSquare = lambda x: True if round(math.sqrt(x), 2) * round(math.sqrt(x), 2) == x else False
while counter <= 150:
    isSquare = checkSquare(counter)
    if isSquare == True: 
        total += counter 
        counter += 1
    else:
        counter += 1
print(total)

'''7.	Given the list a = [1, 12, 42, 20, -1], 
what is the value of total after the following loop has been executed?'''
a = [1, 12, 42, 20, -1]
total = 0
for i in range(5):
  total = total + a[i]

# the total will be 74... 0+1 -> 1+12 -> 12+42 etc.

'''8.	Given the list a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 
what is the value of total after the following loop has been executed?'''
a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
total = 0 
for i in range(9, -1, -2):
  total = total + a[i]

# the toal will be 12... 0+0 -> 0+2 -> 0+4 -> etc.



  

