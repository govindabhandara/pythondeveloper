class Parent1:
    def m1(self):
        print("parent 1 -m1() method")

class Parent2:
    def m2(self):
        print("parent 2 -m2() method")
class Child(Parent2, Parent1):
    def m3(self):
        print("child -m3()method")

c1=Child()
c1.m1()
c1.m2()
c1.m3()