import Lab_Library.graphics as graphics
import math

done=False
while done == False:
    try:
        radius = float(input("enter radius: "))
        done = True
    except ValueError:
        print("[!] Enter a int [!]")

findArea = lambda radius: math.pi * radius**2
findCircumfrence = lambda radius: (2 * math.pi) * radius
findSA = lambda radius: (4 * math.pi) * radius**2
findVolume = lambda radius: ((4/3) * math.pi) * radius**3
done=False
def findVals(radius):
    area = findArea(radius)
    circumfrence = findCircumfrence(radius)
    sa = findSA(radius)
    volume = findVolume(radius)
    return area, circumfrence, sa, volume

vals = findVals(radius)
print("Circle Area: %4.2f" % vals[0])
print("Circle Cirumference: %4.2f" % vals[1])
print("sphere sa: %4.2f" % vals[2])
print("sphere volume: %4.2f" % vals[3])

# testCase = [10, 15, 69]
# for x in testCase:
#     print("Area of circle x={}, val={}".format(x, findArea(x)))
#     print("circumfrence of circle x={}, val={}".format(x, findCircumfrence(x)))
#     print("SA of circle x={}, val={}".format(x, findSA(x)))
#     print("volume of circle x={}, val={}".format(x, findVolume(x)))
    

# Test Case Area of Circle
# input     output
#  10       314.16
#  15       706.86
#  69       14957.12

# Test Case circumfrence of Circle
# input     output
#  10       62.83
#  15       94.25
#  69       433.54

# Test Case SA of Sphere
# input     output
#  10       1256.64
#  15       2827.43
#  69       59828.49

# Test Case Volume of Sphere
# input     output
#  10       4188.79
#  15       14137.17
#  69       1.38×106

window = graphics.GraphicsWindow(500, 500)
canvas = window.canvas()

canvas.setColor(0, 255, 0)
canvas.drawOval(0, 0, 500, 500)

canvas.setColor(255, 0, 0)
canvas.drawOval(50, 50, 400, 400)

canvas.setColor(0, 0, 255)
canvas.drawOval(100, 100, 300, 300)

canvas.setColor(255, 0, 255)
canvas.drawOval(150, 150, 200, 200)

canvas.setColor(255, 255, 255)
canvas.drawOval(200, 200, 100, 100)

window.wait()
