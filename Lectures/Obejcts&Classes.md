# Object ORiented 

- objects that have associated data fields and methods 
    - ex 
        - ###### data
        - speed 
        - direction 
        - loaction 
        - fuel 
        - ###### methods 
        - turn(angle, curvature)
        - setSpeed(speed, acceleration)
        
```python
class counter:
    #                  default var (Counter(3) is not needed)
    def __init__(self, counter = 0)
        # member constructer variable (accessable to all methods)
        self._value = 0
        self._value = counter
    def reset(self):
        name = "Ryan" # this variable is only accessabele by the reset method
        return self._value + 1
    def click(self):
        return self._value = 0

#object of type <Counter>
myCounter = Counter()
#object   method
myCounter.reset()
myCounter.click()
```
###### data 
- _Value 
    - "_" means variable is private
###### methods 
- __init__ 
    - 0, 1, or more accessor methods that return value of instance variable 
    - initilizes all data to the class 
- self - refers to self of class

