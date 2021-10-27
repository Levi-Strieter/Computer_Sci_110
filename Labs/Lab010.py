nList = []
a = int(input("Enter the lower range int: "))
b = int(input("Enter the upper range int: "))

for x in range(a, b):
    n = x**2
    if a <= n and n < b:
        nList.append(n)
if len(nList) == 0:
    print("No Values")
else:
    print(nList)


classes = ["CS 110", "CS 120", "CS 210", "CS 215", "CS 300"]
classes.reverse()
result = ""
for x in classes:
    result = result + x + ", "
result = result[:len(result)-2]
print(result)

import random
randList = []
seen = []
for x in range(0,30):
    randList.append(random.randint(0,10))
print(randList)

for x in randList:
    occurence = randList.count(x)
    if x not in seen:
        print(x, "Occurs", occurence, "time") 
    seen.append(x)
print()

menu = {
    # "Lt. Tso Chicken": float(17.5),
    # "Half Century Eggs": float(2.5),
    # "Durian Ice Creame": float(5)
}
print("Type Q to quit")
finished = False
while finished == False:
    try:
        item = input("Enter the Food You want: ")
        if item.upper() == "Q":
            finished = True
            break
        price = float(input("Enter Price of item: "))
        menu[item] = float(price)
        
    except ValueError as error:
        print(error)

print("Welcome to No. 2 Kitchen.\nOrder")
# print all items ordered
for key, value in menu.items():
    print("%10s" % key, "%15.2f" % value, "$")
# print rest of reciept
print("=" * 40)
print("Subtotal%25.2f" % sum(menu.values()))
print("Tax","(7%)", "%24.2f" % (.07*sum(menu.values())))
print("=" * 40)
print("Total%28.2f" % (.07*sum(menu.values()) + sum(menu.values())))
print()
print("Tip Suggestion")
print("10%:","%28.2f" % ((.07*sum(menu.values()) + sum(menu.values())) * .1))
print("15%:", "%28.2f" % ((.07*sum(menu.values()) + sum(menu.values())) * .15))
print("20%:", "%28.2f" % ((.07*sum(menu.values()) + sum(menu.values())) * .2))
print()




