#Define a class named Circle which can be constructed by a radius. The Circle class has a method 
# which can compute the area.
#Hints:
#Use def methodName(self) to define a method.
import math

class Circle(object):
    def __init__(self, radius = 1):
        self.radius=radius

    def circle_area(self):
        return Circle.pi()*(self.radius**2)

    @staticmethod
    def pi():
        return math.pi

circle5 = Circle(5)
circleD = Circle()
print(Circle.pi())
print (circle5.circle_area())
