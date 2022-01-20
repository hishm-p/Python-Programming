class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def area(self):
        return self.l*self.b

    def perimeter(self):
        return 2*(self.l+self.b)

    def compare(self,rectangle):
        if self.area() == rectangle.area():
            print("\nRectangles with the dimensions entered have equal areas")
        else :
            print("\nRectangles with the dimensions entered have different areas")     

l1=int(input("Enter the length of the first rectangle: "))
b1=int(input("Enter the breadth of the first rectangle: "))

first=Rectangle(l1,b1)
print("Area of First rectangle is:",first.area())

l2=int(input("Enter the length of the second rectangle: "))
b2=int(input("Enter the breadth of the second rectangle: "))

second=Rectangle(l2,b2)
print("Area of Second rectangle is:",second.area())

first.compare(second)
