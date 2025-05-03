import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def distance_to(self, other):
        return math.sqrt((self.__x - other.getX())**2 + (self.__y - other.getY())**2)

class ColorPoint(Point):
    def __init__(self, x=0, y=1, color="xanh"):
        super().__init__(x, y)
        self.__color = color

    def read(self):
        super().read()
        self.__color = input().strip()

    def print(self):
        print(f"{super().__str__()}: {self.__color}")

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

class C002454:
    def testCase1(self):
        A = ColorPoint(5, 10, "trắng")
        A.print()

    def testCase2(self):
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()

    def testCase3(self):
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C.getX(), C.getY(), C.getColor())
        D.print()
        D.setColor("vàng")
        D.print()
        C.print()

    def main(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()

if __name__ == "__main__":
    test = C002454()
    test.main()
