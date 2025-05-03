from bai11 import Point
import math

class LineSegment:
    __d1 = Point()
    __d2 = Point()

    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)

        if len(args) == 2:
            if not (isinstance(args[0], Point) and isinstance(args[1], Point)):
                raise TypeError("Nhập điểm!!!")
            self.__d1 = args[0]
            self.__d2 = args[1]

        if len(args) == 4:
            if not all(isinstance(item, int) for item in args):
                raise TypeError("Only Intergers can be added")
            self.__d1 = Point(args[0],args[1])
            self.__d2 = Point(args[2],args[3])

        if len(args) == 1:
            if not isinstance(args[0], LineSegment):
                raise TypeError("Only one LineSegment can be added")
            self.__d1 = Point(args[0].__d1.getX(),args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(),args[0].__d2.getY())

    def read(self):
        s = input("Nhap diem vao doan thang: ")
        self.__d1 = Point(int(s.split()[0]), int(s.split()[1]))
        self.__d2 = Point(int(s.split()[2]), int(s.split()[3]))

    def __str__(self):
        return "[({},{}); ({},{})]".format(self.__d1.getX(),self.__d1.getY(),self.__d2.getX(),self.__d2.getY())
    
    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)
    
    def angle(self):
        return int(math.atan2(self.__d2.getY()-self.__d1.getY(), self.__d2.getX()-self.__d1.getX()))
    
