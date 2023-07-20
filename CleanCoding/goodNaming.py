class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,length,bredth, stratingPoint) -> None:
        self.length = length
        self.bredth = bredth
        self.startingPoint = stratingPoint
    def getArea(self):
        return self.length*self.bredth
    
def BuildRectangle():
    RectanglePoint = Point(10,20)
    rect = Rectangle(10,50,RectanglePoint)
    
    return rect

myRectangle = BuildRectangle()
print(myRectangle.getArea())
