#Inheritance example

#Parent class
class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

#Child class
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post

        Person.__init__(self,name,idnumber)


a = Employee("Jerry",564357,2000000,"Intern")

a.display()
