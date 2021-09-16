import math 
import Lab_Library.lab05 as quadratic
print("this is result because it has code outide of the def")
#print(help(quadratic))

sphereSA = lambda r: 4*math.pi*r*r

def distance(d, v, a, t):
    dComponent = d
    vComponent = v*t
    aComponent = (a*t*t)/2
    return dComponent+vComponent+aComponent
 
print(sphereSA(0.0189))
print(sphereSA(0.0335))
print(sphereSA(0.0366))

print(distance(10, 2, 5, 3))


# Exam Question...Lab_Library.lab05.py contains all functions 
while True:
        solveEquation = str(input("Do you want to solve equation y/n: "))
        if solveEquation == 'Y' or solveEquation == 'y':
            while True:
                a = int(input("Enter a: "))
                if a == 0:
                    print("[!] a can't be equal to 0 [!]")
                else:
                    break
            b = int(input("Enter b: "))
            c = int(input("Enter c: "))
            
            root1val = quadratic.root1(a,b,c)
            root2val = quadratic.root1(a,b,c)
            print("root1:", root1val, " root2: ", root2val)
            
        else:
            print("GoodBye")
            break

