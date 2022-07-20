#Multiple Inheritances

#Parent class 
class Base1:
    def __init__(self):
        self.str1 = "Google"
        print("Base1")

class Base2:
    def __init__(self):
        self.str2 = "Microsoft"
        print("Base2")


class Derived(Base1 , Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1 , self.str2)

o1 = Derived()
o1.printStrs()
