nList = []
a = int(input("Enter the lower range int: "))
b = int(input("Enter the upper range int: "))

for x in range(a, b):
    n = x**2
    if a <= n and n < b:
        nList.append(n)
print(nList)


classes = ["CS 110", "CS 120", "CS 210", "CS 215", "CS 300"]
classes.reverse()
result = ""
for x in classes:
    result = result + x + ", "
    print(x, end=", ")
result = result[:len(result)-2]
print(result)
