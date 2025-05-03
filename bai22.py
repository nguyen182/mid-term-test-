from bai11 import Point
from bai21 import LineSegment
import math

class LineSegmentTest:
    def testCase1(self):
        print("Test Case 1:")
        pA = Point(2, 5)
        pB = Point(20, 35)
        AB = LineSegment(pA, pB)
        print(AB)  
        AB.move(35, 51)
        print(AB) 

    def testCase2(self):
        print("Test Case 2:")
        CD = LineSegment()
        CD.read()  
        print("|CD| = {:.2f}".format(CD.length())) 

    def testCase3(self):
        print("Test Case 3:")
        danhsach = []
        n = int(input("Nhap so luong doan thang n: "))
        for i in range(n):
            l1 = LineSegment()
            l1.read() 
            danhsach.append(l1)

        for item in danhsach:
            print(item)
            print("Chieu dai:", item.length())

        danhsach.sort(key=lambda seg: seg.length())
        print("Doan thang sau khi sap xep theo chieu dai:")
        for item in danhsach:
            print(item)
            print("Chieu dai:", item.length())

    def main(self):
        while True:
            s = input("Nhập kịch bản muốn chạy 1/2/3/exit: ")
            if s == '1':
                self.testCase1()
            elif s == '2':
                self.testCase2()
            elif s == '3':
                self.testCase3()
            elif s == 'exit':
                break
            else:
                print("Kịch bản không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    test = LineSegmentTest()
    test.main()
