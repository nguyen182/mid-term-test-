from bai11 import Point
import math

class PointTest:
    def main(self):
        pA = Point(3, 4)
        print("Toa do diem A:")
        pA.print()

        pB = Point()
        print("Nhap toa do diem B:")
        pB.read()
        print("Toa do diem B:")
        pB.print()

        pC = Point(-pB.getX(), -pB.getY())  
        print("Toa do diem C:")
        pC.print()

        print("Khoang cach tu B den goc O:", round(pB.distance(), 2))
        print("Khoang cach tu A den B:", round(pA.distance(pB), 2)) 

if __name__ == "__main__":
    test = PointTest()   
    test.main()          
