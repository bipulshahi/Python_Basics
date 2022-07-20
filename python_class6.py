#Inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)


#object of person class
x1 = Person("John","Doe")
x1.printname()


class Student(Person):
    pass

x2 = Student("Mike","Olsen")
x2.printname()

print(type(x1))
print(type(x2))
