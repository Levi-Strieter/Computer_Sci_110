# Files 

- open - open a file 
```python
data = open('contents/json/sample.json', 'r')
#            the path                     read this file only
for line in data:
    line = line.rstrip()
    print(line)
```
```python
values = []
data = open('contents/json/sample.json', 'r')
#            the path                     read this file only
for line in data:
    values.append(line.rstrip().split(":")) # seperates the big lists into sub lists after the colon
print(values)
```
```python
values = []
data = open('contents/json/sample.json', 'r')
#            the path                     read this file only
for line in data:
    values.append(line.rstrip().split(":")) # seperates the big lists into sub lists after the colon

for element in values:
    print('_!_'.join(element))              # combine the elements with the _!_
```
```python
import urllib.request # importing only needed method to access content of a website

url = "https://webpage.com"
content = urllib.request.urlopen(url)
content.readLine()     # skip the first line
webPage = content.read().decode('utf-8')
words = webPage.split()
content.close()
for line in words:
    print(line)
```
```python
try:
    userinput = int(input("Enter num:"))
except ValueError as exception:
    print(exception)
```