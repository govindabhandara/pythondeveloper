class Parent1:
    def m1(self):
        print("Parent1 class -m1() method")
class Parent2:
    def m1(self):
        print("Parent2 class -m1() method")
class Child(Parent1,Parent2):
    def m2(self):
        print("child class -m2() method")

c1=Child()
c1.m1()
c1.m2()
