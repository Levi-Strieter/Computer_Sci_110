# Strings 

##### string funcs/defs
- strings can be 0, 1 or more characters
    - strings can allocate memory very well 
    - its much harder to shrink memory rather than expand memory 
- format specifiers
- a string is an object 
    - object is an entity that has a value and behavior (functions)
        - sudent & car
            - student can study, sleep, eat 
            - cars can go forward, go backward, go left 
            - (can only do functions that are built in, only some things have the ability to change those funcitons)
    - str.lower() - returrns lower case copy 
    - str.upper() - vice versa ^
    - str.isupper() - checks only characters
    - str.replace(old, new) - returns a copy of new string doesnt change original 
        - returns new copy has to init to a var 
            ```python
            myString = "levi"
            string = myString.upper()
            print(string)
            "LEVI"
           
            myString.upper().isupper() # returns copy but doesn't change original
            print(myString)
            "levi"
            ```
        - can do a bool val in var
        ```python
            val = string[0] == "(" and string[3] == ")"
            "returns False or True "
        ```
        

