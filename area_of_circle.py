name = input("Hello, what`s your name?: ")
print("Nice to meet you, " + name + "! Just insert the radius of circle and I will show its area")

radius = input("Input the radius: ")

import math

area_of_circle = 3.14 * (int(radius)**2)

print("Area of circle is " + str(area_of_circle))