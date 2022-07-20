#Multilayer Inheritances >> Parent --> Child --> Grandchild

#Parent Class
class Base:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

#Child class
class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age

    def getAge(self):
        return self.age


#GrandChild Class
class GrandChild(Child):
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.address = address


    def getAddress(self):
        return self.address


#driver code
g = GrandChild("Bipul",24,"abcde")
print(g.getName(),g.getAge(),g.getAddress())


