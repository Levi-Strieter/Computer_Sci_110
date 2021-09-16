# Functions 

 - inputs are supplied by specifying params 
 - outputs are returned by functions 

 ```python
def myFunc(arg1, arg2):
    value = arg1 * arg2
    return value

myFunc(3, 4)
 ```
 This will first call myFunc() with arg1=3 and arg2=4 then return 12...value = (3 * 4)

 ex- 
 ```python
def isEven(theNumber):
    if theNumber % 2 == 0:
        return True 
    else:
        return False

print(isEven(6)) # returns True
 ```

- to use func you need to know only
    - what it needs as input 
    - what it produces

###### Benifits of func
- uniformity 
- dont have to know how function works 
- multiple people can code huge program 
- Can call functions from import 
    - very modular
    - invoke file name then function 
- can invoke help()... help(math)

###### Using Funcs 
- need to have a test file to test function
- variable scope (any var declared in func is not accsessable outside of func)
- anything defined outside of function can be called from inside fucntions
    - global variables are not suggested 
- everything func needs should be passed to funcs as argument 
    - external vars are ok for modularity
```python
def func():
    global num

def fun2():
    print(num+10)
```




