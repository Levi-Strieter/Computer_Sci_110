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


class Bullseye(object):
    def __init__(self, windowWidth=1000,windowHeight=1000):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.center = [self.windowWidth / 2, self.windowHeight / 2]
        self.circleDiameter = self.calculateLines()
        self.anchors = self.getXY()
        self.window = self.createWindow()
        self.canv = self.createCanvas()
        

    def run(self):
        self.Oval()

    def createWindow(self):
        w = graphics.GraphicsWindow(self.windowWidth, self.windowHeight)
        return w

    def createCanvas(self):
        canv = self.window.canvas()
        return canv

    def destroy(self):
        self.window.wait()

    def calculateLines(self):
        circleDiameter = ((self.windowWidth / 2) - 50) / 4
        circleDiameter = round(circleDiameter)
        return circleDiameter
        

    def getXY(self, x=500, y=500):
        # start at center of canvas
        # if iteration is 2 find width of other circle and then move x, y val to account for movement
        anchors = {
            "x": [],
            "y": []
        }
        for z in range(4, 0, -1):
            x = self.center[0] + ((self.circleDiameter * z) + 50)
            anchors["x"].append(x)
            y = self.center[1] + ((self.circleDiameter * z) + 50)
            anchors["y"].append(y)

        return anchors
    
    def Oval(self):
        for value in self.anchors.values():
            x = -1
            self.canv.drawOval(662, 662, 112, 112)

            # self.canv.drawOval(self.anchors[value[3]], self.anchors[value[3]], self.circleDiameter, self.circleDiameter)
            self.destroy()

if __name__ == "__main__":
    # 50 x 50 starting circle
    # gets bigger by 100
    draw = Bullseye(1000,1000)
    draw.run()