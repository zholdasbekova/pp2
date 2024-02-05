class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def init(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

rectangle_obj = Rectangle(length, width)

print("Area of Shape:", rectangle_obj.area())
print("Area of Rectangle:", rectangle_obj.area())
