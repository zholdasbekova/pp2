import math

#radian
def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
radian = degree_to_radian(degree)
print("Output radian:", round(radian, 6))


#trapezoid
def trapezoid_area(height, base1, base2):
    return 0.5 * height * (base1 + base2)

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = trapezoid_area(height, base1, base2)
print("Expected Output:", area)


#polygon
def polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = polygon_area(num_sides, side_length)
print("The area of the polygon is:", area)


#parallelogram
def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base, height)
print("Expected Output:", area)
