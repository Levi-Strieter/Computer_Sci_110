import math
def sphereSA(radius) :
   return 4*math.pi*radius**2

# radius = 4
# print(sphereSA())


'''Practice Exam Question
a - int 
b - int  
c - int 
'''


def root1(a,b,c):
   discriminate = b**2 - 4 * a * c
   return -b + math.sqrt(abs(discriminate)) / (2 * a)

def root2(a,b,c):
   discriminate = b**2 - 4 * a * c
   return -b - math.sqrt(abs(discriminate)) / (2 * a)
