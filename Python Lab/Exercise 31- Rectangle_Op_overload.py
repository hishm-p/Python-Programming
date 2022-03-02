class Rectangle:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def __lt__(self, other):
        if (self._width * self._length) < (other._length * other._width):
            return True


rect1 = Rectangle(2, 5)
rect2 = Rectangle(3, 6)

if rect1 < rect2:
    print("Rect1 is small")
else:
    print("Rect2 is small")