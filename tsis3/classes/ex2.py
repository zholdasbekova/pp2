class Shape:
    def area(self):
        return 0
class Square(Shape):
    def init(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

length=int(input("enter length:"))
square_obj = Square(length)
shape_obj = Shape()
print("Area of Shape:", shape_obj.area())
print("Area of Square:", square_obj.area())