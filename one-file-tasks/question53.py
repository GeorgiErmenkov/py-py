#Question 53
#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class 
# has a method which can compute the area.
#Hints:
#Use def methodName(self) to define a method.

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

Rect1 = Rectangle(5, 10)
print(Rect1.area())

