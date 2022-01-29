from math import pi

def area():
    r=int(input("\nEnter the radius of the circle to find area: "))
    a=pi*r*r
    print("Area of the Circle: ",a)
    

def perimeter():
    r=int(input("\nEnter the radius of the circle to calculate perimeter: "))
    p=2*pi*r
    print("Perimeter : ",p)
    