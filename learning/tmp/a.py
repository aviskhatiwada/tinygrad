#!/usr/bin/python3

class Lim:
    def __init__(self, a):
        self.a=a
class In(Lim):
    def __init__(self,b):
        super().__init__(b)
        self.b=self.a+10
        print(self.a, self.b)


class Shape:
    @staticmethod
    def area():
        if isinstance(self, C):
            return 2 * self.r


class C(Shape):
    def __init__(self,r):
        self.r=r

cir=C(1)
print(cir.area())

