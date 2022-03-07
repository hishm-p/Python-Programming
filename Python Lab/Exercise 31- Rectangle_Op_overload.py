class Rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def __lt__(self,other):
        if(self.__length * self.__width) < (other.__length * other.__width):
            return True


rect1 = Rectangle(3, 5)
rect2 = Rectangle(3, 6)

if rect1 < rect2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller area")
