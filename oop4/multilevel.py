class Grandparent:
    def m1(self):
        print("Grandparent -m1() method")
    def m2(self):
        print("Grandparent -m2() method")
class Parent(Grandparent):
    def m3(self):
        print("Parent -m3() method")
class Child(Parent):
    def m4(self):
        print("child -m4() method")

c1=Child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()