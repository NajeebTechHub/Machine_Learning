# Q-1: Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.


class Rectangle:

    def __init__(self,l,w):
        self.length = l
        self.width = w

    def parameter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print('The length of the rectangle is : ',self.length)
        print('The width of the rectangle is : ',self.width)
        print('The perameter of the rectangle is : ',self.parameter())
        print('The area of the rectangle is : ',self.area())

my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
