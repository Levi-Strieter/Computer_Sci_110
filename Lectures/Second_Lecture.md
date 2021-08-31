# Second Lecture 8/31/21
####Variables
Variables are a storage location that holds a value
- Strings 
- Floats
- int
- bool

amount = amount + interest 
- evaluates right hand side "amount" first then becomes the new amount + interest
- right hand side is computed first then its variable is updated 

###### variable naming 
1. must be letter for first character or '_'
2. can't use symbols 
3. case sensitive 
4. can't be python keywords ex-(False, del, global)

--Naming convention--
- Camel case ex-interstRate
- Constants are upper case ex- PENNY_VAL = 0.01


###### arithmitic
- ** for powers
- (a+b)/2 not a+b/2
- can import math for things like "sin(x)"

###### comments
- use hashtag "#"
- anything to right of "#" is not excuted or even read by python compiler
- only use comments after tricky bit of code

###### user input
```python
testInput = input("please enter message")
print(testInput)
print(testInput * 2)
```
- In the console it will ask the message in quotes, then print the value entered after the message
- line 3 returns "1010" if entered val is "10"
- always returns a string, unless specified
```python
testInput = int(input("please enter number"))
print(testInput)
print(testInput * 2)
```
- only allows a number to be entered 
- line 3 would print "10" if number entered is "5"

###### Printing 
- comma needed to seperate vals in print()
```python
var = 43
print("yo", 10, "number", 291, var)
```
"yo 10 number 291 43"

