import matplotlib 

class graph():
    def __init__(self, name) -> None:
        self.xIntervals = 1
        self.yIntervals = 1
        self.xMin = 100
        self.yMin = 100
        self.name = name
        


    def makeTable(self, equation):
        xVals = []
        yVals = []
        
        for x in range(self.xMin):
            # equation: 10x+13 = y
            xVal = 0
            xVals.append(xVal)

        return xVals, yVals

