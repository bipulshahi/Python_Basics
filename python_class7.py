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
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname , self.lastname ,
              "to the class of",self.graduationyear)


x2 = Student("Mike","Olsen",2023)
x2.printname()
x2.welcome()
