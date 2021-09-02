# Third Lecture 9/2/21 

### Decisions 

##### strings 
- strings are anything, ex- A-z, 0-9, @
- starts with matching ""
- string has length including whitespace 
- can add and multiply strings 
    ```python 
        print("fred" + "fred")
    ```
    ```
        "fredfred" 
    ```
    ```python
        print("fred" * 3)
    ```
    ```
        "fredfredfred"
    ```
- can access individual element of string 
    ```python
        name = "fred"
        print(name[2])
    ```
    ```
        "e"
    ```
###### data storage
- everyhting in computer is stroed as number 
    - ASCII- standard chacters on keyboard 
        - only 128 characters 
    - unicode 
        - represents to 65,000 characters 
        - UTF-16 has an addidtional 32 bits
    - colors as numbers 
        - RGB value ex- 255, 0, 0 

- computer sees 65 
    - could be letter, color, or int
        - thats why python makes you tell if that value is string or int, float, etc.
```python
floatVal = 43.5
intVal = int(floatVal)
print(intVal)
```
```
43
```

###### decsions 
- make a flowchart of a the program 
- if statement 
```python
if condition:
    do_this # condition is true
else: # else part is optional
    do_that # condition is false
```
- uses indentation as the method for determing if the code is part of the if statement or program
    - operators for if statement include ==, <, >, >=, <=, !=, 
        - when using the == sign its so exact that 10.000000002 will still be false (convert float to int)

- also has else if statement- elif 
```python
if score > 89:
    grade = "A"
elif score > 79:
    grade = "B"
...
else:
    grade = "F"
```

###### bools 
- Geaorge bool created a T or F 
- is stored as 1 bit 
    - operators = "and" "or" "not"




 