#Hierarchical Inheritance

class Parent:
    def func1(self):
        print("This is in parent Class")


#Derived class 1
class Child1(Parent):
    def func2(self):
        print("This is in child 1")

#Derived class 2
class Child2(Parent):
    def func3(self):
        print("This is in child 2")


#Driver's code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()

object2.func1()
object2.func3()
