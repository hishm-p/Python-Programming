from graphics import rectangle
import graphics.circle

import graphics.graphics3D.cuboid
from graphics.graphics3D.sphere import *

l=int(input("\nEnter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))  
a=rectangle.area(l,b)
print("Area : ",a)
p=rectangle.perimeter(l,b)
print("Perimeter : ",p)

a=graphics.circle.area()
p=graphics.circle.perimeter()

l=int(input("\nEnter the length of the cuboid : "))
b=int(input("Enter the breadth of the cuboid : "))
h=int(input("Enter the height of the cuboid : "))
a=graphics.graphics3D.cuboid.area(l,b,h)
print("Area of cuboid : ",a)
p=graphics.graphics3D.cuboid.perimeter(l,b,h)
print("Perimeter of cuboid : ",p)

graphics.graphics3D.sphere.area()
graphics.graphics3D.sphere.perimeter()



