# Loops 

###### While Loop
- conditional loop that is executed as long as the condition is satisfied 
```python
while slices < Size:
    slices = slices + 1 # adds this until slices is greater than size 
```

###### For loop
- loop that is count controlled 
    - loops until the counter is satisfied 
    - end val is not included in range
```python
for slices in range(0, size):   # slices is 0, 0  - N amount of times
    pepsi = pepsi-6             # iterates until range o 0-N is completed 
```
- range(m, n)  M <= number < n
    - can be incremented range(0, 8, -2) # 6, 4, 2
    - if the logic of for loop is wrong program won't break it just won't run the loop
```python
s = 1
for n in range(1, 6):
    s = s + n
    print(s)
```
###### Trace Table for above loop
```
s  n  print
1  1   2
2  2   4
4  3   7
7  4   11
11 5   16
```

###### example
add all even numbers 2-100 
```python
sumVal = 0
i = 2
while i <= 100:
    sumVal = sumVal + i
    print(i)
    i = i + 2 

print(sumVal)
```
```python
sumVal = 0
for i in range(2, 101, 2):
    sumVal = sumVal + i

print(sumVal)
```
Same Programs^^^

###### print feautures
- % is format specifier 
print("%9.2f")

###### data structure 
- lists, data types dont matter
```python
    - radi = [1, 2.3, "Fred"]
    - radi[0], # 1
    - radi.append("what")
    - radi.insert(3, 2) # 1, 2.3, 3, Fred
    - radi.remove()
    - radi.reverse() #sort from greatest to least( cant sort different data types )
    - radi.sort() # sort from least to greatest( cant sort different data types )
    - radi.pop() 
```
- built in data types of lists
    - len, max, min, sum

```python
index = 0
while index < len(radi):
    print(radi[index])
    index = index + 1 # index += 1
                      # same thing^^
for x in radi:
    print(x)
```

