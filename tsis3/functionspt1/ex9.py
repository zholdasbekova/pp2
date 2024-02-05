import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius_input = float(input("Enter the radius of the sphere: "))
volume_result = sphere_volume(radius_input)
print(f"The volume of the sphere with radius {radius_input} is: {volume_result:.2f} cubic units")
