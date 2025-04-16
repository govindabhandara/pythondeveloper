class Test:
    a=10

    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c=30

    @classmethod
    def m2(cls):
        cls.d=40
        Test.e=50

    @staticmethod
    def m3():
        Test.f=60

    @staticmethod
    def m4():
        Test.g=70

t1=Test()
t2=Test()

t1.m1()
t1.m2()
t1.m3()
t1.m4()
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)